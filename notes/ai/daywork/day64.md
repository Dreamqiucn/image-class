# Day 64 · 用 Conv2d 提取图像特征

今天用一个卷积层观察图像怎样变成特征图。拿 Day 62 的一批 RGB 图片，先预测输出形状，再实际打印核对。

## 卷积层怎样计算

卷积核是一组可学习的权重。以单通道为例，`2×2` 的卷积核覆盖输入的一个 `2×2` 小块，对应位置相乘再求和，得到输出上的一个数。把卷积核移到下一处，用同一组权重再算一次。

```text
输入         卷积核       输出
1  2  3     1  0        6   8
4  5  6     0  1       12  14
7  8  9
```

步幅为 1、无填充时，左上角的输出是 `1×1 + 2×0 + 4×0 + 5×1 = 6`。RGB 图片有 3 个输入通道，每个滤波器都覆盖这 3 个通道，把三个通道的计算结果加起来，再加一个偏置，得到一张输出特征图。

## PyTorch 参数和形状

```python
conv = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, stride=1, padding=1)
features = conv(images)
print(images.shape, features.shape)
```

`in_channels=3` 对应 RGB，`out_channels=8` 表示有 8 张输出特征图。`kernel_size=3` 表示每次覆盖 `3×3` 的区域。`stride=1` 表示每次移动一个像素。`padding=1` 默认在上下左右各补一圈零。

输入为 `(N, C, H, W)`。批次大小 `N` 保持不变，输出通道由 `out_channels` 决定。默认 `dilation=1` 时，输出高度和宽度分别按下面的式子计算。

```text
输出长度 = (输入长度 + 2 × padding - kernel_size) // stride + 1
```

比如输入是 `(2, 3, 64, 64)`，用上述参数，输出是 `(2, 8, 64, 64)`。卷积权重 `conv.weight` 的形状是 `(8, 3, 3, 3)`，依次是输出通道数、输入通道数、核的高和宽。

## 今天的任务

用 `next(iter(train_loader))` 取出一批真实图片。在同一批图片上试下面三组参数，每组都先手算输出形状，再调用 `conv(images)` 并打印形状来核对。三组都用 3 个输入通道、8 个输出通道和 `3×3` 卷积核。

| 组别 | stride | padding |
| --- | --- | --- |
| A | 1 | 0 |
| B | 1 | 1 |
| C | 2 | 1 |

完成时能解释 `out_channels=8` 代表什么，以及哪组保留了原图的高和宽。今天只做卷积前向和形状检查。

## 收尾

2026-11-20 核心完成。用户确认已运行三组卷积参数。用 `3×3` 卷积核时，`(stride, padding) = (1, 1)` 保留 64×64 高宽。见 [Day 64 记录](../records/day64-record.md)。

参考 [PyTorch Conv2d 文档](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Conv2d.html)。
