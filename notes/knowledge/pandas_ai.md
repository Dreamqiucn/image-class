# Pandas 知识点

整理范围：Day 29～34 已学内容，以及 Day 35 的 `size()`、`count()` 复盘。示例中的路径和角色 A/B 是练习数据，不代表正式数据集。Python 代码中的变量按文中顺序使用；每个主要例子都附输出。输出格式和字符串 dtype 可能因 Pandas 版本不同略有差异。

## 1. 导入与两种数据结构

```python
import pandas as pd

s = pd.Series([100, 200, 300], name="width")
print(s)
```

输出：

```text
0    100
1    200
2    300
Name: width, dtype: int64
```

`pd` 是 pandas 的别名。`Series` 是带索引的一维数据，可以先理解成一列；左边 0、1、2 是默认索引。

```python
df = pd.DataFrame([
    {"path": "A/a.jpg", "label": "A", "width": 100},
    {"path": "A/c.jpg", "label": "A", "width": 200},
    {"path": "B/b.jpg", "label": "B", "width": 300},
])
print(df)
```

输出：

```text
      path label  width
0  A/a.jpg     A    100
1  A/c.jpg     A    200
2  B/b.jpg     B    300
```

`DataFrame` 是二维表：一行可以代表一条样本，一列代表 path、label、width 等一个属性。示例中每个字典是一行，字典的键成为列名；`df` 是自己起的变量名。

## 2. 查看表格信息

```python
print(df.shape)
print(df.columns.tolist())
print(s.dtype)
```

输出：

```text
(3, 3)
['path', 'label', 'width']
int64
```

`df.shape` 是（行数，列数），显示在左侧的行索引不算数据列。`df.columns` 是列名，`.tolist()` 可以转成普通列表；`df.dtypes` 查看各列类型，`s.dtype` 查看 Series 的类型。这些都是属性，只有 `tolist()` 是方法，需要括号。

### head 查看前几行

```python
print(df.head(-1))
```

输出：

```text
      path label  width
0  A/a.jpg     A    100
1  A/c.jpg     A    200
```

`head(2)` 是前两行；`head(-1)` 是除了最后一行的其余行。`head()` 默认前五行，不会删除原表中的行。

## 3. 读取与保存 CSV

```python
csv_text = df.to_csv(index=False)
print(csv_text, end="")
```

输出：

```text
path,label,width
A/a.jpg,A,100
A/c.jpg,A,200
B/b.jpg,B,300
```

上面没有给 to_csv 文件路径，所以返回 CSV 文本，便于看效果。实际写文件可以使用 `df.to_csv(文件路径, index=False, encoding="utf-8-sig")`；传入文件路径后默认返回 None，不会自动在控制台显示内容。

- `index=False`：不额外保存左侧的行索引。
- `encoding="utf-8-sig"`：便于部分 Windows 表格软件识别中文。
- 默认覆盖已有的同名目标文件，输入文件和输出文件要分开。

读取使用 `pd.read_csv(文件路径, encoding="utf-8-sig")`，返回 DataFrame；相对路径从运行时工作目录查找。先打印 `df.columns`，确认列名大小写与实际文件一致，例如 `path` 与 `Path` 不相同。

## 4. 选择列：Series 和 DataFrame

```python
print(type(df["label"]).__name__)
print(type(df[["label"]]).__name__)
print(df[["path", "label"]])
```

输出：

```text
Series
DataFrame
      path label
0  A/a.jpg     A
1  A/c.jpg     A
2  B/b.jpg     B
```

`df["label"]` 选择一列，得到 Series；`df[["label"]]` 传入一个列名列表，保留二维表。双层方括号里，内层是列名列表，外层执行选择。

## 5. loc 和 iloc：按标签或位置选择

先创建一个副本，给行设置不同于位置的索引标签：

```python
example = df.copy()
example.index = [10, 20, 30]
print(example)
```

输出：

```text
       path label  width
10  A/a.jpg     A    100
20  A/c.jpg     A    200
30  B/b.jpg     B    300
```

```python
print(example.loc[20, "width"])
print(example.iloc[1, 2])
```

输出：

```text
200
200
```

| 写法 | 根据什么选择 |
| --- | --- |
| `loc[20, "width"]` | 行索引标签 20，列名 width |
| `iloc[1, 2]` | 第二行、第三列的位置，位置从 0 开始 |

`loc[20]` 中的 20 是标签，不是第 21 行；`iloc[1]` 的 1 是位置。单行索引通常得到 Series，`iloc[0:1]` 这样的切片保留 DataFrame。

对于这个有序且标签唯一的索引，`example.loc[10:20]` 包含标签 10 和 20；`example.iloc[0:1]` 只包含位置 0，不包含终点位置 1。

## 6. 条件筛选

```python
print(df[(df["label"] == "A") & (df["width"] >= 200)])
```

输出：

```text
      path label  width
1  A/c.jpg     A    200
```

比较先得到每行的 True/False，把结果放进 `df[...]` 就保留 True 的行。组合条件用 `&`（同时满足）、`|`（满足一个），各个比较条件单独加括号。筛选后默认保留原来的行索引。

## 7. 缺失值与重复记录

```python
sample = pd.DataFrame({
    "path": ["A/a.jpg", "A/a.jpg", "B/b.jpg", "C/c.jpg"],
    "label": ["A", "A", "B", None],
    "width": [100, 100, None, 400],
})
print(sample.isna().sum())
```

输出：

```text
path     0
label    1
width    1
dtype: int64
```

`isna()` 判断是否缺失，`.sum()` 可以统计 True 的数量。自己手写的空字符串 `""` 默认不算缺失；读取 CSV 时，空字段是否被识别为缺失还受读取参数影响。

```python
valid = sample.dropna(subset=["path", "label"])
clean = valid.drop_duplicates(subset=["path"])
print("原始行数：", len(sample))
print("去掉缺失后：", len(valid))
print("去重后：", len(clean))
```

输出：

```text
原始行数： 4
去掉缺失后： 3
去重后： 2
```

`subset` 指明要检查的列。这里 B 的 width 缺失，但 path、label 完整，所以保留；重复路径默认保留第一次出现的行。要接收返回值才能继续处理，默认不会直接修改原表。

可以用 `valid.duplicated(subset=["path"])` 查看哪些行被标为后续重复。路径去重只比较路径字符串，不能证明图片内容不同；同一路径对应不同标签时，应先检查冲突。

## 8. 统计数量与占比

```python
print(df["label"].value_counts())
print(df["label"].value_counts(normalize=True).round(2))
```

输出：

```text
label
A    2
B    1
Name: count, dtype: int64
label
A    0.67
B    0.33
Name: proportion, dtype: float64
```

`value_counts()` 统计各值出现次数，默认按数量从多到少排列；`normalize=True` 计算占比，`.round(2)` 将数值舍入到小数点后两位。默认不统计缺失值，占比的分母也是参与统计的非缺失值数量。

### 分组统计：groupby

```python
print(df.groupby("label").size())
print(df.groupby("label")["width"].mean())
```

输出：

```text
label
A    2
B    1
dtype: int64
label
A    150.0
B    300.0
Name: width, dtype: float64
```

`groupby("label")` 按标签分组，`size()` 数每组行数，`["width"].mean()` 求每组有效宽度的平均值。groupby 默认按标签排序，value_counts 默认按数量排序，所以输出顺序可能不同。

如果 width 缺失：`groupby("label").size()` 仍数该行；`groupby("label")["width"].count()` 数该列非缺失值；width 的 `mean()` 默认跳过缺失值。一列缺失不会自动删除其他列的值。

## 9. map 与 merge：匹配类别编号

### map：用字典匹配

```python
class_to_idx = {"A": 0}
mapped = df.copy()
mapped["class_id"] = mapped["label"].map(class_to_idx)
print(mapped)
```

输出：

```text
      path label  width  class_id
0  A/a.jpg     A    100       0.0
1  A/c.jpg     A    200       0.0
2  B/b.jpg     B    300       NaN
```

map 根据 label 查字典。B 没有匹配到，class_id 为缺失值；用 `mapped[mapped["class_id"].isna()]` 可以找出这些行。可能是标签没在字典里，也可能输入或映射值本身缺失，应结合原数据检查。

```python
class_to_idx["B"] = 1
mapped["class_id"] = mapped["label"].map(class_to_idx)
print(mapped)
```

输出：

```text
      path label  width  class_id
0  A/a.jpg     A    100         0
1  A/c.jpg     A    200         0
2  B/b.jpg     B    300         1
```

给字典增加 B 后重新 map，会重新赋值整列；因为原字典仍有 A，所以 A 仍能匹配。写 `class_to_idx = {"B": 1}` 则会换成一个新字典，原来的 A 映射不再在新字典里。

### merge：按公共列连接两张表

```python
classes = pd.DataFrame({"label": ["A"], "class_id": [0]})
joined = df.merge(classes, on="label", how="left")
print(joined)
```

输出：

```text
      path label  width  class_id
0  A/a.jpg     A    100       0.0
1  A/c.jpg     A    200       0.0
2  B/b.jpg     B    300       NaN
```

`on="label"` 根据两表的 label 列匹配；`how="left"` 保留左表的样本，B 没匹配到编号因此为缺失值。右表同一标签如果有多行，一条左表记录可能匹配出多行，使用前应检查映射是否符合预期。

如果两表有相同名称的非连接列，Pandas 默认用 `_x`、`_y` 区分左右表。它们不一定代表同一个含义，需要看原表的列。

## 10. reset_index 与保存统计表

```python
counts = df["label"].value_counts()
stats = counts.reset_index(name="count")
print(stats)
```

输出：

```text
  label  count
0     A      2
1     B      1
```

原来的 A/B 是 counts 的索引；`reset_index()` 默认把旧索引变为一列，并新建 0、1、2……行索引。这里 `name="count"` 是给 **Series.reset_index** 转出来的值列命名；`drop=True` 则丢弃旧索引。

现在 stats 是二维 DataFrame，可以用 `stats.to_csv(路径, index=False, encoding="utf-8-sig")` 保存；一张包含两列的 DataFrame 不能直接赋给另一张表的单个列。

## 11. 快速查阅

| 想做什么 | 写法 |
| --- | --- |
| 从列表建一列 | `pd.Series([...])` |
| 从字典列表建表 | `pd.DataFrame(rows)` |
| 查看行列数、列名 | `df.shape`、`df.columns` |
| 读取、保存 CSV | `pd.read_csv(path)`、`df.to_csv(path, index=False)` |
| 选一列 / 保留一列表格 | `df["label"]` / `df[["label"]]` |
| 按行标签和列名取值 | `df.loc[标签, "列名"]` |
| 按行列位置取值 | `df.iloc[行位置, 列位置]` |
| 按条件选行 | `df[df["label"] == "A"]` |
| 检查缺失 / 必要列去缺失 | `df.isna().sum()` / `df.dropna(subset=["path", "label"])` |
| 查重复 / 按路径去重 | `df.duplicated(subset=["path"])` / `df.drop_duplicates(subset=["path"])` |
| 值的数量 / 比例 | `df["label"].value_counts()` / `value_counts(normalize=True)` |
| 按标签数行 / 求平均 | `df.groupby("label").size()` / `df.groupby("label")["width"].mean()` |
| 用字典映射 | `df["label"].map(class_to_idx)` |
| 两张表按标签左连接 | `df.merge(classes, on="label", how="left")` |
| 索引变数据列 | `series.reset_index(name="count")` |

参考：[Pandas 入门](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)、[数据选择](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)、[to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)、[Series.map](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)、[DataFrame.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)。
