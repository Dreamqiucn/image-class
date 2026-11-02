# Day 37：直方图与图片亮度分布

布置日期：2026-11-02。用户自行编写核心代码；本日结束后统一更新学习记录。

## 目标

了解直方图如何按数值区间统计频数，用 Pillow 和 NumPy 读取一张练习图片的灰度值，再用 Matplotlib 展示像素亮度分布。

## 简单示例

```python
import matplotlib.pyplot as plt

values = [10, 20, 30, 70, 80, 90]
fig, ax = plt.subplots()
ax.hist(values, bins=[0, 50, 100], edgecolor="black")
ax.set_xlabel("Value")
ax.set_ylabel("Count")
plt.show()
```

显示两根柱子：区间 [0, 50) 高度 3，区间 [50, 100] 高度 3。最后一个区间包含右端点。柱状图按指定类别画数量；直方图则将数值按区间分组计数。

## 图片练习

```python
from PIL import Image
import numpy as np

with Image.open("图片路径") as image:
    gray = image.convert("L")
    pixels = np.array(gray)

print(pixels.shape)
print(pixels.ravel().shape)
```

例如图像高 2、宽 3 时输出 `(2, 3)` 和 `(6,)`；实际尺寸随图片不同。`convert("L")` 转为 8 位灰度图，数值通常在 0 至 255，越大越亮；`ravel()` 把二维像素值展开为一维。

使用 `ax.hist(pixels.ravel(), bins=16, range=(0, 256))` 绘图；16 表示分 16 个等宽区间，横轴是灰度值，纵轴是落入各区间的像素个数。

## 今日任务

1. 自己用一张已有练习图片读入灰度数组并展平，打印两者 shape。
2. 画该图片的亮度直方图，标注横纵轴并显示；观察较多像素落在哪个亮度范围。
3. 尝试修改 bins 的数量，观察柱子宽度和分组细节的变化。

参考：[Matplotlib Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)、[Pillow Image](https://pillow.readthedocs.io/en/stable/reference/Image.html)。

## 完成情况

用户选择进入 Day 38，按现有代码范围结束；图形窗口与观察结果未确认。详情见 [当日记录](../records/day37-record.md)。
