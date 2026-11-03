# Day 41：图片数据分析小练习

日期：2026-11-03。将 Pillow、NumPy、Pandas、Matplotlib 串起来，使用已有少量图片；用户自行编写核心代码。当天结束后统一整理记录。

## 目标

对至少两张练习图片读取 RGB 像素，计算每张图片的平均 RGB 像素值，并结合标签整理成表格，按类别画平均亮度相关的统计图。这里使用三个 RGB 通道的像素平均作为简化的亮度指标，不等同于感知亮度或 Pillow 的灰度转换。

## 基础示例

```python
import numpy as np

pixels = np.array([[[10, 20, 30], [40, 50, 60]]])
print(pixels.shape)
print(pixels.mean())
```

输出：`(1, 2, 3)` 和 `35.0`。这里示例是 RGB 各通道全部数值的平均值。

```python
import pandas as pd

df = pd.DataFrame([
    {"label": "A", "mean_rgb": 35.0},
    {"label": "A", "mean_rgb": 45.0},
    {"label": "B", "mean_rgb": 60.0},
])
stats = df.groupby("label")["mean_rgb"].mean()
print(stats)
```

输出：A 为 40.0，B 为 60.0；每张图片的平均值以相同权重参与类别均值。

## 今日任务

1. 自选至少两张已有图片；用 Pillow 转 RGB、NumPy 转数组并计算每张图的像素均值。图片及标签可手动指定。
2. 用 Pandas 汇总图片路径、类别和均值，按类别计算每张图片均值的平均。
3. 用 Matplotlib 将类别和均值画成柱状图，设置标题及坐标轴；打印表格，简单说出结果。类别相同也可完成练习，若有两个类别更方便比较。

不要求正式数据集、模型训练或额外安装；不覆盖已有输出数据。参考：[NumPy mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)、[Pandas groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)。
