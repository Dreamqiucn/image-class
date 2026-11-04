# Day 44：NumPy 条件、范围、预测和矩阵乘法

日期：2026-11-04。巩固周第 2 天，用户自行写练习；当天结束后统一记录。

## where 与 clip

```python
import numpy as np
a = np.array([-10, 30, 260])
print(np.where(a > 100, 100, a))
print(np.clip(a, 0, 255))
print(a)
```

输出 `[ -10   30  100]`、`[  0  30 255]`、`[-10  30 260]`。where 根据条件选择，clip 限制范围；这两次调用不改变原数组。

## argmax

```python
scores = np.array([[0.1, 0.7, 0.2], [0.8, 0.1, 0.1]])
print(scores.argmax(axis=1))
```

输出 `[1 0]`：沿第 1 轴分别找到每一行最大值的下标，模拟两张图片的预测编号；不是最大分数本身。

## 逐元素乘法与矩阵乘法

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 0], [1, 2]])
print(a * b)
print(a @ b)
```

输出分别为 `[[2 0], [3 8]]` 和 `[[4 4], [10 8]]`。对于二维矩阵，@ 要求左边列数等于右边行数，结果形状为左边行数、右边列数。

## 今日任务

1. 用一维数组自行试 where 与 clip，并对照原数组。
2. 创建两行模拟类别分数，用 argmax 找出每行预测类别编号。
3. 对两个 2×2 数组分别计算 `*` 和 `@`，输出结果并解释其中一个位置。

参考：[where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)、[clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html)、[argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)、[matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)。
