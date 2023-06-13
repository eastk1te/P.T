'''
분류작업을 위한 손실함수로 CrossEntropyLoss 설정.
'''

import torch.nn as nn

def criterion():
    return nn.CrossEntropyLoss()