# Day 55：分类分数、标签与交叉熵

日期：2026-11-13。用户自行写练习，当天结束后统一记录。所有分数和类别为模拟，不是训练结果。

## 基本示例

```python
import torch
from torch import nn

logits = torch.tensor([[2.0, 0.0], [0.0, 2.0]], requires_grad=True)
targets = torch.tensor([0, 1], dtype=torch.long)
print(logits.argmax(dim=1))
loss = nn.CrossEntropyLoss()(logits, targets)
print(loss.item())
loss.backward()
print(logits.grad)
```

输出预测为 `tensor([0, 1])`，loss 约 `0.126928`，梯度约 `[[-0.0596, 0.0596], [0.0596, -0.0596]]`。两条模拟样本、每条两类分数，targets 是正确类别编号。CrossEntropyLoss 接受未归一化 logits，内部处理 softmax 及对数损失，不提前对输入 softmax；默认批次损失取平均。

## 今日任务

1. 手工准备两条样本、每条两个类别的 logits 和对应整数标签，打印 shape、预测编号和交叉熵。
2. 改变正确类别的分数并比较损失；明确真实标签不变，打印前后数值。
3. 对 requires_grad=True 的模拟 logits 反向求导并查看梯度，理解 backward 不更新参数。无需训练模型。

参考：[CrossEntropyLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)、[PyTorch 优化教程](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)。

## 完成情况

已实际运行验证损失变化和反向求导。用户进入 Day 56，详情见 [当日记录](../records/day55-record.md)。
