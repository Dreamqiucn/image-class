# Day 56：PyTorch 基础复盘

2026-11-14，用户完成聊天复盘并明确结束 Day 56。

- Tensor：正确区分 CPU 上的原 Tensor 和转到 GPU 的结果，也正确区分 from_numpy 共享数据和 torch.tensor 复制数据。复习了 unsqueeze 按指定位置插入长度为 1 的轴，随后正确回答了 axis=2 的形状。讲解了 to(torch.float32) 需要接收返回值。
- 自动求导：正确回答梯度累积结果为 4、8，也能调整 requires_grad_ 的调用顺序。复习了多元素输出不能直接无参数 backward，求总和的梯度可用 y.sum().backward()。起初选错 .item() 后用于求导的对象，后续正确区分了覆盖 loss 和仅打印 loss.item()。讲解了 backward 计算梯度，优化器按梯度更新参数。
- 网络层：正确判断 Linear 的输入和输出形状，区分 __init__ 和 forward，答对 ReLU 的输出数值。练习后正确回答 Linear(2, 3) 的权重形状 (3, 2) 和偏置形状 (3,)。
- 分类：正确选用 logits 计算交叉熵，知道 logits 需为浮点数，也能判断两次均预测正确时哪组分数的损失更大。用逐项比较和求和复习准确率，纠正正确个数后答对变式。用户追问 softmax，解释了它如何将每条样本的 logits 转为一组概率，以及交叉熵接收原始 logits 的用法。

本日为聊天复盘。下一学习日为 Day 57，学习从 Dataset 取出一张图片及其标签。
