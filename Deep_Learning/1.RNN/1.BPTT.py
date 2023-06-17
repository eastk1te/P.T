'''
BPTT는 RNN을 펼친 후에 일반적인 역전파 알고리즘을 적용한 것으로 이해할 수 있습니다. 
펼친 RNN은 시간의 흐름에 따라 여러 개의 중복되는 계층으로 구성되어 있으며, 
각 계층에서의 역전파는 순전파와 마찬가지로 그래디언트를 전파하면서 가중치를 업데이트합니다. 
이를 반복하면 BPTT를 구현할 수 있습니다.

'''

import numpy as np

class BPTT:

  def __init__(self, input_size, hidden_size, output_size):
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.output_size = output_size

    # 가중치 초기화
    self.W_hh = np.random.randn(hidden_size, hidden_size)
    self.W_xh = np.random.randn(hidden_size, input_size)
    self.W_yh = np.random.randn(output_size, hidden_size)
    
    # 편향 초기화
    self.b_h = np.zeros((hidden_size, 1))
    self.b_y = np.zeros((output_size, 1))

    # 중간 결과 저장을 위한 변수
    self.hidden_states = {}
    self.outputs = {}

  def forward(self, inputs):
    T = len(inputs)
    self.hidden_states[-1] = np.zeros((self.hidden_size, 1))  # 초기 은닉 상태
    for t in range(T):
        x = inputs[t]
        h = np.tanh(np.dot(self.W_hh, self.hidden_states[t-1]) + np.dot(self.W_xh, x) + self.b_h)
        y = np.dot(self.W_yh, h) + self.b_y
        self.hidden_states[t] = h
        self.outputs[t] = y
    return self.outputs

  def backward(self, dh_next):
    W_x, W_h, bias = self.params
    input_data, h_prev, h_next = self.temp

    dt = dh_next * (1 - h_next**2)
    db = np.sum(dt, axis=0)
    dWh = np.matmul(h_prev.T, dt)
    dh_prev = np.matmul(dt, W_h.T)
    dWx = np.matmul(input_data.T,dt)
    dx = np.matmul(dt, W_x.T)

    self.grads[0][...] = dWx
    self.grads[1][...] = dWh
    self.grads[2][...] = db
    return dx, dh_prev