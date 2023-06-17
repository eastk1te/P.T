import numpy as np

class TimeRNN:

  def __init__(self, W_x, W_h, bias, stateful=False):
    self.params = [W_x, W_h, bias]
    self.grads = [np.zeros_like(W_x), np.zeros_like(W_h), np.zeros_like(bias)]
    self.layers = None
    self.hidden_state = None
    self.dh = None
    self.stateful = stateful

  def set_state(self, hidden_state):
    self.hidden_state = hidden_state
  
  def reset_state(self):
    self.hidden_state = None

  def forward(self, input_data):
    W_x, W_h, bias = self.params
    N, T, D = input_data.shape
    D,H = W_x.shape

    self.layers = []
    output = np.empty((N,T,H), dtype='f')

    if not self.statefull or self.hidden_state is None:
      self.hidden_state = np.zeros((N,H), dtype='f')

    for t in range(T):
      layer = RNN(*self.params)
      self.hidden_state = layer.forward(input_data[:,t,:], self.h)
      output[:,t,:] = self.hidden_state
      self.layers.append(layer)

    return output

  def backward(self, doutput):
    W_x, W_h, bias = self.params
    N, T, D = input_data.shape
    D,H = W_x.shape

    dinput = np.empty((N,T,D), dtype='f')
    dh = 0
    grads = [0,0,0]

    for t in reversed(range(T)):
      layer = self.layers[t]
      dx, dh = layer.backward(doutput[:,t,:] + dh)
      dinput[:mt,:] = dx

      for i, grad in enumerate(layer.grads):
        grads[i] += grad

    for i, grad in enumerate(grads):
      self.grads[i[...]] = grad
    
    self.dh = dh

    return dinput
     