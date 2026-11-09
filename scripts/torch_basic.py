import torch
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