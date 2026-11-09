# Day 51：Tensor 创建、属性和 NumPy 转换

日期：2026-11-09。用户自行编写练习，结束当日后统一记录。

## Tensor

```python
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print(x)
print(x.shape)
print(x.dtype)
```

输出二维 tensor `[[1., 2., 3.], [4., 5., 6.]]`、`torch.Size([2, 3])`、`torch.float32`。

`torch.zeros((2, 3))` 创建 2 行 3 列的零 Tensor；`x.to(torch.int64)` 返回指定类型的结果，除非重新赋值不改变原变量的 dtype。

## 与 NumPy 转换

```python
import numpy as np
a = np.array([1, 2, 3])
t = torch.from_numpy(a)
a[0] = 9
print(t)
print(t.numpy())
```

输出 `tensor([9, 2, 3])`、`[9 2 3]`。本例 NumPy 数组与 CPU Tensor 共享数据；torch.tensor(a) 创建副本。普通的 numpy() 可用于 CPU 且不需要梯度的 Tensor，返回的数组通常共享数据。

## 今日任务

1. 创建至少一个二维 Tensor 和一个 zeros Tensor，打印值、shape、dtype。
2. 将 Tensor 转换 dtype 并比较原变量与转换结果。
3. 用 NumPy 创建数组，通过 from_numpy 转为 Tensor；修改一方观察另一方，再用 tensor 创建独立副本。将一个 CPU、无梯度 Tensor 转回 NumPy。

参考：[PyTorch Tensor 入门](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)。

## 完成情况

用户完成核心练习并明确结束；类型转换和 NumPy 共享、副本结果已实际运行确认。详情见 [当日记录](../records/day51-record.md)。
