# Day 61：固定小批次训练

2026-11-18 核心完成。用户将 `next(iter(train_loader))` 放在训练循环外，取一次两张图，做 20 次参数更新。在 Windows 的 image-class-conda 环境运行，首行 loss 为 0.6656，正确数 1/2。末行 loss 为 0.0206，正确数 2/2。两个指标使用各轮参数更新前算出的 logits，末行未重新评估第 20 次更新后的模型。当前输出展示预测和正确数，没有单独打印真实标签。

## 今天的问答

- 交叉熵用标签编号选择正确类别。正确类别获得的 softmax 概率越高，负对数损失越小。相对分数决定概率。
- `loss.backward()` 计算梯度，`optimizer.step()` 根据梯度更新权重和偏置。
- `iter(loader)` 建立一次批次遍历，`next(...)` 取下一批。循环外取一次可以固定批次，`for` 可以遍历全部批次，也可以用 `break` 只取首批。
- `len(loader)` 是批次数，`loader.batch_size` 是设置的批大小，`len(labels)` 或 `images.shape[0]` 是当前批实际有多少张图。
- `running / total` 是按样本数加权的平均 loss。每轮只有一批时，它等于该批的 `loss.item()`。输出中的「错误率」实际打印了平均 loss，错误率可用 `1 - 正确数 / 样本数` 计算。
