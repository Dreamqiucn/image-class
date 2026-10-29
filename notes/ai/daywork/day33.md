# Day 33：map、merge 与角色编号

布置日期：2026-10-29。预计约 60 分钟。接续 Day 32，使用已有 Pandas，核心练习由用户自己写。所有例子均附对应输出；显示空格或 dtype 可能因版本不同略有差异。

## 今天的目标

将样本表的角色名称映射成数字编号，分别理解 Series.map 和 DataFrame.merge，并找出没有匹配到编号的样本。今天的 A、B、C 是练习标签，不代表已确定正式作品或角色名单。

## 示例数据

```python
import pandas as pd

rows = [
    {"path": "A/a.jpg", "label": "A"},
    {"path": "B/b.jpg", "label": "B"},
    {"path": "A/c.jpg", "label": "A"},
    {"path": "C/d.jpg", "label": "C"},
]
df = pd.DataFrame(rows)
print(df)
```

输出：

```text
      path label
0  A/a.jpg     A
1  B/b.jpg     B
2  A/c.jpg     A
3  C/d.jpg     C
```

## 1. map：用字典查找每个标签

这个字典与 Day 19 的 class_to_idx 思路相同：键是角色名称，值是数字编号。

```python
class_to_idx = {"A": 0, "B": 1}
mapped = df.copy()
mapped["class_id"] = mapped["label"].map(class_to_idx)
print(mapped)
```

输出：

```text
      path label  class_id
0  A/a.jpg     A       0.0
1  B/b.jpg     B       1.0
2  A/c.jpg     A       0.0
3  C/d.jpg     C       NaN
```

map 根据每个 label 查字典：A→0，B→1；C 不在字典里，所以结果缺失。先 df.copy() 是为了让示例保留原表；给 mapped['class_id'] 赋值是在副本上添加一列。

有缺失值时，此处编号列显示为浮点形式 0.0、1.0、NaN；这些数字仍表示原来给定的 0、1 编号。不要把 NaN 当作一个自动分配的类别编号。

## 2. 找出没有匹配到编号的样本

```python
unmatched = mapped[mapped["class_id"].isna()]
print(unmatched)
```

输出：

```text
      path label  class_id
3  C/d.jpg     C       NaN
```

isna() 判断结果列是否缺失。此例中 C 的缺失来自字典没有 C；实际使用中，输入标签本身缺失、映射值本身缺失也可能导致结果缺失，应结合原始标签查看原因，不直接猜测真实类别。

## 3. 补全映射后重新计算

示例中确认 C 是有效练习类别，因此自行为它指定 2：

```python
class_to_idx["C"] = 2
mapped["class_id"] = mapped["label"].map(class_to_idx)
print(mapped)
```

输出：

```text
      path label  class_id
0  A/a.jpg     A         0
1  B/b.jpg     B         1
2  A/c.jpg     A         0
3  C/d.jpg     C         2
```

所有标签匹配后，本例结果是整数列。训练中同一个角色的编号需要保持一致，不要把未匹配角色自动填成已有角色编号，也不要求现在确定正式数据集的编号。

## 4. merge：用另一张表匹配

当对应关系存在另一张 DataFrame 中时，可以用 merge 按共同的 label 列合并：

```python
classes = pd.DataFrame({"label": ["A", "B"], "class_id": [0, 1]})
print(classes)
```

输出：

```text
  label  class_id
0     A         0
1     B         1
```

```python
joined = df.merge(classes, on="label", how="left")
print(joined)
```

输出：

```text
      path label  class_id
0  A/a.jpg     A       0.0
1  B/b.jpg     B       1.0
2  A/c.jpg     A       0.0
3  C/d.jpg     C       NaN
```

df 是左表，classes 是右表；on='label' 按两表同名的 label 匹配；how='left' 保留左表所有样本，找不到的编号显示缺失。这里的 classes 标签各不重复，因此行数仍是四行；如果右表同一个标签出现多行，一条样本可能匹配出多行，实际使用时应检查对应表是否唯一。

map 适合拿字典给一列找对应值，merge 适合用公共列连接两张表；各自返回结果，需要接住返回值。最终打印新表不等于自动保存到 CSV。

## 自己实践

可以在 scripts/pandas_basics.py 中新增自己的 day33 函数，或自选新文件：

1. 创建一个至少三行的样本 DataFrame，包含 path、label，其中至少两个类别；自己建立名称到整数的字典，用 map 新增 class_id 列并打印表格。
2. 故意放入一个字典里不存在的标签，使用 isna 找到未匹配行；之后自己补充映射，重新映射并查看结果。可以用 A/B/C，也可以自选练习名称。
3. 建立标签与编号的 DataFrame，用 merge(on='label',how='left') 把它与样本表连接；至少观察一次未匹配的缺失结果。
4. 比较两种写法的结果，理解一个查字典、一个按列连接两张表。样本值、函数名和打印格式可以自主决定。

不需要采集正式数据集、训练模型或改写原 CSV，不要求提前做冲突清洗或全部 join 类型。不强制额外口头考试。

## 收尾与记录

本日练习完成后按实际范围核对，问答与成果等用户确认结束后统一保存到 records/day33-record.md，再更新总进度。此文件只保存任务，尚未完成。未代写核心代码、安装依赖、Git 暂存、提交或推送；不提前创建 Day 34 任务。

参考：[Pandas Series.map](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)、[DataFrame.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)、[isna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)。

## 收尾状态：2026-10-29

核心练习完成。用户自行编写 day33，使用 map、isna、补充映射后重新计算，以及 merge 左连接；实际 Conda Python 执行正常，缺失项与连接结果正确。

当前 map 使用字符串 x/y/z，merge 右表的编号为 0/1；未将 map 示例记成整数映射。两表都含 n 列，结果自动分成左侧 n_x 和右侧 n_y；详细输出和问答统一保存到 records/day33-record.md。下一学习日 Day 34，等待用户要求开始；未代改核心代码或环境，未暂存、提交或推送。
