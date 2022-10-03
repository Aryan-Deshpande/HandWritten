from PIL import Image,ImageOps
import torch
import torch.nn as nn
import torchvision as torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import os
from torchvision.transforms import ToTensor
from backend.model_class import CNN, Predictive, output_labels

# INPUT CHANNELS FOR CNN or Neural Networks -> ( No. of batches, No. of channels, Width, Height )

PATH = os.getcwd()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def inference(image):
    attribute = Predictive()

    model = CNN()
                                                            #model.load_state_dict(torch.load('./backend/model.pth', map_location=torch.device('cpu')))
    state_dict = torch.load('./backend/model.pt', map_location=torch.device('cpu'))
    print(state_dict)
    model.load_state_dict(state_dict=state_dict)
    #model.eval() # inference mode, disables dropout

    #databytes = io.BytesIO(image_bytes)                     # './backend/s.png'
                                                            #image = image.resize(att.size) --> optional
                                                            #image = ImageOps.grayscale(image)

    transform = torchvision.transforms.Compose([
            transforms.Grayscale(),
            transforms.Resize(attribute.size),
            transforms.ToTensor(),

            # IMAGE = ( IMAGE - MEAN ) / SD
            transforms.Normalize( (0.1307,),(0.3081,) )
    ])



    image1 = Image.open(image)
 
    image1 = transform(image1).float()

    image1 = image1.unsqueeze(0) # creates new dimension at each item or specified position

                                                #image = image.to(device)       #Try to enable cuda , as the model weights are trained from GPU Tensors
    
    output = model(image1)
    _ , prediction = output.max(1)
                                                #return att.output_labels[prediction.item()],True
    print(prediction)
    return prediction
