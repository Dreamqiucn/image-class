# Day 59：图像预处理与训练集、验证集

2026-11-16。沿用 Day 58 的三张图片及 Dataset。本日观察输入的数据格式和不同集合的处理规则。

## 像素缩放

`pixels.float() / 255.0` 把 8 位像素从 0～255 缩放到 0～1，形状保持 `(3, 64, 64)`。例如 `[0, 128, 255]` 变成约 `[0.0000, 0.5020, 1.0000]`，类型变成 `torch.float32`。

## 划分与随机增强

训练集用于更新参数，验证集用于检查模型在未参与参数更新的样本上的表现。先按原图划分，同一张原图及其变体应放在同一集合。可用列表切片演示前两张训练、第三张验证。如果两张汐见萤图片来自同一张原图，请换一张独立图片或用虚拟路径演示划分。三张图片用于验证代码流程，验证集只有一张且可能缺少类别。

两个 Dataset 都转换 RGB、统一尺寸和缩放像素。给 Dataset 增加可选的训练标记或可调用的翻转参数，只为训练样本启用随机水平翻转。可用 `torchvision.transforms.RandomHorizontalFlip(p=0.5)`，先创建变换对象，再调用它处理图片。`p=1.0` 可用于确认翻转确实发生。验证份使用固定预处理。

## 练习验收

1. 打印训练和验证样本数量，若用三张独立样本按两张和一张划分，预期为 2 和 1。
2. 打印各取一张的 shape、dtype 和像素最小与最大值，预期为 `(3, 64, 64)`、`torch.float32`，且像素都在 0～1。
3. 训练侧试 `p=1.0`，用一张左右不对称的图确认翻转，再改回 `p=0.5`。重复读取同一张验证图，检查结果相同且标签仍然对应原图。

参考 [TorchVision 图像变换](https://docs.pytorch.org/vision/stable/transforms.html) 和 [RandomHorizontalFlip](https://docs.pytorch.org/vision/main/generated/torchvision.transforms.v2.RandomHorizontalFlip.html)。

## 收尾

2026-11-16 按当前范围结束。分别取批实测通过，脚本入口仍遍历全量 loader。见 [Day 59 记录](../records/day59-record.md)。
