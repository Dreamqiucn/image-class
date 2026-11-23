# Day 66 每日记录

日期：2026-11-22。主题：组装简单 CNN 并接入训练循环。

用户自行在 scripts/torch_weel10.py 新增 day66，使用 Conv2d(3,8,3,padding=1)、ReLU、MaxPool2d(2)、Flatten、Linear(8192,2)，并用 CrossEntropyLoss 与 SGD 训练三张 64×64 练习图片，batch_size=2，20 轮。验证 loader 已创建但未执行。

第一次检查时脚本正常训练，但只打印各 batch 的 loss 和正确数；经说明按每轮汇总后，用户累计 batch loss 乘 batch 样本数及正确数，但最初未除以总数。再次说明后用户在每轮末将累计值除以 len(photo_list)，当前每轮恰好使用全部三张图，计算正确。

实际使用 Mac 的 image-class-conda Python 运行最终脚本，退出码 0：首轮平均 loss 约 0.5391、正确数 2/3；末轮约 0.0117、正确数 3/3。运行包含随机打乱和数据增强，结果随运行而变化，且仅为训练集指标，不代表泛化。最终脚本未打印 shape；此前一版打印的 logits 显示两张图为两行、最后一张为一行，每行两个类别分数，不虚构额外验证。

当前 loss 累加使用 Tensor，轮末调用 item()，数值正确；累计 loss.item() 可避免把训练图留在统计值里，但不要求重写。固定分母 3 适用于当前每轮遍历全部样本，若日后使用不同采样或丢弃批次，应统计实际样本数。用户未独立复述层和优化器功能，不记为已进行该理解检查。

Day 65 的代码实现到 Flatten，并逐层打印形状，见 [Day 65 学习记录](day65-record.md)。Day 66 接入 Linear 分类层。按核心训练与统计完成收尾，下一项 Day 67 学习 train/eval 和 no_grad；未更改用户学习代码、训练数据、Git 暂存、提交或推送。
