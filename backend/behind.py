from PIL import Image,ImageOps
import torch
import torch.nn as nn
import torchvision as torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import os
#from backend.modeclass import CNN
import io

# INPUT CHANNELS FOR CNN or Neural Networks -> ( No. of batches, No. of channels, Width, Height )
output_labels = ["0","1","2","3","4","5","6","7","8","9"]


PATH = os.getcwd()

class Predictive:
    def __init__(self):
        #self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.output_labels = ["0","1","2","3","4","5","6","7","8","9"]
        self.size = (28,28)

def inference(images):
    obj = Predictive()
    
    print("error here 1")

    class CNN(nn.Module):
        def __init__(self):
            super(CNN,self).__init__()

            self.conv1 = nn.Conv2d(in_channels=1,out_channels=8,kernel_size=(5,5))
            self.conv2 = nn.Conv2d(in_channels=8,out_channels=16,kernel_size=(4,4))
            # self.conv2 = nn.Conv2d(in_channels=16,out_channels=32,kernel_size=(4,4)) optional 

            self.maxpool = nn.MaxPool2d((2,2))

            self.linear1 = nn.Linear(256,120)
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
    model = CNN()
    m = torch.load('./backend/model.pt',map_location=torch.device('cpu'))['state_dict']
    model.load_state_dict(m)
#    model = torch.load('./backend/inference.pth',map_location=('cpu'))
    model.eval() # inference mode, disables dropout

    print("error here 2")

    #size = (28,28)'
    image = Image.open(io.BytesIO(images)) # './backend/s.png'
    image = image.resize(obj.size)
    image = ImageOps.grayscale(image)

    transform = torchvision.transforms.Compose([
            transforms.Resize(obj.size),
            transforms.ToTensor(),
            transforms.Normalize( (0.1307,),(0.3081,) )
    ])

    image = transform(image).float()

    image = image.unsqueeze(0) # creates new dimension at each item or specified position

        #image = image.to(device)       Try to enable cuda , as the model weights are trained from GPU Tensors

    output = model(image)
    _ , prediction = torch.max(output,1)
    return obj.output_labels[prediction.item()],True

#print(inference())