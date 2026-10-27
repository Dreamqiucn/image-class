# NumPy 知识点

整理范围：Day 22～28 已学内容。代码块标为 Python 的是代码，标为 text 的是打印结果。示例先执行下面的导入；不同小节中的 a 等变量会重新赋值。

## 1. 导入

```python
import numpy as np
```

np 是给 NumPy 起的常用别名。数组的类型叫 ndarray。

## 2. 创建数组

### array：自己指定内容

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
```

输出：

```text
[[1 2 3]
 [4 5 6]]
```

Python 列表在代码里需要逗号，NumPy 数组打印时通常没有逗号，不要直接把上面的输出当作 Python 列表代码。

### arange：按间隔自动生成，得到一维数组

格式：`np.arange(起点, 终点, 步长)`，不包含终点。只填一个参数时，从 0 开始；默认步长为 1。

```python
print(np.arange(6))         # [0 1 2 3 4 5]
print(np.arange(1, 7))      # [1 2 3 4 5 6]，不包含 7
print(np.arange(1, 10, 2))  # [1 3 5 7 9]
```

### zeros 和 ones：全是 0、全是 1

```python
print(np.zeros((2, 3)))  # 两行三列，默认浮点数
print(np.ones((2, 3), dtype=np.int32))  # 两行三列的整数 1
```

`(2, 3)` 是传入的 shape 元组。也可以用 `(2, 3, 4)` 创建三维数组。

## 3. 数组属性与形状

```python
a = np.arange(24).reshape(2, 3, 4)
print(a.shape)  # (2, 3, 4)：各轴的长度
print(a.ndim)   # 3：有几个轴
print(a.size)   # 24：总元素数，2×3×4
print(a.dtype)  # 元素的数据类型，看实际输出
print(len(a))   # 2：第一轴的长度，不是总元素数
```

这些属性不加括号；len 是函数，要加括号。这里的 len 用法针对有至少一个轴的数组。

维度数不是行数。三行四列的数组仍是二维，因为需要行、列两个下标来定位元素。

| shape | 含义 |
| --- | --- |
| `(4,)` | 一维，四个元素；末尾逗号表示单元素元组 |
| `(1, 4)` | 二维，一行四列 |
| `(4, 1)` | 二维，四行一列 |
| `(2, 3, 4)` | 三个轴，长度分别为 2、3、4 |

二维数组的高度、宽度可以这样取：

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
height = a.shape[0]  # 2：行数
width = a.shape[1]   # 3：列数
```

轴编号从 0 开始。三维的含义由数据约定决定：普通例子可以按“表、行、列”理解；RGB 图片数组按“高、宽、通道”理解，不要混用。

## 4. 索引与切片

### 索引：按位置取

```python
a = np.arange(1, 13).reshape(3, 4)
print(a[0, 1])    # 2：第一行第二列
print(a[-1, -1])  # 12：最后一行最后一列
print(a[0])       # [1 2 3 4]：第一行
print(a[:, 0])    # [1 5 9]：第一列
```

下标从 0 开始。没有写出来的后续轴默认全部取，不要求所有轴都写下标。

对于上面的二维 a，`a[0]`、`a[0,]`、`a[0, :]` 取到同样的第一行；这里是在描述结果相同，不是使用赋值号连接它们。

### 切片：取一个范围

每个轴可以写 `开始:结束:步长`，用英文冒号；多个轴之间用逗号分隔。

切片包含开始，不包含结束。省略开始表示从开头取，省略结束表示取到末尾；省略步长默认为 1。

```python
x = np.array([10, 20, 30, 40, 50])
print(x[1:4])     # [20 30 40]
print(x[::2])     # [10 30 50]
print(a[:2, 1:3]) # [[2 3], [6 7]]，前两行、第 2～3 列
print(a[2::2])    # 从行下标 2 开始，行下标每次增加 2
```

### 整数索引去掉轴，切片保留轴

```python
print(a[0].shape)     # (4,)
print(a[0:1].shape)   # (1, 4)
print(a[:, 0].shape)  # (3,)
print(a[:, 0:1].shape) # (3, 1)
```

`0:1` 只包含下标 0，不包含下标 1；它选择的行数虽然只有 1，但仍保留行轴。不能简单记成“只要用了冒号就是二维”。

三维 RGB 示例：

```python
image = np.arange(60).reshape(4, 5, 3)
print(image[:, :, 0].shape)    # (4, 5)：取第一个通道，去掉通道轴
print(image[:, :, 0:1].shape)  # (4, 5, 1)：切一个通道，保留通道轴
print(image[0, 0].shape)       # (3,)：一个像素的三个通道值
```

## 5. 求和、平均值、最大值和最小值

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.sum())   # 21
print(a.mean())  # 3.5
print(a.max())   # 6
print(a.min())   # 1
```

这四个都是方法，要加括号。不指定 axis，默认统计全部元素。mean 求平均，不是只求和。

### axis：指定沿哪个轴汇总

基本规则：axis 指定被汇总的轴，默认在结果中删掉这个轴，其他轴按原顺序保留。

```python
print(a.sum(axis=0))   # [5 7 9]：1+4、2+5、3+6
print(a.sum(axis=1))   # [6 15]：1+2+3、4+5+6
print(a.mean(axis=0))  # [2.5 3.5 4.5]：每列平均值
print(a.mean(axis=1))  # [2. 5.]：每行平均值
```

二维时，axis=0 汇总行轴，留下每列的结果；axis=1 汇总列轴，留下每行的结果。默认得到一维结果，不是自动变成二维的“一行”。

对二维数组，`a.mean(axis=(0, 1))` 与 `a.mean()` 都汇总全部元素。三维数组再用 `(0, 1)` 时，还会保留轴 2，含义不同。

三维数组按 shape 判断，不用猜括号层数。例如原 shape 为 `(2, 3, 4)`：

| 操作 | 默认结果 shape | 加 keepdims=True 后 |
| --- | --- | --- |
| `mean(axis=0)` | `(3, 4)` | `(1, 3, 4)` |
| `mean(axis=1)` | `(2, 4)` | `(2, 1, 4)` |
| `mean(axis=2)` | `(2, 3)` | `(2, 3, 1)` |
| `mean(axis=(0, 1))` | `(4,)` | `(1, 1, 4)` |
| `mean(axis=(0, 2))` | `(3,)` | `(1, 3, 1)` |

sum、min、max 也遵循这样的 axis/keepdims 形状规则。

### keepdims=True：保留轴的位置，长度改成 1

它不增加数据量，也不是把每个值变成列表；它保留被汇总轴的位置，方便之后广播。

```python
row_mean = a.mean(axis=1, keepdims=True)
print(row_mean)        # [[2.], [5.]]
print(row_mean.shape)  # (2, 1)
print(a - row_mean)    # [[-1. 0. 1.], [-1. 0. 1.]]
```

图片 shape 为 `(高, 宽, 3)` 时，`mean(axis=(0, 1))` 汇总高和宽，留下三个通道均值，shape 为 `(3,)`；加 keepdims 后为 `(1, 1, 3)`。

对于原 shape 为 `(2, 3, 4)` 的数组，`mean(axis=(0, 1), keepdims=True)` 得到 `(1, 1, 4)`，最内层有四个数，不固定是三个。

## 6. reshape：改变形状

默认按原来的逐行顺序重新分组，新旧元素总数必须相同。

```python
x = np.arange(1, 13)
a = x.reshape(3, 4)
b = x.reshape(2, 6)
print(a.shape, b.shape)  # (3, 4) (2, 6)
print(x.shape)          # (12,)，原变量的形状没有被直接修改
```

12 个元素不能 reshape 为 `(3, 5)`，因为需要 15 个元素，会报 ValueError。

### -1：让 NumPy 推算一个轴的长度

```python
print(x.reshape(3, -1).shape)  # (3, 4)：12÷3=4
print(x.reshape(4, -1).shape)  # (4, 3)
print(a.reshape(-1).shape)     # (12,)：变为一维
print(a.reshape(1, -1).shape)  # (1, 12)：仍然是二维
```

这里的 -1 是自动推算，不是倒数第一个；一次最多用一个 -1，已知轴长度也要能与元素总数匹配。

## 7. 转置：交换轴顺序

### 二维 .T：交换行与列

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)
```

输出：

```text
[[1 4]
 [2 5]
 [3 6]]
```

`a.T` 是属性，不加括号；对于二维数组，它等价于 `a.transpose(1, 0)`。原位置 `[i, j]` 对应转置后的 `[j, i]`。

同样变为 `(3, 2)`，reshape 的排列却不同：

```python
print(a.reshape(3, 2))  # [[1 2], [3 4], [5 6]]
```

shape 一样不代表元素位置一样。一维数组的 `.T` 仍是一维，想变成二维列形状可以用 `reshape(-1, 1)`。

### 三维 .T 与指定顺序

```python
c = np.arange(24).reshape(2, 3, 4)
print(c.T.shape)  # (4, 3, 2)，等价于 transpose(2, 1, 0)
d = c.transpose(2, 0, 1)
print(d.shape)   # (4, 2, 3)
print(c[1, 2, 3] == d[3, 1, 2])  # True
```

`.T` 反转所有轴。`transpose(2, 0, 1)` 表示按“原轴 2、原轴 0、原轴 1”排列，每个原轴恰好出现一次；参数是轴编号，不是轴长度。

RGB 图片原本按 `(高, 宽, 通道)` 排列时，`transpose(2, 0, 1)` 变为 `(通道, 高, 宽)`。

## 8. 数组运算与列表运算

```python
a = np.array([1, 2, 3])
print(a + 10)  # [11 12 13]
print(a * 2)   # [2 4 6]：每个元素乘以 2
print(a ** 2)  # [1 4 9]：每个元素平方
print(a / 2)   # [0.5 1. 1.5]
print([1, 2, 3] * 2)  # [1, 2, 3, 1, 2, 3]：列表重复
```

两个兼容形状的 ndarray 使用 `+ - * /` 时，对应位置计算；这里的 `*` 是逐元素乘法。

```python
b = np.array([10, 20, 30])
print(a * b)  # [10 40 90]
c = a * 2
print(a)      # [1 2 3]：结果存到 c，a 没变
```

如果想让变量 a 使用计算结果，写 `a = a * 2`；`a *= 2` 则会直接修改数组数据。`/` 保留除法的小数结果，`//` 是向下取整的整除。

## 9. 广播：不同形状如何配合

把 shape 从右往左对齐，各个对应轴必须长度相同，或者其中一方长度为 1；缺少的前导轴按 1 处理。

| 两个 shape | 能否计算 | 结果 shape |
| --- | --- | --- |
| `(2, 3)` 与 `(2, 3)` | 可以，对应位置计算 | `(2, 3)` |
| `(2, 3)` 与 `(3,)` | 可以，一维数组用于每行 | `(2, 3)` |
| `(2, 3)` 与 `(1, 3)` | 可以，一行用于每行 | `(2, 3)` |
| `(2, 3)` 与 `(2, 1)` | 可以，每行用一个数 | `(2, 3)` |
| `(2, 3)` 与 `(2,)` | 不可以，最右轴 3 与 2 不兼容 | — |

不要求其中一个只有一行；行数、列数也不一定都相同。

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a + np.array([10, 20, 30]))
# [[11 22 33], [14 25 36]]
print(a * np.array([[10], [20]]))
# [[10 20 30], [80 100 120]]
```

广播可以按概念理解成把长度为 1 的方向展开使用，不要求自己先复制出多行数据。

## 10. dtype 转换与像素缩放

### astype：转换元素类型

```python
a = np.array([1, 2, 3], dtype=np.int32)
b = a.astype(np.float32)
print(a.dtype)  # int32
print(b.dtype)  # float32
print(b)        # [1. 2. 3.]
```

单独调用 astype 不会直接改变原变量 a 的类型，需要接收结果。常用类型：int32/int64 是整数，float32/float64 是浮点数，uint8 是 0～255 的无符号 8 位整数。

### uint8 的运算可能超出范围

```python
x = np.array([250], dtype=np.uint8)
print(x + 10)                    # [4]：数组运算超出范围后回绕
print(x.astype(np.float32) + 10) # [260.]：运算前先转换
```

先算出错误值再转浮点数，不能恢复正确结果；类型转换也不会自动把结果限制在 0～255。

### 常见 8 位像素除以 255.0

```python
pixels = np.array([0, 128, 255], dtype=np.uint8)
scaled = pixels.astype(np.float32) / 255.0
print(scaled)  # 约 [0. 0.5019608 1.]
print(pixels.dtype, scaled.dtype)  # uint8 float32（当前环境）
```

形状和元素数量不变，数值缩放到 0～1。128/255 约为 0.502，不精确等于 1/2；不要转回整数，否则很多小数会变成 0。

这里针对 8 位 0～255 数据，不是所有图片都属于这个范围。真实图片可能没有纯黑、纯白像素，所以缩放后的最小值和最大值不一定恰好为 0、1。

整数数组直接 `/ 255.0` 也会得到浮点数；提前 astype 是明确选择 float32，不是说不转换就一定做整除。

## 11. 布尔筛选

```python
a = np.arange(1, 13).reshape(3, 4)
mask = a > 6
print(mask.shape)  # (3, 4)：比较产生同形状的布尔数组
print(a[mask])     # [7 8 9 10 11 12]
print(a[(a >= 4) & (a <= 9)])  # [4 5 6 7 8 9]
print(a[(a < 3) | (a > 10)])  # [1 2 11 12]
```

完整同形状的布尔掩码选取 True 对应的元素，结果是一维。数组条件组合用 `&`（同时）、`|`（至少一个）、`~`（取反），每个比较条件加括号，不用 and/or 组合这些布尔数组。

## 12. np.append：追加元素与多行

### 一维追加

```python
a = np.array([1, 2, 3])
a = np.append(a, 4)
print(a)  # [1 2 3 4]
a = np.append(a, [5, 6])
print(a)  # [1 2 3 4 5 6]
```

np.append 返回新数组，不会原地追加，必须接收返回值。

### 二维追加多行

```python
a = np.array([[1, 2, 3]])
a = np.append(a, [[4, 5, 6], [7, 8, 9]], axis=0)
print(a.shape)  # (3, 3)
print(a)
```

输出：

```text
(3, 3)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

二维 axis=0 增加行，列数必须相同；axis=1 增加列，行数必须相同，追加数据的维数也要匹配。

```python
print(np.append(a, [[10], [11], [12]], axis=1).shape)  # (3, 4)
```

一维 `[1, 2, 3]` 要先变成二维，例如 `reshape(1, 3)`，才能这样追加多行。省略 axis 时，np.append 默认把数据展平后追加，返回一维。

## 13. 视图与副本

基本切片得到的数组与原数组共享数据，修改切片元素会影响原数组。

```python
a = np.array([1, 2, 3, 4])
b = a[1:3]
b[0] = 99
print(a)  # [1 99 3 4]
```

想独立修改，用 copy：

```python
a = np.array([1, 2, 3, 4])
b = a[1:3].copy()
b[0] = 99
print(a)  # [1 2 3 4]
```

`b = a` 只是让两个变量指向同一个数组，不会复制数据。reshape、转置的结果也可能共享数据，不要默认它们都是独立副本；普通布尔筛选得到的数组则是副本。

## 14. 快速查阅

| 想做什么 | 写法 |
| --- | --- |
| 创建 1～12 的一维数组 | `np.arange(1, 13)` |
| 看形状、维度、总数、类型 | `a.shape`、`a.ndim`、`a.size`、`a.dtype` |
| 二维数组的行数、列数 | `a.shape[0]`、`a.shape[1]` |
| 取第一行，保留为二维 | `a[0:1]` |
| 三维图片取第一个通道并去轴 | `image[:, :, 0]` |
| 三维图片取一个通道并保留轴 | `image[:, :, 0:1]` |
| 二维每行平均值，保留轴 | `a.mean(axis=1, keepdims=True)` |
| RGB 图片的三个通道均值 | `image.mean(axis=(0, 1))` |
| 改成三行，自动算列数 | `a.reshape(3, -1)`，元素数需兼容 |
| 变回一维 | `a.reshape(-1)` |
| 二维转置 | `a.T` |
| HWC 转为 CHW | `image.transpose(2, 0, 1)` |
| 每个元素乘 2、平方 | `a * 2`、`a ** 2` |
| 转 float32 | `a.astype(np.float32)` |
| 8 位像素缩放到 0～1 | `a.astype(np.float32) / 255.0` |
| 筛选大于 6 的元素 | `a[a > 6]` |
| 追加元素并保存新数组 | `a = np.append(a, 4)` |
| 独立复制数据 | `a.copy()` |

参考：[NumPy 入门](https://numpy.org/doc/stable/user/absolute_beginners.html)、[索引与切片](https://numpy.org/doc/stable/user/basics.indexing.html)、[reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)、[转置](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)、[广播](https://numpy.org/doc/stable/user/basics.broadcasting.html)、[数据类型](https://numpy.org/doc/stable/user/basics.types.html)、[追加数组](https://numpy.org/doc/stable/reference/generated/numpy.append.html)。
