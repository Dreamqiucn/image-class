import torch
import random
from PIL import Image
from torch.utils.data import DataLoader
from torchvision.transforms import RandomHorizontalFlip
import numpy as np
from torch import nn

def day57_58_59():
    photo_list=list([("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)])
    class photos(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1):
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")#不会转换image本身，应该是新建个变量来存的
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)#调整轴的顺序，显示通道，再是高，宽
                pixels=pixels/255.0
                return pixels,label
    x = random.randint(1, len(photo_list)-1)
    train_dataset=photo_list[x:]
    val_dataset=photo_list[:x]
    x=photos(photo_list)
    y=photos(train_dataset,0.5)
    z=photos(val_dataset,0)
    #因为__init__里面就要sample所以创建函数就需要写，而num是只有调用————getitem————时才需要的所以不必要这时候写
    # x.__len__() = len(x)
    # print(len(x))
    # print(x.__getitem__(2)) = x[2]
    # image,label=x[2]
    # print(image,label)
    loader=DataLoader(x,batch_size=2,shuffle=True)#true是乱序，false顺序
    train_loader = DataLoader(y, batch_size=2, shuffle=True)
    val_loader = DataLoader(z, batch_size=2, shuffle=False)
    for images,labels in loader:
        print(images.shape,labels.tolist())
        #tensor([2, 3, 64, 64]) [0, 1] 先是这一组有2个，再3通道，高，宽。后面是labels都有什么
def day60():
    class photos(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1):
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")#不会转换image本身，应该是新建个变量来存的
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)#调整轴的顺序，显示通道，再是高，宽
                pixels=pixels/255.0
                return pixels,label
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    train_loader=DataLoader(photos(photo_list[:2]),batch_size=2,shuffle=True)
    val_loader=DataLoader(photos(photo_list[2:]),batch_size=2,shuffle=False)
    #DataLoader会自动使用sample[x]，导致__getitem__被偷偷执行了

    model = nn.Sequential(#MLP模型
        nn.Flatten(),#把图片的像素铺平
        nn.Linear(12288,32),#12288是3x64x64
        nn.ReLU(),
        nn.Linear(32,2)
    )

    loss_fn=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(model.parameters(),lr=0.01)#把model的信息都给optimizer
    for epoch in range(1000):
        running=0.0
        total=0
        for image,label in train_loader:
            logits=model(image)#算出来分数
            loss=loss_fn(logits,label)
            #logits是分数，label是正确的答案，这个label是什么无所谓
            #loss算的是是-ln(对应的图片的概率)，logits越大,概率越高，概率越接近1，loss越接近0
            #1.先算出来logits，长tensor([[-1,1],[-2,1]])
            #2.再算概率，通过算概率函数算出来tensor([[0.1,0.9],[0.05,0.95]])
            #3.再算loss，算loss时算的是应该正确的图片的概率
            #比如说第一张图片应该是-ln(0.1)，第二张是-ln(0.95),loss.item()是前面写的两个-ln的平均数
            #概率函数是e^x0/e^x0+e^x1,得到的结果属于0-1
            optimizer.zero_grad()#清除梯度
            loss.backward()#算出loss的梯度
            optimizer.step()#根据梯度知道哪个会导致loss降低，降低拉低logits的权重，更新参数
            running+=loss.item()*label.size(0)#失败的图片数
            total+=label.size(0)#所有多少张图片
            print(epoch,loss,running/total)#第几轮，loss，算错的百分比
def day61():
    class photos(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1):
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")#不会转换image本身，应该是新建个变量来存的
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)#调整轴的顺序，显示通道，再是高，宽
                pixels=pixels/255.0
                return pixels,label
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    train_loader=DataLoader(photos(photo_list[:2]),batch_size=2,shuffle=True)
    val_loader=DataLoader(photos(photo_list[2:]),batch_size=2,shuffle=False)
    #DataLoader会自动使用sample[x]，导致__getitem__被偷偷执行了

    model = nn.Sequential(#MLP模型
        nn.Flatten(),#把图片的像素铺平
        nn.Linear(12288,32),#12288是3x64x64
        nn.ReLU(),
        nn.Linear(32,2)
    )

    loss_fn=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(model.parameters(),lr=0.01)#把model的信息都给optimizer
    images,labels=next(iter(train_loader))#只取一批的images和labels，day60其实不应该写image的，应该加s，因为一次取两张图片
    for epoch in range(20):
        running=0.0
        total=0
        logits=model(images)
        loss=loss_fn(logits,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running+=loss.item()*labels.size(0)
        total+=labels.size(0)
        pred=logits.argmax(dim=1)
        #若logits是torch.tensor([[2.0, 1], [1.2, 1]])，每张图片是类别0,1的分数，argmax是求最大的下标，这时候输出tensor([0, 0])
        if epoch==0 or epoch==19:
            print(epoch,"loss",loss.item(),"平均 loss",running/total,"预测图",pred,"正确数",(pred == labels).sum().item(),"/",len(images))#len(train_loader)得到的是一共有几批
    #下面是写着玩的看看认不认识shiomi
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    new=DataLoader(photos(new_photo_list),batch_size=2,shuffle=False)
    for images,labels in new:
        logits=model(images)
        loss=loss_fn(logits,labels)
        pred=logits.argmax(dim=1)
        print(logits,loss.item(),pred)
def day62():
    class photos(torch.utils.data.Dataset):
        def __init__(self,sample,tran=1):
            super().__init__()
            self.sample=sample
            self.tran=tran
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                rgb=image.convert("RGB")#不会转换image本身，应该是新建个变量来存的
                rgb=rgb.resize((64,64))
                flip=RandomHorizontalFlip(p=self.tran)
                rgb=flip(rgb)
                pixels=torch.from_numpy(np.array(rgb)).permute(2,0,1)#调整轴的顺序，显示通道，再是高，宽
                pixels=pixels/255.0
                return pixels,label
    photo_list=[("data/raw/丰川祥子/saki.webp",0),("data/raw/汐见萤/shiomi.webp",1),("data/raw/汐见萤/shiomi2.webp",1)]
    new_photo_list=[("data/raw/汐见萤/shiomi3.png",1)]
    train_loader=DataLoader(photos(photo_list),batch_size=2,shuffle=True)
    val_loader=DataLoader(photos(new_photo_list),batch_size=2,shuffle=False)

    #DataLoader会自动使用sample[x]，导致__getitem__被偷偷执行了

    model = nn.Sequential(#MLP模型
        nn.Flatten(),#把图片的像素铺平
        nn.Linear(12288,32),#12288是3x64x64
        nn.ReLU(),
        nn.Linear(32,2)
    )

    loss_fn=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(model.parameters(),lr=0.01)#把model的信息都给optimizer
    for epoch in range(20):
        it =iter(train_loader)
        running=0.0
        total=0
        correct=0
        while True:
            try:
                images, labels = next(it)
                logits=model(images)
                loss=loss_fn(logits,labels)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                pred=logits.argmax(dim=1)
                running+=loss.item()*labels.size(0)
                total+=labels.size(0)
                correct+=(pred == labels).sum().item()
            except StopIteration:
                break
        print(epoch,"loss",loss.item(),"平均 loss",running/total,"预测图",pred,"正确数",correct,"/",len(photo_list))
    for images,labels in val_loader:
        logits=model(images)
        loss=loss_fn(logits,labels)
        pred=logits.argmax(dim=1)
        print(logits,loss.item(),pred)
day62()
            