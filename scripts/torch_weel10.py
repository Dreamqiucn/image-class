import torch
from torch import nn
from PIL import Image
from torch.utils.data import DataLoader
from torchvision.transforms import RandomHorizontalFlip
import numpy as np
import matplotlib.pyplot as plt
import csv
from pathlib import Path

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
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list),batch_size=2,shuffle=False)
    conv=nn.Conv2d(
        in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1
    )   #三通道rgb(2,3,64,64)     输出8通道(2,8,64,64) 大小 步长 外边一圈
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
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list),batch_size=2,shuffle=False)
    layers=nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2,stride=2),#64->32
        nn.Flatten()
    )
    for images,labels in train_loader:
        print("输入",images.shape) 
        for layer in layers:
            images=layer(images)
            print(layer.__class__.__name__, images.shape)
            #     model里面这一步操作的名字
def day66():
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
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list),batch_size=2,shuffle=False)
    layers=nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2,stride=2),
        nn.Flatten(),
        nn.Linear(8192,2)
    )
    loss_fn=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(layers.parameters(),lr=0.01)#把layers的信息都给optimizer
    for epoch in range(20):
        correct=0
        loss_ave=0#平均loss
        for images,labels in train_loader:
            logits=layers(images)
            loss=loss_fn(logits,labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            pred=logits.argmax(dim=1)
            correct+=(pred==labels).sum().item()
            loss_ave+=loss*labels.size(0)
        print("平均loss",loss_ave.item()/len(photo_list),"正确数",correct)
def day67():
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
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list,0),batch_size=2,shuffle=False)
                                            #验证集不需要图片反转，不需要顺序打乱
    layers=nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2,stride=2),
        nn.Flatten(),
        nn.Linear(8192,2)
    )
    loss_fn=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(layers.parameters(),lr=0.01)#把layers的信息都给optimizer
    for epoch in range(20):
        layers.train()
        loss_ave=0#平均loss
        for images,labels in train_loader:
            logits=layers(images)
            loss=loss_fn(logits,labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            loss_ave+=loss*labels.size(0)
        print("训练")
        print("平均loss",loss_ave.item()/len(photo_list),"\n")
        layers.eval()#验证模式
        correct=0
        loss_ave=0

        with torch.no_grad():
            for images,labels in val_loader:
                logits=layers(images)
                loss=loss_fn(logits,labels)
                pred=logits.argmax(dim=1)
                correct+=(pred==labels).sum().item()
                loss_ave+=loss*labels.size(0)
            print("验证")
            print("平均loss",loss_ave.item()/len(new_photo_list),"正确数",correct,"\n")
def day68():
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
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photo_process(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photo_process(new_photo_list,0),batch_size=2,shuffle=False)
                                            #验证集不需要图片反转，不需要顺序打乱
    layers=nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2,stride=2),
        nn.Flatten(),
        nn.Linear(8192,2)
    )
    loss_fn=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(layers.parameters(),lr=0.01)#把layers的信息都给optimizer
    train_loss=[]
    val_loss=[]
    epoch_list=[]
    for epoch in range(20):
        layers.train()
        loss_ave=0#平均loss
        for images,labels in train_loader:
            logits=layers(images)
            loss=loss_fn(logits,labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            loss_ave+=loss*labels.size(0)
        train_loss.append(loss_ave.item()/len(photo_list))
        print("训练")
        print("平均loss",loss_ave.item()/len(photo_list),"\n")
        layers.eval()#验证模式
        correct=0
        loss_ave=0

        with torch.no_grad():
            for images,labels in val_loader:
                logits=layers(images)
                loss=loss_fn(logits,labels)
                pred=logits.argmax(dim=1)
                correct+=(pred==labels).sum().item()
                loss_ave+=loss*labels.size(0)
            val_loss.append(loss_ave.item()/len(new_photo_list))
            print("验证")
            print("平均loss",loss_ave.item()/len(new_photo_list),"正确数",correct,"\n")
        epoch_list.append(epoch+1)
    print(epoch_list,train_loss,val_loss)
    samples=[epoch_list,train_loss,val_loss]
    with open("output/loss_day68.csv","w",newline="",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["epoch","train_loss","val_loss"])
        for i in range(len(samples[0])):
            writer.writerow([samples[0][i],samples[1][i],samples[2][i]])
    fig ,ax=plt.subplots()
    ax.plot(epoch_list,train_loss,marker="o",label="train loss")
    ax.plot(epoch_list,val_loss,marker="o",label="val loss")
    ax.legend()
    
    #显示右上角的图例，什么点代表什么label
    ax.set_title("Training and validation loss")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    fig.savefig("output/loss_day68.png")
    plt.show()
    Path("output").mkdir(parents=True,exist_ok=True)
    torch.save(layers.state_dict(),"output/day68.pth")
    #保存权重
def day69():
    class photo_process(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1) :
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)
                pixels=pixels/255.0
                return pixels
    val_photo_list=["data/raw/汐见萤/shiomi3.png","data/raw/gpt娘/gpt.png"]
    val_class={
        0:"丰川祥子",
        1:"汐见萤",
        2:"GPT",
        3:"DeepSeek"
    }
    val_loader=DataLoader(photo_process(val_photo_list,0),batch_size=2,shuffle=False)
                                            #验证集不需要图片反转，不需要顺序打乱
    val_model=nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=8,kernel_size=3,stride=1,padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2,stride=2),
        nn.Flatten(),
        nn.Linear(8192,2)    
    )
    weights=torch.load(
        "output/day68.pth",
        weights_only=True,
        map_location="cpu"
    )
    val_model.load_state_dict(weights)
    val_model.eval()#验证模式
    correct=0
    pred_list=[]
    with torch.no_grad():
        for i,images in enumerate(val_loader):#为了得到i，enumerate加了之后变成(i,val_loader)
            for ii,image in enumerate(images):
                logits=val_model(torch.unsqueeze(image,dim=0))
                pred=logits.argmax(dim=1)
                print(logits)
                pred_list.append([val_photo_list[i*val_loader.batch_size+ii],torch.squeeze(logits,dim=0).tolist(),val_class[pred.item()]])
        print(pred_list)

day69()