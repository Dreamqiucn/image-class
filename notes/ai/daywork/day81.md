# Day 81：把残差连接封装成 BasicBlock

状态：核心任务完成。已将 Day 80 的残差计算封装为可重复使用的 `nn.Module`。运行结果见 [Day 81 记录](../records/day81-record.md)。

## 知识要点

一个同通道、同尺寸的 BasicBlock 接收输入 `x`，主分支依次经过 `Conv → BN → ReLU → Conv → BN` 得到 `F(x)`，随后将它与保留下来的原输入相加，再经过 ReLU 得到输出。今天两条分支的形状相同，跳跃分支直接使用 `x`。

`__init__` 中创建层并保存为 `self` 属性；`forward(self, x)` 中使用这些层计算并返回结果。调用 `block(x)` 时会执行 `forward`。

## 今日任务

在 `scripts/torch_week12.py` 中自己实现一个继承 `nn.Module` 的 `BasicBlock`。创建对象时传入通道数 `channels`，两次卷积的输入和输出通道数都为该值，使用 `3×3` 卷积、`stride=1`、`padding=1`、`bias=False`，两次卷积后各接对应通道数的 `BatchNorm2d`；只在第一组卷积和 BN 后接 ReLU，主分支结果与原输入相加后再次使用 ReLU，并返回输出。

创建 `BasicBlock(16)` 和形状 `(2, 16, 56, 56)` 的随机输入，执行一次前向计算，打印输入和输出的 shape。预期两者都是 `torch.Size([2, 16, 56, 56])`。如需使用 GPU，模型和输入要放在相同设备上；CPU 也足够完成本练习。

想一想：为什么主分支的输出可以直接和输入相加？如果输入和输出的通道数不同，今天的直接相加是否还适用？
