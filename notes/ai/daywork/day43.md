# Day 43：NumPy 数组组合与批次维度

日期：2026-11-04。巩固周第 1 天，Day 42 为原计划休息日，未记录为已进行。用户自行编写练习，结束当天后统一记录。

## concatenate 和 stack

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=0).shape)
print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=0).shape)
```

输出：`concatenate` 得到 `[[1 2], [3 4], [5 6], [7 8]]`、shape `(4, 2)`；`stack` 得到 `[[[1 2], [3 4]], [[5 6], [7 8]]]`、shape `(2, 2, 2)`。前者沿已有轴拼接，后者新增一个轴；stack 的输入形状必须相同。

## 图片批次

```python
image1 = np.zeros((2, 3, 3))
image2 = np.ones((2, 3, 3))
batch = np.stack((image1, image2), axis=0)
print(batch.shape)
print(batch[0].shape)
```

输出 `(2, 2, 3, 3)`、`(2, 3, 3)`；依次是图片数、高、宽、通道。图像堆叠前形状必须一致。当前是 NumPy 的 NHWC 示例，后续 PyTorch 常用 NCHW。

## 今日练习

1. 创建两个同形二维数组，分别用 concatenate 的 axis=0、axis=1 和 stack 的 axis=0 输出内容及 shape。
2. 用小数组模拟两张同形 RGB 图片，stack 成批次，取出一张并打印 shape。
3. 对取出的切片分别直接修改及使用 copy 后修改，观察是否影响批次；任选独立的小数组练习也可。

参考：[stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html)、[concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)。

## 完成情况

用户选择进入 Day 44，Day 43 按现有范围结束；未独立运行脚本。详情见 [当日记录](../records/day43-record.md)。
