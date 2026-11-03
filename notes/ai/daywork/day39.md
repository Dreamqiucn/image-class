# Day 39：折线图、图例与保存

日期：2026-11-03。今天使用明确标注的模拟数据练习训练曲线，不代表真实训练结果；用户自行编写核心代码，当天结束后统一记录。

## 示例

```python
from pathlib import Path
import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4]
train_loss = [1.2, 0.9, 0.7, 0.5]
val_loss = [1.3, 1.0, 0.9, 0.8]

fig, ax = plt.subplots()
ax.plot(epochs, train_loss, marker="o", label="Train loss")
ax.plot(epochs, val_loss, marker="o", label="Validation loss")
ax.set_title("Simulated loss curves")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.legend()

output = Path("output")
output.mkdir(parents=True, exist_ok=True)
fig.savefig(output / "simulated_loss.png", dpi=150, bbox_inches="tight")
plt.show()
```

输出：显示模拟训练和验证损失两条折线，图例标明各自名称；在当前工作目录的 output 中保存 simulated_loss.png。使用已有同名文件时会覆盖。两条折线均向下，具体图形显示视环境而定。

`ax.plot(x, y)` 按位置配对坐标并依次连线；`label` 设置名称，`ax.legend()` 显示图例；`fig.savefig` 保存图片，建议放在 `plt.show()` 前。

## 今天任务

1. 自己准备等长的轮次、模拟训练损失和模拟验证损失，画两条折线并标注模拟数据。
2. 给图设置标题、横纵轴标签和图例，显示图像。
3. 把图保存为 PNG 并检查生成的文件。自选输出位置，注意同名文件会被覆盖。

参考：[Matplotlib 快速入门](https://matplotlib.org/stable/users/explain/quick_start.html)、[Figure.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html)。

## 完成情况

用户完成两条模拟损失曲线和 PNG 保存，已检查生成的图片；进入 Day 40。详情见 [当日记录](../records/day39-record.md)。
