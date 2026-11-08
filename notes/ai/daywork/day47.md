# Day 47：Pandas 分组汇总与条件赋值

日期：2026-11-08。巩固周第 5 天；用户自行编写练习，结束当日后统一记录。

## 数据

```python
import pandas as pd
df = pd.DataFrame({
    "label": ["A", "A", "B", "B"],
    "width": [100, None, 200, 300],
})
print(df)
```

输出 A 两行宽度 100、NaN；B 两行宽度 200、300，具体数值显示精度可能随版本不同。

## 一次分组汇总

```python
stats = df.groupby("label").agg(
    rows=("width", "size"),
    valid_widths=("width", "count"),
    mean_width=("width", "mean"),
)
print(stats)
```

输出：A 的 rows=2、valid_widths=1、mean_width=100；B 的 rows=2、valid_widths=2、mean_width=250。size 算所有行，count 算非缺失值，mean 跳过缺失。

## 条件赋值

```python
df["status"] = "ok"
df.loc[df["width"].isna(), "status"] = "missing"
print(df[["label", "status"]])
```

输出：A 的两行为 ok、missing；B 的两行均为 ok。loc 左边条件选行，右边列名选列，只修改目标表匹配的位置。status 是人为标记，不会补出真实宽度。

## 今日任务

1. 自行构建有多个类别且含缺失宽度的模拟表，使用 groupby.agg 统计各组行数、有效宽度数、平均宽度。
2. 用 loc 为宽度缺失的记录设置状态，打印结果，解释 size 和 count 的差别。
3. 指出每组有几行、几个有效宽度；可选择自己的列名与数据，不需准备正式数据集。

参考：[Pandas 分组](https://pandas.pydata.org/docs/user_guide/groupby.html)、[选择与赋值](https://pandas.pydata.org/docs/user_guide/indexing.html)。

## 完成情况

用户明确结束并进入 Day 48；代码中已进行分组统计与条件标记，stats 未打印。详情见 [当日记录](../records/day47-record.md)。
