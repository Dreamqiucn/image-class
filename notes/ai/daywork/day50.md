# Day 50：PyTorch 环境和首次运算

日期：2026-11-09。用户自行操作安装与核心练习，结束当天后统一记录。

## 当前环境检查

- 2026-11-09 本机检查：RTX 5070 Ti Laptop GPU，驱动 616.92，显存 12227 MiB；image-class-conda Python 3.12.15 当前未发现 torch。
- 官方安装清单提供 Windows CUDA 13.0 版本：`python -m pip install torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/cu130`。由用户在确认使用的 Conda 环境中执行；未验证安装或 GPU 运算。
- 参考：[PyTorch 安装版本](https://pytorch.org/get-started/previous-versions/)。CUDA 版本、环境与设备支持以安装后实测为准。

## 基础理解与练习

PyTorch 是用于张量计算和深度学习的框架，Tensor 可理解为具有设备、数据类型和形状的多维数组；自动求导用于计算梯度。用户先自行安装，再执行以下验证：

```python
import torch
print("PyTorch:", torch.__version__)
print("CUDA build:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())
for device in (["cpu", "cuda"] if torch.cuda.is_available() else ["cpu"]):
    x = torch.tensor([1.0, 2.0, 3.0], device=device, requires_grad=True)
    y = (x ** 2).sum()
    y.backward()
    print(device, "result:", y.item(), "grad:", x.grad.cpu().tolist())
```

预期 CPU 结果为 14.0、梯度 [2.0, 4.0, 6.0]；若 CUDA 可用还应运行并输出相同的 CUDA 结果。设备是否真实可用以实际运算结果为准。如果 CUDA 不可用只打印 CPU，不记 GPU 已通过。

今日任务：自行安装、确认 VS Code Python 环境，运行验证并理解 device 和打印结果；出错时保留报错。初次运行中 CUDA 是否可用需要观察，不自动修改依赖文件或进行 Git 操作。
