import torch
import torch.nn as nn
import torchvision as torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

class CNN(nn.Module):
        def __init__(self):
            super(CNN,self).__init__()

            self.conv1 = nn.Conv2d(in_channels=1,out_channels=8,kernel_size=(5,5))
            self.conv2 = nn.Conv2d(in_channels=8,out_channels=16,kernel_size=(4,4))
            # self.conv2 = nn.Conv2d(in_channels=16,out_channels=32,kernel_size=(4,4)) optional 

            self.maxpool = nn.MaxPool2d((2,2))

            self.linear = nn.Linear(256,120)
            self.linear2 = nn.Linear(120,45)
            self.linear3 = nn.Linear(45,10)

            self.dropout = nn.Dropout(0.25)

        def forward(self,x):
            x = F.relu(self.conv1(x))
            x = self.maxpool(x)

            x = F.relu(self.conv2(x))
            x = self.maxpool(x)

            x = x.view(x.size(0),-1)

            x = self.linear(x)
            x = F.relu(x)
            x = self.dropout(x)

            x = self.linear2(x)
            x = F.relu(x)
            x = self.dropout(x)

            x = self.linear3(x)

            return x
        

class Predictive:
    def __init__(self):
        #self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.output_labels = ["0","1","2","3","4","5","6","7","8","9"]
        self.size = (28,28)

output_labels = ["0","1","2","3","4","5","6","7","8","9"]