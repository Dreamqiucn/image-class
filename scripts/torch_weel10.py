import torch
from torch import nn
from PIL import Image
from torch.utils.data import DataLoader
from torchvision.transforms import RandomHorizontalFlip
import numpy as np
def day64():
    class photo_process(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1) :
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)
                pixels=pixels/255.0
                return pixels,label
    photo_list=[("1/丰川祥子/saki.webp",0),("1/汐见萤/shiomi.webp",1),("1/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("photos/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list),batch_size=2,shuffle=False)
    conv=nn.Conv2d(
        in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1
    )
    for images,labels in train_loader: 
        features=conv(images)
        print(features.shape)
def day65():
    class photo_process(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1) :
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)
                pixels=pixels/255.0
                return pixels,label
    photo_list=[("1/丰川祥子/saki.webp",0),("1/汐见萤/shiomi.webp",1),("1/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("photos/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list),batch_size=2,shuffle=False)
    layers=nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2,stride=2),
        nn.Flatten()
    )
    for images,labels in train_loader:
        print("输入",images.shape) 
        for layer in layers:
            images=layer(images)
            print(layer.__class__.__name__, images.shape)
day65()