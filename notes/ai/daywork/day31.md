# Day 31：条件筛选、缺失值与重复记录

布置日期：2026-10-28。预计约 60 分钟，接续 Day 30。使用已有 Pandas，核心练习由用户自己写。

## 今天的目标

用条件选择行，查看缺失值，并按必要列去除缺失与重复记录。今天在内存中使用小样本表练习，不要求修改或覆盖已有 CSV，也不要求重新扫描图片。

## 示例表

```python
import pandas as pd

rows = [
    {"Path": "A/a.jpg", "Label": "A", "Width": 640},
    {"Path": "A/a.jpg", "Label": "A", "Width": 640},
    {"Path": "B/b.jpg", "Label": "B", "Width": 800},
    {"Path": "C/c.jpg", "Label": None, "Width": None},
    {"Path": "A/d.jpg", "Label": "A", "Width": None},
]
df = pd.DataFrame(rows)
print(df)
```

示例路径、标签和宽度只是练习数据。Path、Label 的大小写与当前样本 CSV 对应，Width 是本次人为添加的示例列，并不表示现有 CSV 已有该列。原表有 5 行：两条完全重复，一条缺 Label，另一条虽然缺 Width 但 Path 和 Label 完整。

## 1. 按条件选择行

```python
print(df["Label"] == "A")
print(df[df["Label"] == "A"])
print(df[(df["Label"] == "B") & (df["Width"] >= 700)])
```

比较先生成每行 True/False 的 Series；放到 df[...] 中后，保留 True 的行。组合条件用 & 或 |，每个条件分别加括号，不用 and/or 组合整列。筛选结果默认保留原索引，例如符合条件的行原索引是 0、1、4，就仍显示 0、1、4；索引不是筛选后的行数。

## 2. 查看和处理缺失值

```python
print(df.isna())           # 每个格子是否缺失
print(df.isna().sum())     # 每列缺失数量
print(df[df["Label"].isna()])  # 找出缺 Label 的行
```

示例中的 Label 有 1 个缺失，Width 有 2 个缺失。isna 检测缺失值；人工 DataFrame 中空字符串 "" 默认不是缺失值。CSV 默认读取规则可能把空字段识别成缺失值，具体视读入参数和内容而定。

```python
valid = df.dropna(subset=["Path", "Label"])
print(valid)
```

subset 指只检查 Path 和 Label：两列中任意一个缺失就不保留该行。Width 缺失的 A/d.jpg 仍保留。dropna 返回结果，默认不改变原 df；不赋值只会看到结果，原表与原 CSV 都不会因此改变。

## 3. 查看和去除重复

```python
print(valid.duplicated(subset=["Path"]))
print(valid[valid.duplicated(subset=["Path"])])
clean = valid.drop_duplicates(subset=["Path"])
print(clean)
```

这次用 Path 判断重复。duplicated 默认将第一次出现标为 False、后续重复标为 True；drop_duplicates 默认保留第一次出现的记录。例子中 A/a.jpg 留下一条，最终 3 行（A/a.jpg、B/b.jpg、A/d.jpg），默认仍保留原索引 0、2、4。

按路径去重是按字符串值判断，不是按图片内容去重。真实数据中同一路径如果出现不同标签，要先检查冲突；不要把相同角色标签的不同图片当成重复样本。

## 自己实践

可以在 scripts/pandas_basics.py 新增函数，或选择新文件。自己建立几行练习数据：包含 Path、Label、Width，至少有一条相同路径重复、一条 Label 缺失和一条仅 Width 缺失；也可用上述示例。

1. 根据 Label 筛选一个类别；再尝试两个条件组合，观察 True/False 和筛选结果。
2. 打印每列缺失数，找到缺 Label 的行；使用 dropna(subset=["Path","Label"]) 得到新表，确认仅缺 Width 的行仍在。
3. 用 duplicated(subset=["Path"]) 找重复，再用 drop_duplicates(subset=["Path"]) 得到去重后的新表。
4. 打印清理前后行数与结果；如果采用示例，预期 5→4→3。查看原 df 的行数，理解返回新表不会默认改掉原表。

不要求固定函数名、输出格式、额外口头考试或写新 CSV。真实数据的冲突处理、文件存在性、分组统计留到后续按需要学习，不提前整理正式角色数据集。

## 完成与记录

能运行条件筛选、缺失值检查、按必要列 dropna 和按路径检查/去重，并理解原表与清理后结果即可按核心范围收尾。当天问答与成果在用户结束本日后统一保存到 records/day31-record.md，再更新总进度；不提前标记完成。未代写核心代码、安装依赖或 Git 暂存、提交、推送；不提前创建 Day 32 任务。

参考：[Pandas 条件选择](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)、[isna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)、[dropna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)、[duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)、[drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)。
