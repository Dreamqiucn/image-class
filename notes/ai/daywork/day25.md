# Day 25：逐元素计算、类型转换和像素缩放

布置日期：2026-10-23。预计约 60 分钟，接续 Day 24。只使用已有 NumPy，不安装依赖；练习代码由用户自己编写。

## 目标

使用数组进行逐元素计算，通过 astype 转换 dtype，并将 8 位像素从 0～255 缩放到 0～1。今天使用手写模拟像素数组，不要求读取真实图片或整合扫描程序。

## 1. 逐元素计算

```python
import numpy as np

a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
print(a + 10) # [12 14 16]
print(a * 2)  # [4 8 12]
print(a / 2)  # [1. 2. 3.]
print(a + b)  # [3 6 9]
print(a * b)  # [2 8 18]
```

数组与单个数字运算时，数字作用于每个元素；两个相同形状的数组用 +、-、*、/ 运算时，对应位置分别计算。今天只用相同形状，广播规则留到 Day 26。

a+10 返回计算结果，不会直接修改 a；需要保留结果时赋给变量，例如 c=a+10。

## 2. astype：转换元素类型

```python
a = np.array([1, 2, 3], dtype=np.int32)
b = a.astype(np.float32)
print(a.dtype) # int32
print(b.dtype) # float32
print(b)       # [1. 2. 3.]
```

astype 返回转换结果，a 的 dtype 不会因为单独调用 a.astype(...) 就改变；需要使用返回值或重新赋值。float32 是 32 位浮点类型，适合后续许多数值处理场景。它与整数数组不同，可以保存小数。

## 3. 8 位像素值与缩放

uint8 是无符号 8 位整数，范围为 0～255。今天模拟常见的 8 位灰度像素：0 表示黑，255 表示白，中间值表示不同亮度；并非所有图片都采用这个范围。

```python
pixels = np.array([0, 64, 128, 255], dtype=np.uint8)
scaled = pixels.astype(np.float32) / 255.0
print(scaled)
# 约 [0. 0.2509804 0.5019608 1.]
print(pixels.dtype) # uint8
print(scaled.dtype) # float32（当前环境）
```

对每个值执行 x/255，原来的 0、255 分别变成 0、1，64 约为 0.251，128 约为 0.502。形状和元素个数不变，数值与类型发生变化。这里不是把值变成只有 0 和 1，也不是改变图片尺寸。不要把这个结果转回整数，否则很多 0～1 之间的小数会变成 0。

使用 / 进行普通除法；// 会做向下取整的整除，不适合保留这些小数。这里明确 astype 是为了得到 float32 工作数据；直接使用整数数组 /255.0 也会得到浮点结果，不能误解成“不先转换就一定做整除”。

## 4. 整数范围会影响运算

```python
x = np.array([250], dtype=np.uint8)
print(x + 10)                    # [4]，超出 uint8 范围后发生回绕
print(x.astype(np.float32) + 10) # [260.]
```

需要在运算前转换类型。把 (x+10) 的结果再转换为 float32，已经丢失的正确值不会恢复。这里转成浮点数也不会自动把 260 限制为 255，不把类型转换当作范围裁剪。

## 自己实践

继续在 scripts/numpy_basics.py 新增函数，或自选新文件：

1. 自选两个形状相同的小数组，计算 a+10、a*2、a+b、a*b，观察对应位置的结果。
2. 创建整数数组，使用 astype(np.float32)，打印转换前后的数据与 dtype。
3. 创建一个两行三列的 uint8 模拟像素数组，值在 0～255 之间，并包含 0、255 和中间值；转换为 float32 后除以 255.0，打印前后数据、dtype 与 shape，确认形状不变。
4. 观察 uint8 的 [250]+10 与先转 float32 再加 10 的结果差异，理解为什么转换时机有影响。

不要求特定函数名、输出排版、额外测试文件或口头考试。不处理真实图片，不提前做按轴统计或广播教程。

## 记录规则

本文件只保存当日任务，尚未完成。每日成果与问答等本日结束后统一更新到 records/day25-record.md；总进度不收录具体问答。未完成的内容不提前记为已实践。不进行 Git 暂存、提交或推送。

参考：[NumPy 基础运算](https://numpy.org/doc/stable/user/quickstart.html#basic-operations)、[astype](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html)、[数据类型](https://numpy.org/doc/stable/user/basics.types.html)。

## 收尾状态：2026-10-23

按核心目标完成。用户自行编写 answer_12 至 answer_15，实际 Conda Python 运行确认数组乘法及广播、int64 到 float32 转换、(2,3) uint8 模拟像素除以 255.0 的缩放、两种类型加 10 的范围对比均正确，退出码 0。

当前未练习加法示例，模拟像素只用 1 至 6、未包含 0 与 255 端点；这些不记为已实践，接受当前核心范围，不强制补做所有例子。详细过程统一保存到 records/day25-record.md。下一学习日 Day 26 学习广播与 axis 统计，等待用户要求开始。未代改核心代码或环境，未操作 Git。
