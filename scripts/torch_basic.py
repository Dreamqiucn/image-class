import torch
import numpy as np
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
day51()