# Day 62：完整训练循环与每轮统计

沿用 Day 60/61 的 Dataset、训练集、模型、交叉熵和 SGD。今天把固定一批图片的训练写成完整的一轮训练循环。每个 epoch 都遍历训练集里的所有 batch，每处理一个 batch 就更新一次参数，最后统计这一轮的平均 loss 和猜对数量。

## 先看懂计数

- `running_loss` 累加每批的平均 loss 乘以图片数，所以最后除以总图片数时得到按图片加权的平均 loss。若训练集两张图恰好是一批，那么这一轮的平均 loss 等于这一批的 loss。
- `total_correct` 累加每批猜对的张数。
- `total_samples` 累加实际处理的图片数。即使最后一批较小，准确率也要除以实际图片总数。
- `logits.argmax(dim=1)` 对每行两个类别分数取最大值的下标，得到每张图的预测类别。
- `(pred == labels).sum().item()` 先逐个比较预测和正确标签，再把猜对数量转成普通 Python 数字。

## 今天的任务

在 `scripts/torch_week9.py` 里，为当前训练集编写完整的 epoch 循环，先运行 20 轮。每一轮开始把三个统计量重置为 0，然后遍历 `train_loader`。每个 batch 都做前向计算、交叉熵、清空旧梯度、反向传播和参数更新，再更新 loss 总和、猜对数和已处理图片数。

每轮结束只打印一行，包含 epoch、平均 loss、正确数和准确率。准确率计算为 `total_correct / total_samples`。注意 `loss` 是每批的平均值，所以累计它时要乘上当前 `labels` 的样本数。

示例结构：

```python
for epoch in range(20):
    running_loss = 0.0
    total_correct = 0
    total_samples = 0

    for images, labels in train_loader:
        # 前向、计算 loss、清梯度、反向传播、更新参数
        # 累加本批 loss 对应的总量
        # 累加本批预测正确数和样本数
        pass

    average_loss = running_loss / total_samples
    accuracy = total_correct / total_samples
    print(epoch + 1, average_loss, total_correct, total_samples, accuracy)
```

把 `pass` 和注释替换成自己的代码。Day 61 固定批次时把 `next(iter(train_loader))` 放在循环外。今天应直接遍历 `train_loader`，这样每轮都会处理所有 batch。

## 验收

本次练习最终使用三张训练图，batch size 为 2，所以每轮处理一批两张和一批一张。每轮处理的样本数应为 3，正确数在 0 到 3 之间。平均 loss 通常会逐渐下降，但随机初始化和学习率会影响具体数值。这里的训练准确率只表示模型对训练图片的预测情况。

## 收尾

2026-11-19 核心完成。脚本跑完 20 轮，每轮汇总平均 loss 和正确数，当前用「正确数 / 总数」展示训练准确率。见 [Day 62 记录](../records/day62-record.md)。

参考 [PyTorch 优化循环教程](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)。
