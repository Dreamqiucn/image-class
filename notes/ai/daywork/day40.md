# Day 40：混淆矩阵与热力图

日期：2026-11-03。用手工模拟例子理解分类结果，不代表真实模型；用户自行编写核心代码，当天结束后统一整理记录。

## 理解矩阵

约定行表示真实类别，列表示预测类别。模拟矩阵 `[[3, 1], [2, 4]]` 表示真实 A 预测 A 有 3 个、预测 B 有 1 个；真实 B 预测 A 有 2 个、预测 B 有 4 个。主对角线是预测正确数量，其他位置是预测错误数量。

## 画图示例

```python
import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([[3, 1], [2, 4]])  # 模拟数量
labels = ["A", "B"]
fig, ax = plt.subplots()
image = ax.imshow(matrix, cmap="Blues")
ax.set_xticks([0, 1], labels=labels)
ax.set_yticks([0, 1], labels=labels)
ax.set_xlabel("Predicted label")
ax.set_ylabel("True label")
ax.set_title("Simulated confusion matrix")
fig.colorbar(image, ax=ax)
for row in range(2):
    for col in range(2):
        ax.text(col, row, matrix[row, col], ha="center", va="center")
plt.show()
```

输出：窗口显示 2×2 蓝色热力图，每格标注 3、1、2、4，旁边有颜色条。横轴是预测类别，纵轴是真实类别。

## 今日任务

1. 自己准备 2×2 模拟矩阵，说出每格含义。
2. 用 imshow 画热力图，标注真实和预测类别，显示各格数字。
3. 能指出正确与错误预测分别在哪些格子；无需安装新库或训练模型。

参考：[混淆矩阵定义](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)、[Matplotlib 热力图](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)。

## 完成情况

用户完成混淆矩阵热力图代码并选择进入 Day 41；窗口运行结果未确认。详情见 [当日记录](../records/day40-record.md)。
