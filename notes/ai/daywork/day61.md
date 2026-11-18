# Day 61：让模型学会固定的一批图片

目标是在 Day 60 的模型上，只用一批固定图片反复更新参数。比较训练前后的 loss、预测类别和准确率，检查模型能不能认出它反复见过的样本。

## 先看懂用法

`images, labels = next(iter(train_loader))` 会从 DataLoader 取出一批数据。`iter(train_loader)` 创建一个迭代器，`next(...)` 取第一批。把这行放在训练循环外，就会一直用同一批 Tensor。本练习中 `images.shape` 是 `(2, 3, 64, 64)`，`labels.shape` 是 `(2,)`。如果 loader 启用了 shuffle，第一批的标签顺序可能是 `[0, 1]` 或 `[1, 0]`，每个标签仍然跟着自己的图片。

模型输出 `logits` 的形状是 `(2, 2)`，每行是一张图的两个类别分数。用 `logits.argmax(dim=1)` 取每行最高分的类别编号。

```python
logits = torch.tensor([[2.0, 0.5], [1.2, 0.8]])
labels = torch.tensor([0, 1])
pred = logits.argmax(dim=1)
correct = (pred == labels).sum().item()

print(pred.tolist())       # [0, 0]
print(correct)             # 1
print(correct / len(labels))  # 0.5
```

`pred == labels` 逐项得到 `[True, False]`，求和就是猜对的张数。用交叉熵时，继续把原始 `logits` 和真实 `labels` 传给损失函数。可以用 `with torch.no_grad():` 包住训练前和最后一次参数更新后的检查，只计算指标。中间要反向传播的训练循环放在这个代码块外。

## 今天的任务

在 Day 60 脚本的基础上写一个固定批次实验。先从训练 loader 取一批，打印训练前的 loss、预测类别、真实标签和准确率；再用这批图反复执行 Day 60 的训练步骤，可以先跑 20 次；最后用更新过参数的模型重新计算这批图的同样四项结果。

验收时看训练后的 loss 是否下降、预测类别是否逐个和真实标签对上。示例输出如下，实际数字和标签顺序可以不同。

```text
训练前 loss=0.71  预测=[0, 0]  标签=[0, 1]  正确=1/2
训练后 loss=0.04  预测=[0, 1]  标签=[0, 1]  正确=2/2
```

这里的准确率只描述这批训练图片。

参考 [PyTorch 优化循环教程](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)。

## 收尾

2026-11-18 核心完成。固定批次实测 loss 降低且两张训练图均预测正确。末行输出使用最后一次更新前的分数。见 [Day 61 记录](../records/day61-record.md)。
