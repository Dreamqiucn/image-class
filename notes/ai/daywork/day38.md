# Day 38：imshow 与图片网格

日期：2026-11-02。用户自行写核心代码；当天结束后统一更新学习记录。

## 目标

通过 imshow 展示图片，用 subplots 在一张 Figure 中排列多个 Axes，并为图片加类别标签。

## 显示一张图

```python
from PIL import Image
import matplotlib.pyplot as plt

with Image.open("图片路径") as image:
    rgb = image.convert("RGB")

fig, ax = plt.subplots()
ax.imshow(rgb)
ax.set_title("Character A")
ax.axis("off")
plt.show()
```

输出：窗口显示所选图片，标题是 Character A，坐标轴隐藏；实际图片取决于输入路径。

## 排列多个绘图区

```python
fig, axes = plt.subplots(1, 2)
print(axes.shape)
```

输出 `(2,)`。这是 1 行 2 列的两个 Axes；分别用 axes[0]、axes[1] 访问。二维排列例如 `plt.subplots(2, 2)` 默认返回 shape 为 `(2, 2)` 的 Axes 数组，可用 axes[0, 0] 访问第一格。

## 今天任务

1. 在同一张图中创建至少两个绘图区，展示两张已有图片，图片不足时可暂时使用同一张。
2. 给每张图设置对应类别标题，隐藏坐标轴，显示窗口。若中文字体无法显示，可先使用英文标签。
3. 理解 Figure、每个 Axes 和 imshow 的关系，观察两张图片的位置。

可使用已有练习图片，不需准备正式数据集。参考：[imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html)、[subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)。
