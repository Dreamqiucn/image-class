# Day 67 每日记录

日期：2026-11-22。主题：train、eval、no_grad 与验证 loss。

用户在 scripts/torch_weel10.py 新增 day67。每轮开始 layers.train()，遍历三张训练图完成前向、损失、清梯度、反向和 SGD 更新；随后 layers.eval()，在 torch.no_grad() 中遍历独立验证列表，计算验证 logits、交叉熵 loss 和正确数。

用户曾写 val_loader() 导致 TypeError，助手说明 DataLoader 对象应直接迭代，用户改为 for images,labels in val_loader。首次检查发现验证复用训练最后一个 loss、除以训练样本数、验证图默认总是翻转；经说明后用户分别改为对验证 logits/labels 算 loss、除以 len(new_photo_list)、验证 Dataset 传入 tran=0。用户明确不想计算 accuracy，按调整范围验收，以正确数表示结果。

实际使用 Mac image-class-conda Python 运行最终脚本，20 轮正常退出。本次首轮训练 loss 约 0.6824、验证 loss 约 0.0999、验证正确数 1；末轮训练 loss 约 0.0231、验证 loss 约 0.0035、验证正确数 1。验证只有一张图，且初始化与训练图顺序随机，不将本次结果用于判断泛化，也不保证每轮下降。

验证按 batch 样本数加权，分母 len(new_photo_list)=1 与本次实际遍历数量一致；未实现遍历时累计 total，如以后使用会丢弃样本的采样策略需按实际数量调整。训练与验证列表路径字面值不同；未运行用户自行编写的路径检查，也未做图片内容去重。未将准确率、用户独立复述理解或额外路径检查记作完成。

按用户指定范围核心完成。未代改学习代码、安装依赖或进行 Git 暂存、提交、推送。下一项 Day 68：记录真实训练与验证 loss 并绘图，等待用户要求开始。
