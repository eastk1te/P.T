import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module):
    
    def __init__(self, output_classes):
        super(LeNet, self).__init__()

        self.feature_extractor = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, stride=1), # C1 : feture maps 6@28x28
            nn.ReLU(), # activation function
            nn.AvgPool2d(kernel_size=2), # S2 : feature maps 6@14x14
            nn.Conv2d(6, 16, kernel_size=5, stride=1), # C3 : feture maps 16@14x14
            nn.ReLU(), # activation function
            nn.AvgPool2d(kernel_size=2) # S4 : feature maps 6@10x10
        )

        self.classifier = nn.Sequential(
            nn.Linear(16 * 4 * 4, 120), # C5 : layers 120
            nn.ReLU(), # activation function
            nn.Linear(120, 84), # C6 : layers 84
            nn.ReLU(), # activation function
            nn.Linear(84, output_classes) # output : layers 10
        )

        self.conv1 = nn.Conv2d(1, 6, kernel_size=5) # input_kernel : 1, output_kernel : 6
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5) # input_kernel : 6, output_kernel : 16
        self.fc1 = nn.Linear(16 * 4 * 4, 120) # 256 to 120
        self.fc2 = nn.Linear(120, 84) # 120 to 84
        self.fc3 = nn.Linear(84, 10) # 84 to 10

    def forward(self, input):
        
        x = input # Input : 32 x 32
        x = self.feature_extractor(x) # C1, S2, C3, S4
        x = torch.flatten(x, 1) # Flatten
        logits = self.classifier(x) # C5, C6, output
        probs = F.softmax(logits, dim=1)
        return logits, probs