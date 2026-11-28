import torch
from torch import nn
from PIL import Image
from torch.utils.data import DataLoader
from torchvision.transforms import RandomHorizontalFlip
import numpy as np
import matplotlib.pyplot as plt
import csv
from pathlib import Path
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def day78():
    def day78_1():
        print("day78_1")
        x=torch.randn(2,16,56,56)
        layers=nn.Sequential(
            nn.Conv2d(16,16,kernel_size=3,stride=1,padding=1),
            nn.Conv2d(16,16,kernel_size=3,stride=1,padding=1)
        )
        for layer in layers:
            x=layer(x)
            print(x.shape)
    def day78_2():
        print("day78_2")
        x=torch.randn(2,16,56,56)
        layers=nn.Sequential(
            nn.Conv2d(16,16,kernel_size=3,stride=2,padding=1),
            #上面的是主分支
            nn.Conv2d(16,16,kernel_size=3,stride=1,padding=1)
        )
        for layer in layers:
            x=layer(x)
            print(x.shape)
    def day78_3():
        print("day78_3")
        x=torch.randn(2,16,56,56)
        x_odd=torch.randn(2,16,55,55)
        layers=nn.Sequential(
            nn.Conv2d(16,32,kernel_size=1,stride=2,padding=0),
        )#跳跃分支
        for layer in layers:
            out=layer(x)
            out2=layer(x_odd)
            print(out.shape)
            print(out2.shape)
def day79():
    conv=nn.Conv2d(3,8,kernel_size=3,stride=1,padding=1,bias=False)
    bn=nn.BatchNorm2d(8)#它的值要与out_channel一样,它是让平均值趋向0，方差趋向1的
    x=torch.randn(2,3,4,4)+10.0
    bn.train()#训练模式可以更改running_mean,running_var，不可以抄经验
    out_train=bn(conv(x))
    print(out_train.shape,bn.running_mean)
    bn.eval()#推理模式
    out_eval=bn(conv(x[:1]))
    print(out_eval.shape)
    print(bn.running_mean,bn.running_var)
def day80():
    x=torch.randn(2,16,56,56)
    main_path=nn.Sequential(
        nn.Conv2d(16,16,3,stride=1,padding=1,bias=False),
        nn.BatchNorm2d(16),
        nn.ReLU(),
        nn.Conv2d(16,16,3,stride=1,padding=1,bias=False),
        nn.BatchNorm2d(16)
    )
    fx=main_path(x)
    out=torch.relu(fx+x)
    print(x.shape,fx.shape,out.shape)
    # print(out)
def day81():
    x=torch.randn(2,16,56,56)
    class BasicBlock(nn.Module):
        def __init__(self,channels):
            super().__init__()
            self.channels=channels
            self.main_path=nn.Sequential(
                nn.Conv2d(self.channels,self.channels,3,stride=1,padding=1,bias=False),
                nn.BatchNorm2d(self.channels),
                nn.ReLU(),
                nn.Conv2d(self.channels,self.channels,3,stride=1,padding=1,bias=False),
                nn.BatchNorm2d(self.channels))
        def forward(self,x):
            self.x=x
            out=torch.relu(self.main_path(self.x)+self.x)
            return out
    block16=BasicBlock(16)
    print(block16(x).shape)
day81()
