import os
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as tt


face_classifier = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
model_state = torch.load('./models/emotion_detection_model_state.pth')

class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Suprise']


def conv_block(in_channels, out_channels, pool=False):
    layers = [nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1), 
              nn.BatchNorm2d(out_channels), 
              nn.ELU(inplace=True)]
    if pool: layers.append(nn.MaxPool2d(2))
    return nn.Sequential(*layers)

class ResNet(nn.Module):
    def __init__(self, in_channels, num_classes):
        super().__init__()
        
        self.conv1 = conv_block(in_channels, 128)
        self.conv2 = conv_block(128, 128, pool=True)
        self.res1 = nn.Sequential(conv_block(128, 128), conv_block(128, 128))
        self.drop1 = nn.Dropout(0.5)
        
        self.conv3 = conv_block(128, 256)
        self.conv4 = conv_block(256, 256, pool=True)
        self.res2 = nn.Sequential(conv_block(256, 256), conv_block(256, 256))
        self.drop2 = nn.Dropout(0.5)
        
        self.conv5 = conv_block(256, 512)
        self.conv6 = conv_block(512, 512, pool=True)
        self.res3 = nn.Sequential(conv_block(512, 512), conv_block(512, 512))
        self.drop3 = nn.Dropout(0.5)
        
        self.classifier = nn.Sequential(nn.MaxPool2d(6), 
                                        nn.Flatten(),
                                        nn.Linear(512, num_classes))
        
    def forward(self, xb):
        out = self.conv1(xb)
        out = self.conv2(out)
        out = self.res1(out) + out
        out = self.drop1(out)
        
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.res2(out) + out
        out = self.drop2(out)
        
        out = self.conv5(out)
        out = self.conv6(out)
        out = self.res3(out) + out
        out = self.drop3(out)
        
        out = self.classifier(out)
        return out

model = ResNet(1, len(class_labels))
model.load_state_dict(model_state)


files = []
for i in range(1, 6):
    rgb_image = cv2.imread('face/' + str(i)+'.jpg')
    files.append(rgb_image)

k = 1
for file in files:
    print(k)
    k += 1
    labels = []
    gray = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(file ,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray,(48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray])!= 0:
            roi = tt.functional.to_pil_image(roi_gray)
            roi = tt.functional.to_grayscale(roi)
            roi = tt.ToTensor()(roi).unsqueeze(0)

            # make a prediction on the ROI
            tensor = model(roi)
            pred = torch.max(tensor, dim=1)[1].tolist()
            label = class_labels[pred[0]]
            print(label)

        else:
            print('No Face Found')

            







