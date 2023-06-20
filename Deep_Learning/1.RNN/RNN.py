import numpy as np

class RNN:

    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # 가중치 초기화
        self.W_h = np.random.randn(hidden_size, hidden_size)
        self.W_x = np.random.randn(hidden_size, input_size)
        self.W_y = np.random.randn(output_size, hidden_size)
        
        # 편향 초기화
        self.b_x = np.random.randn(hidden_size, 1)
        self.b_y = np.random.randn(output_size, 1)

        self.h_prev = np.zeros((self.hidden_size, 1))

    def forward(self, x):

        # 순전파 계산
        self.h = np.tanh(np.dot(self.W_h, self.h_prev) + np.dot(self.W_x, x) + self.b_x)

        self.a = np.dot(self.W_y, self.h) + self.b_y
        
        return self.a
    
    def backward(self, x, target, learning_rate):
        # metrics
        metrics = self.MSE(self.a, target)

        # Figure 3의 왼쪽 점선 박스
        da = self.a - target 
        dW_y = np.dot(da, self.h.T)
        db_y = da
        dh = np.dot(self.W_y.T, da)

        # Figure 4
        dtanh = dh * (1 - self.h ** 2) 

        dW_h = np.dot(dtanh, self.h_prev.T)
        dW_x = np.dot(dtanh, x.T)
        db_x = dtanh
       
        # 가중치 업데이트
        self.W_h -= learning_rate * dW_h
        self.W_x -= learning_rate * dW_x
        self.W_y -= learning_rate * dW_y
        self.b_x -= learning_rate * db_x
        self.b_y -= learning_rate * db_y
        
        return metrics
    
    def MSE(self, x, y):
        return np.mean((x-y)**2)
    
    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(X))
    
    def CE_loss(self, y, t):
        epsilon = 1e-10
        return -np.sum(t * np.log(y + epsilon))



if __name__ == '__main__':

    np.random.seed(0)

    # 입력 데이터와 타깃 데이터 생성
    def generate_data(sequence_length):
        # 입력 데이터는 0과 1 사이의 랜덤한 값으로 구성된 시계열 데이터입니다.
        temp = np.random.uniform(0, 1)
        X = np.arange(temp, temp+sequence_length,1).reshape(-1,1)
        
        # 타깃 데이터는 입력 데이터의 이전 값과의 관계에 따라 정의합니다.
        Y = np.zeros((sequence_length, 1))
        Y[1:] = X[:-1]  # 타깃 데이터는 입력 데이터의 이전 값을 가져옵니다.
        
        return X, Y

    sequence_length = 10

    # 예제 학습 코드
    hidden_size = 16
    learning_rate = 0.01
    num_epochs = 1000

    # SimpleRNN 모델 초기화
    model = RNN(sequence_length, hidden_size, sequence_length)

    # 학습 시작
    for epoch in range(1, num_epochs+1):
        # 입력 데이터와 타깃 데이터 생성
        X, Y = generate_data(sequence_length)
        
        # 순전파 및 역전파를 번갈아 수행하는 BPTT 알고리즘.
        y_pred = model.forward(X)
        loss = model.backward(X, Y, learning_rate)
        
        # 현재 에폭의 손실 출력
        if not epoch % 100:
            print(f"Epoch: {epoch}, Loss: {loss}")

    # 예제 테스트 코드
    test_input = np.arange(.5,sequence_length, 1).reshape(-1,1)
    expected_output  = np.zeros((sequence_length, 1))
    expected_output[1:] = test_input[:-1]

    # 테스트 데이터에 대한 예측 수행
    predicted_output = model.forward(test_input)

    print(f"Expected Output: {expected_output.flatten()}")
    print(f"Predicted Output: {predicted_output.flatten()}")
    print(f'Loss : {np.mean((expected_output - predicted_output)**2)}')