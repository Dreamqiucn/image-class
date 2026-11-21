# Day 65 · 把卷积特征接到分类层

延续 Day 64 的 `Conv2d(3, 8, kernel_size=3, stride=1, padding=1)`。今天用同一批两张图，依次经过 `Conv2d → ReLU → MaxPool2d → Flatten → Linear`，看清每层怎样改变数字或形状。

## ReLU 和最大池化

`nn.ReLU()` 把负数设为 0，保留非负数与张量形状。`nn.MaxPool2d(kernel_size=2, stride=2)` 在每张特征图上用 `2×2` 窗口取最大值，窗口每次移动两格。输入高宽都是 64 时，输出高宽都是 32，通道数仍为 8。

```python
import torch
from torch import nn

x = torch.tensor([[[[-3.0, 5.0], [2.0, -1.0]]]])
activated = nn.ReLU()(x)
pooled = nn.MaxPool2d(kernel_size=2, stride=2)(activated)
print(activated.tolist())  # [[[[0.0, 5.0], [2.0, 0.0]]]]
print(pooled.tolist())     # [[[[5.0]]]]
```

这里 `nn.ReLU()` 创建一个层，后面的 `(x)` 才是让这个层处理张量。池化的写法同理。

## 展平与分类

`nn.Flatten()` 默认保留第 0 维，也就是批次维。它把每张图的通道、高、宽合成一行，`(2, 8, 32, 32)` 变成 `(2, 8192)`，因为 `8 × 32 × 32 = 8192`。把每张图的 8192 个特征交给 `nn.Linear(8192, 2)`，每张图得到两个类别分数。

## 今天的练习

在现有图片读取代码上取一批图，接上这四层，每过一层打印一次形状。先根据池化后的通道、高、宽算出 `Linear` 的输入特征数。最后检查 logits 是否有两行、每行两个分数。

```text
输入        (2, 3, 64, 64)
Conv2d      (2, 8, 64, 64)
ReLU        (2, 8, 64, 64)
MaxPool2d   (2, 8, 32, 32)
Flatten     (2, 8192)
Linear      (2, 2)
```

参考 [PyTorch 网络搭建教程](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) 和 [MaxPool2d 文档](https://docs.pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html)。
