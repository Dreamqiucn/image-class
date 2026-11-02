# Day 36：Matplotlib 入门与柱状图

日期：2026-11-01。今天学习 Figure、Axes 和柱状图，用模拟类别数量练习；A、B、C 不代表正式角色。用户自行编写核心练习，学习记录在结束当天后统一更新。

## 环境

在 VS Code 选用的 Python 环境中运行 `python -c "import matplotlib; print(matplotlib.__version__)"`。若提示没有 matplotlib，用户可在已激活的 Conda 环境中自行运行 `conda install matplotlib`；无需助手代装。

## 入门示例

```python
import matplotlib.pyplot as plt

labels = ["A", "B", "C"]
counts = [5, 3, 7]
fig, ax = plt.subplots()
ax.bar(labels, counts)
ax.set_title("Samples per class")
ax.set_xlabel("Class")
ax.set_ylabel("Count")
plt.show()
```

输出：显示柱状图，横轴 A、B、C 对应柱高 5、3、7；标题为 Samples per class，两个坐标轴分别标注 Class 和 Count。普通脚本中通常以窗口展示，不是终端打印文本。

`fig` 是整张图，`ax` 是其中画数据的区域；`plt.subplots()` 返回这两个对象。`ax.bar(labels, counts)` 依位置配对类别和数量。Axes 是绘图区，Axis 指坐标轴，也不同于 NumPy 的轴。

## 今天任务

1. 用户自己编写脚本，使用至少三个模拟类别和对应数量，通过 `plt.subplots()`、`ax.bar()`、标题和横纵轴标签画柱状图。
2. 显示图像；修改一个数量重新运行，观察对应柱子的变化。
3. 能解释 Figure、Axes 与类别和数量的对应关系；可用自己之前的统计数据，但不要求准备正式数据集。

下一次继续学习直方图。参考：[Matplotlib 官方快速入门](https://matplotlib.org/stable/users/explain/quick_start.html)。

## 完成情况

用户选择进入 Day 37，按现有代码范围结束。代码已覆盖柱状图核心写法；图形窗口和修改数量后的运行未确认。详情见 [当日记录](../records/day36-record.md)。
