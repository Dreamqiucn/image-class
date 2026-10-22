# Day 22：NumPy 数组入门

布置日期：2026-10-22。预计约 60 分钟，开始 NumPy，不安排 Python 复习。NumPy 由用户手动安装；助手不安装或修改环境配置。

## 今天的目标

能创建一维、二维 ndarray，读懂 shape、ndim、size、dtype，并知道列表和数组的简单区别。

## 准备

在现有 image-class-conda 环境中手动安装 NumPy，例如在终端运行 `conda install -n image-class-conda numpy`。安装完成后，在选用该环境的 Python 中检查 `import numpy as np` 和 `print(np.__version__)`。不需要另建环境。

## 教程

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
print(b.shape)  # (2, 3)：两个轴的长度分别为 2 和 3
print(b.ndim)   # 2：二维
print(b.size)   # 6：一共六个元素
print(b.dtype)  # 元素的数据类型；看实际输出
```

`np` 是 NumPy 的常用别名，`np.array(...)` 把列表等数据转换为数组。普通数值数组的元素使用共同的数据类型。一维数组 a 的 shape 为 `(3,)`，二维数组 b 的 shape 为 `(2, 3)`；ndim 是轴的个数，size 是所有轴长度的乘积。这四项都是属性，访问时不加括号。

```python
print([1, 2, 3] * 2)             # 列表重复两遍
print(np.array([1, 2, 3]) * 2)   # 每个元素乘以 2
```

今天只用这个例子认识数组与列表的差别，逐元素计算在后面的任务中展开。

## 自己实践

自己创建 `scripts/numpy_basics.py`，不要命名为 numpy.py，以免遮住导入的库。

1. 创建一个四个元素的一维数组，以及一个两行三列的二维数组，数字自行选择。
2. 先预测，再打印它们的 shape、ndim、size、dtype。
3. 另建一个包含小数的数组，观察 dtype；再尝试在 np.array 中指定 `dtype=np.float32`，观察变化。
4. 对列表和数组分别执行乘以 2，观察结果。

不需要整合旧扫描脚本或准备正式角色数据集。索引、切片、reshape 和广播在后续学习日再学。

## 完成标准

上述小练习可以运行，并能解释二维数组中 shape、ndim、size 各自表示什么，以及为什么访问这些属性不写括号。无需特定输出格式或额外工程化。

本文件只保存当日任务；每日问答和进度等用户确认当日结束后统一记录，不提前标记完成。不进行 Git 暂存、提交或推送。

参考：[NumPy 官方入门](https://numpy.org/doc/stable/user/absolute_beginners.html)、[安装说明](https://numpy.org/install/)。

## 收尾状态：2026-10-22

按核心数组练习完成本日。用户已编写一维数组及三行四列 float32 数组；使用现有 Conda Python 实际运行两段函数，分别得到 `(4,) 1 4 int64` 和 `(3, 4) 2 12 float32`，无报错。NumPy 2.5.4 可用，由用户手动安装，助手未改环境。

接受用户自主选择的二维形状，不要求补做所有教程变体。列表与数组乘法比较、默认小数 dtype 未在脚本中实践，不记成已完成；维度与行数的区别已讲解，未独立复答。详细过程统一保存到 records/day22-record.md；后续 Day 23 按用户要求开始，不提前创建任务。
