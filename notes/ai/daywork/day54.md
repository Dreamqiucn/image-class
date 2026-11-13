# Day 54：nn.Module 与线性层

日期：2026-11-12。用户自行写网络练习，当天结束后统一记录。

## 目标

理解继承 nn.Module、super().__init__、定义 Linear 层和 forward，通过模拟数据跑通前向传播，不表示训练或真实图片识别。

## 示例

```python
import torch
from torch import nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 4)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(4, 2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        return self.fc2(x)

model = SimpleNet()
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = model(x)
print(x.shape)
print(y.shape)
```

输出 `torch.Size([2, 3])`、`torch.Size([2, 2])`；每行是一个模拟样本，每个样本输入三个特征、输出两个分数。默认参数初始化导致分数不固定，也尚未训练。

Linear(3,4) 的权重形状是 (4,3)，偏置形状是 (4,)；线性层使用 y=xW^T+b。ReLU 对每个数取 max(0,x)，例如 [-2,3] → [0,3]。model(x) 会执行 forward 的过程，保留 Module 的正常调用机制。

## 任务

1. 自行定义继承 nn.Module 的类，包含 Linear、ReLU 和第二个 Linear。
2. 创建至少两个模拟样本，做一次前向传播，打印输入输出的值和 shape。
3. 打印一个 Linear 的 weight 和 bias 的 shape，说明 in_features、out_features 与样本数量的区别。

参考：[PyTorch 构建网络](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html)。

## 完成情况

用户自行建立两层网络并分别输入两条样本；实际运行及形状检查通过，详情见 [当日记录](../records/day54-record.md)。
