# Day 32：类别统计、占比与 groupby

布置日期：2026-10-28。预计约 60 分钟。接续已按用户范围结束的 Day 31，不强制补写旧脚本。使用已有 Pandas，练习代码由用户自行编写。

## 目标

使用 value_counts 统计标签数量与占比，使用 groupby 分组求数量和数值列平均值。今天示例都包含输出，示例数据仅供练习，不决定正式角色名单。

## 示例表

```python
import pandas as pd

rows = [
    {"Path": "A/a.jpg", "Label": "A", "Width": 600},
    {"Path": "A/b.jpg", "Label": "A", "Width": 800},
    {"Path": "B/c.jpg", "Label": "B", "Width": 800},
    {"Path": "B/d.jpg", "Label": "B", "Width": 1000},
    {"Path": "B/e.jpg", "Label": "B", "Width": 1200},
]
df = pd.DataFrame(rows)
print(df)
```

输出：

```text
      Path Label  Width
0  A/a.jpg     A    600
1  A/b.jpg     A    800
2  B/c.jpg     B    800
3  B/d.jpg     B   1000
4  B/e.jpg     B   1200
```

Width 为自编的整数，只用于练习计算平均值；示例路径不要求真实存在。实际 1/output/samples.csv 已核对有 Path、Label 两列，通常没有 Width；如果使用真实 CSV，可以先只做标签数量和占比，数值列的分组平均用模拟表学习。

## 1. value_counts：统计出现次数

```python
print(df["Label"].value_counts())
```

输出：

```text
Label
B    3
A    2
Name: count, dtype: int64
```

先取 Label 这一列（Series），再数每个不同值出现多少次；结果也是 Series，左边的 A/B 是索引标签，右边是数量。默认按数量从多到少排序。value_counts 默认不计入缺失标签，处理含缺失数据时要注意分母。

## 2. normalize=True：计算占比

```python
print(df["Label"].value_counts(normalize=True))
```

输出：

```text
Label
B    0.6
A    0.4
Name: proportion, dtype: float64
```

B 有 3 条，占 3/5=0.6，也就是 60%；A 有 2 条，占 2/5=0.4，也就是 40%。在默认 dropna=True 的情况下，分母为参与统计的非缺失标签数量，示例里全部标签都有值，因此是 5。

## 3. groupby：按列分组再统计

```python
print(df.groupby("Label").size())
```

输出：

```text
Label
A    2
B    3
dtype: int64
```

groupby('Label') 先按标签分组，size() 再统计每组行数。此处 value_counts 默认按数量排序、groupby 默认按分组标签排序，所以顺序不同，数量一致。groupby 默认不单独统计缺失的分组标签。

## 4. 每个角色图片的模拟平均宽度

```python
print(df.groupby("Label")["Width"].mean())
```

输出：

```text
Label
A     700.0
B    1000.0
Name: Width, dtype: float64
```

A 组 (600+800)/2=700；B 组 (800+1000+1200)/3=1000。groupby 按 Label 分组，['Width'] 选出组内的 Width 列，mean() 求各组平均值。

Width 需要可用于数值计算。本例中的 Width 是手写整数，并不是 Day 29 里 x、y、z 那些文本占位，也不声称是实际图片宽度。

## 自己实践

在 scripts/pandas_basics.py 中新增函数，或自选新文件，自己构造包含 Path、Label、Width 的小表：至少两种模拟类别，至少五条记录，Width 使用自行选择的整数。

1. 用 value_counts() 统计类别数量，并用 normalize=True 算占比；打印结果。
2. 用 groupby('Label').size() 统计类别数量，与 value_counts 按类别对应比较，不要求显示顺序相同。
3. 用 groupby('Label')['Width'].mean() 求各类别平均宽度，并任选一组手算核对。
4. 看看标签占比的含义，说明每个类别数量除以参与统计的标签总数；不强制写导出或可视化。

也可以用现有 CSV 的实际 Label 列先完成数量和占比；因为当前表未必有 Width，平均宽度练习可另用自建数字表。不要自动采集或确定正式数据集。

## 记录与接续

今天不要求修改或覆盖现有 CSV、不提前绘图或训练。当天问答与成果在用户确认结束后统一保存到 records/day32-record.md，再更新总进度；此任务尚未完成。不代写核心代码，不 Git 暂存、提交或推送，不提前创建 Day 33 任务。

参考：[value_counts](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)、[groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)。

## 收尾状态：2026-10-28

用户自行实现 path 计数、width 有效值占比、按 label 的分组数量和平均宽度。实际 Conda Python 执行，分组数量为 3、2，平均宽度为 1.5、4.5，运行正常。缺失 width 在平均与宽度占比中被跳过，在分组行数中仍计入。

用户表示对不同列使用 value_counts 的方法相同，并明确结束本日；按现有练习范围完成，不要求增加同样方法的重复示例。用户代码未单独输出 label.value_counts 或标签占比，不记为已执行；三个相同路径为三条表记录，不当作三张不同图片。详细问答与结果见 records/day32-record.md。下一学习日 Day 33，等待用户要求开始。
