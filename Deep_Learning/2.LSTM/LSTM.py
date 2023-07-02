import numpy as np

import tensorflow as tf

class LSTM(tf.keras.layers):

    def __init__(self, input_size, hidden_size):
        super(LSTM, self).__init()

        self.input_size = input_size
        self.hidden_size = hidden_size

        initializer = tf.keras.initializers.GlorotUniform()

        self.params = {}
        self.grads = {}
        self.temp = None

        # self.W.shape = (hidden_size * 4, input_size)
        self.W = self.add_weight(shape=(hidden_size * 4, input_size),
                                 initializer=initializer,
                                 name='W')

        self.U = self.add_weight(shape=(hidden_size * 4, hidden_size),
                                 initializer=initializer,
                                 name='U')

        self.b = self.add_weight(shape=(hidden_size * 4, ),
                                 initializer=tf.zeros_initializer(),
                                 name='b')

    def call(self, inputs, states):
        prev_hidden_state, prev_cell_state = states
        
        # x.shape = (batch_size, input_size) => (input_size, batch_size)
        x = tf.transpose(inputs)

        # 이전 hidden state와 input x를 가지고 선형변환을 진행하는 gate식.
        gates = tf.matmul(self.W, x) + tf.matmul(self.U, prev_hidden_state) + self.b

        # tf.matmul(self.W, x) 계산식 
        # => (hidden_size * 4, input_size) x (input_size, batch_size) 
        # tf.matmul(self.U, prev_hidden_state) 계산식
        # => (hidden_size * 4, hiddne_size) x (hidden_size, batch_size)
        # gates.shape = (hidden_size * 4, batch_size)

        i, f, o, c_tilde = tf.split(gates, num_or_size_splits=4, axis=0)

        i = self.sigmoid(i) # input gate
        f = self.sigmoid(f) # forget gate
        o = self.sigmoid(o) # output gate
        c_tilde = self.tanh(c_tilde) # 모델의 단순화를 위해 b_c 편향 제거.

        cell_state = f * prev_cell_state + i * c_tilde
        hidden_state = o * self.tanh(cell_state)

        return hidden_state, cell_state

    def tanh(self, x):
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))