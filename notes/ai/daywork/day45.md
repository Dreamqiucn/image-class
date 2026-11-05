# Day 45：NumPy 随机数、种子和打乱

日期：2026-11-05，巩固周第 3 天。用户自行写练习；当日结束后统一记录。

## 随机数与种子

```python
import numpy as np
rng1 = np.random.default_rng(42)
rng2 = np.random.default_rng(42)
a = rng1.integers(0, 10, size=5)
b = rng2.integers(0, 10, size=5)
print(a.shape)
print(np.array_equal(a, b))
```

输出 `(5,)` 和 `True`。随机种子用于初始化生成器；在相同环境及调用方式下，两个同种子的生成器产生相同随机序列。连续调用同一生成器会推进状态，不保证相同。

## 打乱

```python
samples = np.array(["a", "b", "c", "d"])
rng = np.random.default_rng(42)
shuffled = rng.permutation(samples)
print(samples)
print(sorted(shuffled) == sorted(samples))
```

输出原数组 `['a' 'b' 'c' 'd']` 和 `True`；打乱结果是新数组，顺序可打印观察，原数组未被修改。

## 今日任务

1. 创建生成器，生成指定范围、数量的随机整数，理解上限默认不包含；打印数组和 shape。
2. 用两个同种子生成器比较结果；再连续使用一个生成器两次，观察结果。
3. 对少量样本进行 permutation，打印打乱前后；若同时有路径和标签，应使用同一组索引打乱，保持配对。

数据划分仅用模拟数据说明；正式数据需避免同一原图及变体跨集合造成泄漏。参考：[Generator](https://numpy.org/doc/stable/reference/random/generator.html)、[permutation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html)。
