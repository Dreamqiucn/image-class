import torch
import numpy as np
from torch import nn
def day50():
    print("pytorch版本：",torch.__version__)
    print("pytorch的cuda版本",torch.version.cuda)
    print("GPU 是否可用：", torch.cuda.is_available())
    devices=["cpu"]
    if torch.cuda.is_available():
        devices.append("cuda")
    for device in devices:
        x=torch.tensor(
            [1.0,2.0,3.0],
            device=device,
            requires_grad=True
        )
        y=(x**2).sum()#x方求和
        y.backward()#求导
        print(device,x.grad,y.item())
def day51():
    x=torch.tensor([[1,2,3],[4,5,6]])
    
    zeros=torch.zeros((2,3))#全0
    print(x,x.shape,x.dtype,x.device)
    x_float=x.to(torch.float32)#改变数据类型
    print(x_float,x_float.dtype)
    num2=np.arange(0,12).reshape(2,6)

    y=torch.from_numpy(num2)#这个是孪生的，a改b也改
    z=torch.tensor(num2)#这个是copy，不是必须一样
    num2[0][3]=100#改数测试
    print(y)
    print(z)
    print(y.numpy())
def day52():
    x=torch.tensor([1,2,3,4,5,6])
    y=x.to("cuda")#gpu运算
    x+=1
    y+=2
    x=x.reshape((2,3))
    x=x.unsqueeze(0)#加个轴0
    print(x.shape)
    x=x.squeeze(0)
    print(x.shape)
    print(y.cpu(),y.cpu().device)
def day53():
    x=torch.tensor([2.0],requires_grad=True)
    y=x**x
    y.backward()#反向求导赋值到x.grad
    print(x.grad)

    y=x**x
    y.backward()
    print(x.grad)#再导一次会叠加
    x.grad.zero_()#清除求导的内容
    y=x**x
    y.backward()
    print(x.grad)    
def day54():
    class samplenet(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc1=nn.Linear(3,4)
            self.relu=nn.ReLU()
            self.fc2=nn.Linear(4,2)
        def forward(self,x):
            x=self.fc1(x)
            x=self.relu(x)
            x=self.fc2(x)
            return x
    x=torch.tensor([2.0,3.0,4.0])
    y=torch.tensor([1.0,2.0,5.0])
    model=samplenet()
    z=model(x)#会自动执行forward的
    w=model(y)
    print(z.shape,w.shape)
    print(z,w)
    print(model.fc1.weight.shape)
    print(model.fc1.bias.shape)
def day55():
    logits=torch.tensor([[2.0,0.0],[1.0,3.0]])
    # targets=logits.argmax(dim=1) 算出最大的数
    targets = torch.tensor([0, 1])
    targets.to(dtype=torch.long)#转换模式
    print(targets.dtype)
    loss_fn = nn.CrossEntropyLoss()  # 创建损失函数
    loss = loss_fn(logits, targets)  # 传入分数和正确标签，计算损失
    print(loss)
    logits[0][1]=9.4
    loss = loss_fn(logits, targets) 
    print(loss)
    logits.requires_grad_(True)
    loss = loss_fn(logits, targets)  # 为了backward
    loss.backward() 
    print(logits.grad)
day55()