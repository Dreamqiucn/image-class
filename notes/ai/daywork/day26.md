# Day 26：广播与 axis 按轴统计

布置日期：2026-10-24。预计约 60 分钟，接续 Day 25。使用已有 NumPy，不安装依赖；核心练习由用户自行编写。

## 目标

理解广播的形状匹配规则，区分整体统计、axis=0 和 axis=1，使用 sum、mean、min、max，并通过 keepdims 保留轴以便继续广播计算。

## 1. 广播：形状不同也可以逐元素计算

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)
# [[11 22 33]
#  [14 25 36]]
```

a.shape=(2,3)，b.shape=(3,)。从右往左对齐，缺少的前导轴按长度 1 处理，相当于对比 (2,3) 和 (1,3)；每个对应轴的长度相同或有一方为 1，即可兼容。这里概念上把同一个一维数组用于两行，不要求先实际复制数组。

```python
c = np.array([[10], [20]]) # shape=(2,1)
print(a * c)
# [[10 20 30]
#  [80 100 120]]
```

此时每行乘各自的数。(2,3) 与 (2,) 不能广播，因为最右轴长度 3 与 2 不相同、也没有 1；两行数据要各配一个数，可以把两个数组织成 (2,1)。广播同样适用于 +、-、*、/。

## 2. 四个统计方法

```python
print(a.sum())  # 21，总和
print(a.mean()) # 3.5，平均值
print(a.min())  # 1，最小值
print(a.max())  # 6，最大值
```

这些是方法，需要括号。不指定 axis 时，这四个方法默认对整个数组的所有元素统计。np.sum(a) 与 a.sum() 都可以，今天统一使用数组方法即可。

## 3. axis 指定沿哪个轴汇总

对于当前二维数组，轴 0 是行轴，轴 1 是列轴。统计时指定哪个轴，就把沿着这个轴变化的元素合并起来，默认在结果中去掉这个轴。

```python
print(a.sum(axis=0)) # [5 7 9]，每列一个总和
print(a.sum(axis=1)) # [6 15]，每行一个总和
```

axis=0 时，分别计算 1+4、2+5、3+6，把两行合并，留下三列；shape 从 (2,3) 变成 (3,)。axis=1 时，分别计算 1+2+3、4+5+6，把每行的三个列元素合并，留下两行的结果；shape 变成 (2,)。

不要将“轴 0 对应行轴”误读为“axis=0 得到每行总和”。轴编号指定被汇总的方向，不是结果被保留的方向。二维时 axis=0 得到每列统计，axis=1 得到每行统计；三维时仍按指定轴合并，不能套用固定的行列口号。

```python
print(a.mean(axis=0)) # [2.5 3.5 4.5]
print(a.mean(axis=1)) # [2. 5.]
print(a.min(axis=0))  # [1 2 3]
print(a.max(axis=1))  # [3 6]
```

## 4. keepdims：保留被汇总轴的位置

```python
row_mean = a.mean(axis=1, keepdims=True)
print(row_mean)
# [[2.]
#  [5.]]
print(row_mean.shape) # (2,1)
print(a - row_mean)
# [[-1. 0. 1.]
#  [-1. 0. 1.]]
```

keepdims=True 让被汇总的轴长度变为 1，而非删去该轴；所以每行平均值的 shape 从 (2,) 变为 (2,1)，可以广播回 (2,3)，让每行减去各自的平均值。a 没有因这个表达式被原地修改。

## 自己实践

继续在 scripts/numpy_basics.py 新增函数，或选择新文件。建议使用三行四列的数组 np.arange(1,13).reshape(3,4)：

1. 创建一个长度为 4 的一维数组，加到原数组上；再创建 (3,1) 的数组与原数组相乘，观察两种广播方向。
2. 计算原数组整体的 sum、mean、min、max。
3. 分别按 axis=0、axis=1 求和及求平均，打印结果与 shape；另选一个轴求 min 和 max，理解它们使用相同的 axis 规则。
4. 使用 mean(axis=1,keepdims=True) 求每行平均值，让原数组减去每行平均值，观察结果；可查看结果的每行平均值是否接近 0。浮点计算时不强求所有任意数据恰好等于 0。

不要求固定函数名、输出排版或额外口头考试；若已能正确实现核心目标，不机械重复每个统计方法的所有组合。不整合扫描程序，不要求今天读真实图片。

## 记录约定

此文件只保存今天的任务，尚未完成。每日问答与成果等用户结束本日后统一整理到 records/day26-record.md，总进度不收录具体问答。未代写核心学习代码、安装依赖或操作 Git；不提前创建 Day 27 任务。

参考：[NumPy 广播](https://numpy.org/doc/stable/user/basics.broadcasting.html)、[sum 与 axis/keepdims](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)、[mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)、[min](https://numpy.org/doc/stable/reference/generated/numpy.min.html)、[max](https://numpy.org/doc/stable/reference/generated/numpy.max.html)。

## 收尾状态：2026-10-24

核心目标完成。用户自行编写 answer_day26，实现两个方向的广播、整体四种统计、按轴求和与平均、按轴最小/最大值、keepdims 行均值与逐行减均值。实际 Conda Python 运行结果全部正确，退出码 0，无报错。

接受合并广播表达式和当前输出方式，不要求额外 shape 打印或口头考试。详细问答和结果统一保存到 records/day26-record.md。下一学习日 Day 27，等待用户要求开始。未代改核心代码、环境或操作 Git。
