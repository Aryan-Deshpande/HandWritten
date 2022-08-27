# model predictino routes / backend 
from pprint import pprint
import torch
import torchvision
import torchvision.transforms as transforms


def getpred(image):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    prediction = 0
    PIL = transforms.ToPILImage()
    resize = torchvision.transforms.Resize(28)
    transform = transforms.ToTensor()

    newimg = transform(image)
    img = PIL(newimg)
    resizedimg = resize(img)

    img2 = resizedimg.to(device)

#    new2 = new2.to(device) // need to change this so that maybe collab notebook works real time ?

    input = img2.unsqueeze(0)

    model = torch.load('best_model.pth')
    model.eval()
    prediction = torch.argmax(model(input))

    print(prediction)
    # dont need a database
import cv2

image = cv2.imread("C:/Users/deshp/Desktop/APIs/HandWritten/backend/test.png",0)
print(image.size)
getpred(image)
