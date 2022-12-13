import torch
import torch.nn as nn

class Flatten(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), -1)


class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=10, kernel_size=3, stride=1),
            nn.BatchNorm2d(10),
            nn.leaky_relu(),
            nn.Conv2d(10, 20, 3, 1),
            nn.BatchNorm2d(20),
            nn.leaky_relu(),
            Flatten()
        )

        self.fc = nn.Sequential(
            nn.Linear(None, 64),
            nn.Linear(64, 2),
            nn.Softmax()
        )

    def forward_once(self,x):
        output = self.cnn(x)
        return output


    def forward(self,x1,x2):
        output1 = self.forward_once(x1)
        output2 = self.forward_once(x2)
        output = torch.cat((output1,output2),1)
        output = self.fc(output)
        return output
