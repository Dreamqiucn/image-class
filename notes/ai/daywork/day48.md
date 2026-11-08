# Day 48：Matplotlib 多图与散点图

日期：2026-11-08。巩固周第 6 天；用户自行编写练习，结束后统一记录。

## 模拟图片尺寸

```python
widths = [100, 200, 300]
heights = [200, 250, 350]
```

三个模拟点分别为 (100,200)、(200,250)、(300,350)，横轴是宽、纵轴是高；不是实际图片尺寸。

```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(widths, heights)
axes[0].set_xlabel("Width")
axes[0].set_ylabel("Height")
axes[0].grid(True)
axes[1].bar(["A", "B"], [2, 1])
axes[1].set_title("Sample counts")
fig.tight_layout()
fig.savefig("day48_practice.png")
plt.show()
```

输出：窗口左侧显示 3 个散点和网格，右侧显示 A=2、B=1 的柱状图；当前工作目录保存 PNG，同名文件会覆盖。figsize 使用英寸，tight_layout 调整布局。

## 今日任务

1. 自己构造几组模拟宽高，画散点图并标横纵轴和网格。
2. 用 subplots 创建至少两个绘图区，另一图可画模拟类别数量柱状图；调整 figsize，显示图形。
3. 保存 PNG 并检查结果；不用准备正式数据集。输出路径可自选，避免意外覆盖。

参考：[scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html)、[subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)。

## 完成情况

用户完成散点图、多图布局及保存，已查看输出图片；详情见 [当日记录](../records/day48-record.md)。
