# Day 46：Pandas 数据整理

日期：2026-11-08。巩固周第 4 天，用户自行编写练习，当天结束后统一记录。

## 练习数据

```python
import pandas as pd
df1 = pd.DataFrame({"label": [" A ", "B"], "width": ["200", None]})
df2 = pd.DataFrame({"label": ["A"], "width": ["100"]})
df = pd.concat([df1, df2], ignore_index=True)
print(df)
```

输出为 3 行：标签分别是带两侧空格的 A、B、A，width 分别为字符串 200、缺失值和字符串 100；缺失显示依版本可能不同。concat 纵向拼接并重新编号。

```python
df["label"] = df["label"].str.strip()
df["width"] = pd.to_numeric(df["width"], errors="coerce")
print(df.sort_values("width"))
```

按 width 升序的标签依次为 A、A、B，宽度依次为 100、200、缺失；排序保留原索引 2、0、1。strip 去除两端空白；to_numeric 将数字字符串转为数值，无法转换的值变缺失，默认缺失排最后。

`df["width"].fillna(0)` 返回填补后的列，不赋值不会改变 df；示例的 0 是占位，并非真实图片宽度。

## 今日任务

自己构造两个小表，拼接、去除标签空格、转数值、检查缺失值，并按 width 排序；单独展示 fillna 的效果，解释占位值的含义。可用模拟数据，无需修改真实数据文件。

参考：[Pandas 入门](https://pandas.pydata.org/docs/user_guide/10min.html)、[to_numeric](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)。

## 完成情况

用户修正拼接后表格的标签清理并确认结束，按现有代码范围记录，详情见 [当日记录](../records/day46-record.md)。
