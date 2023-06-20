import numpy as np

class BPTT:

    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # 가중치 초기화
        self.W_h = np.random.randn(hidden_size, hidden_size)
        self.W_x = np.random.randn(hidden_size, input_size)
        self.W_y = np.random.randn(output_size, hidden_size)
        
        # 계산 간단화를 위해 편향 제거

    def forward(self, inputs):
        
        self.h_states = [np.zeros((self.hidden_size, 1))] # 각 시간별 h
        self.outputs = [] # 각 시간별 a 결과값

        for x in inputs:
            self.h = np.tanh(np.dot(self.W_h, self.h_states[-1]) + np.dot(self.W_x, x))
            self.a = np.dot(self.W_y, self.h)

            self.h_states.append(self.h)
            self.outputs.append(self.a)

        return self.outputs
    
    def backward(self, inputs, targets):

        T = len(inputs)
        
        y_states = [np.zeros((self.hidden_size, 1))]
        
        dW_h = np.zeros_like(self.W_h)
        dW_x = np.zeros_like(self.W_x)
        dW_y = np.zeros_like(self.W_y)

        for t in range(T):
            x, target = inputs[t], targets[t]

            h = self.h_states[t+1]
            a = self.outputs[t] # 현재 t 시점의 결과값

            da = a - target # 현재 t 시점의 오차(delta) 계산

            # 이전 단계의 은닉상태로부터 전달되는 오차와 현재 출력값에 대한 오차의 가중합을 계산
            
            dtanh = (np.dot(self.W_y.T, da) + np.dot(self.W_h.T, y_states[-1]))  * (1 - h ** 2) 
            y_states.append(dtanh)

            dW_h += np.outer(dtanh, y_states[t])
            dW_y += np.outer(da, h)
            dW_x += np.outer(dtanh, x)
       
        # 가중치 업데이트
        self.W_h -= self.learning_rate * dW_h
        self.W_x -= self.learning_rate * dW_x
        self.W_y -= self.learning_rate * dW_y
        
    
    def train(self, inputs, targets, num_epochs):
        for epoch in range(num_epochs):
            
            loss = self.train_sequence(inputs, targets)
            
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss / len(inputs)}")


    def train_sequence(self, inputs, targets):
        outputs = self.forward(inputs)
        self.backward(inputs, targets)
        loss = self.MSE(outputs, targets)

        return loss
    
    def MSE(self, x, y):
        return np.mean((x-y)**2)
    
if __name__ == '__main__':

    np.random.seed(0)

    # 입력 데이터와 타깃 데이터 생성
    def generate_data(sequence_length, num_samples):
        
        data = []
        label = []
        temp = np.random.uniform(0, 1, num_samples)

        for i in range(num_samples):
            # 입력 데이터는 0과 1 사이의 랜덤한 값으로 구성된 시계열 데이터입니다.
            X = np.arange(temp[i], temp[i]+sequence_length,1).reshape(-1,1)
            
            # 타깃 데이터는 입력 데이터의 이전 값과의 관계에 따라 정의합니다.
            Y = np.zeros((sequence_length, 1))
            Y[1:] = X[:-1]  # 타깃 데이터는 입력 데이터의 이전 값을 가져옵니다.
            data.append(X)
            label.append(Y)
        return np.array(data), np.array(label)
  
    sequence_length = 10

    # 예제 학습 코드
    hidden_size = 16
    learning_rate = 0.01
    num_epochs = 10
    num_samples = 100

    data, label = generate_data(sequence_length, num_samples)

    model = BPTT(sequence_length, hidden_size, sequence_length, learning_rate)
    
    model.train(data, label, num_epochs)
