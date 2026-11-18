# Day 60：把前向、损失、反向、更新串成训练循环

2026-11-17。沿用 Day 59 的 Dataset 和 train/val 两个 loader。今天第一次让参数真正被损失推动。

## 循环里的四个动作

- `logits = model(images)`：前向，得到每个类别的原始分数
- `loss = loss_fn(logits, labels)`：这些分数离正确标签有多远
- `optimizer.zero_grad()`：清掉上一轮累积的梯度
- `loss.backward()`：反向传播，把梯度写进每个参数
- `optimizer.step()`：按梯度更新参数

`zero_grad()` 必须排在 `backward()` 之前。少了这一步，梯度会在参数里一轮轮累加，更新方向就乱了。

## 今天要换掉的东西

Day 55 算过 `CrossEntropyLoss`，但传进去的是手写的固定 logits，参数从头到尾没动过。今天把模型换成真正的层，让 `optimizer.step()` 真的改权重。

`nn.Linear` 只接收二维张量 `(样本数, 特征数)`，而 loader 给的是 `(批次, 3, 64, 64)`。用 `nn.Flatten()` 放在网络最前面，展平成 `(批次, 12288)`，因为 3 × 64 × 64 = 12288。

## 练习

1. 新建 `scripts/torch_week10.py`，把 Day 59 的 Dataset 和两个 loader 搬进来。切分点写死：`photo_list[:2]` 训练、`photo_list[2:]` 验证。别再让 `random.randint` 决定，它可能切出个训练集只剩一张、甚至只剩一个类别的结果。
2. 定义网络：`nn.Sequential(nn.Flatten(), nn.Linear(12288, 32), nn.ReLU(), nn.Linear(32, 2))`。最后输出 2，因为只有 2 个类别。
3. 创建三个对象：模型、`loss_fn = nn.CrossEntropyLoss()`、`optimizer = torch.optim.SGD(model.parameters(), lr=0.01)`。
4. 写 `for epoch in range(20):`，每轮遍历 `train_loader`，把上面四个动作依次执行，把 `loss.item()` 累加起来。
5. 每轮打印 epoch 序号和这一轮的平均 loss。

## 验收

1. 训练开始前，在验证集上量一次 loss，用 `with torch.no_grad():` 包住，验证不需要建计算图。把这个数字记下来。
2. 训练 loss 要从 0.7 附近一路降到 0.05 以下。二分类乱猜的对数损失就是 ln(2) ≈ 0.69，起点大致落在那里，压到这个量级才说明参数真的被推动了。
3. 训练结束再量一次验证 loss，和起点比。它多半会**变大**。

## 一句提醒

训练 loss 一路降、验证 loss 反而升，这两条线分开的那一刻，就是过拟合的样子。3 张图配 39 万个参数，模型把两张训练图背了下来，再来一张新图就不认识了。

验证集只有一张图，准确率只能是 0 或 1，那个数字没有任何统计意义，别拿它当模型好坏的证据。今天的验收只看训练 loss 有没有下去、流程有没有走通。

设备保持 CPU 就好。三张图挪到 MPS 上，搬运的时间比计算还长，等数据量上去再折腾设备。

## 参考

- [PyTorch 优化循环教程](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [torch.optim.SGD](https://docs.pytorch.org/docs/stable/generated/torch.optim.SGD.html)

## 收尾

2026-11-17 用户在 Mac 上完成。个人笔记记录训练 20 轮，训练 loss 下降。见 [Day 60 记录](../records/day60-record.md)。
