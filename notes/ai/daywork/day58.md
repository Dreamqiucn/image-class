# Day 58：用 DataLoader 读取一批图片

2026-11-15。继续用 Day 57 的三张图片，观察 DataLoader 怎样把单条样本组成批次。

1. 在 Dataset 的 `__getitem__` 中，用 Pillow 读取图像、转 RGB 并缩放到相同尺寸，例如 `resize((64, 64))`。用 `torch.from_numpy(np.array(rgb)).permute(2, 0, 1)` 转成形状为 `(3, 64, 64)` 的 Tensor。返回这个 Tensor 和原来的整数标签。
2. 从 `torch.utils.data` 导入 `DataLoader`。用 `DataLoader(x, batch_size=2, shuffle=False)` 创建加载器，循环取出 `images, labels`，打印 `images.shape` 和 `labels.tolist()`。
3. 按昨天的图片顺序，预期第一批为 `torch.Size([2, 3, 64, 64])` 与 `[0, 1]`，第二批为 `torch.Size([1, 3, 64, 64])` 与 `[1]`。解释为什么最后一批只有一张图。
4. 改成 `shuffle=True` 观察取样顺序。图片与各自的标签一起移动；两张图片同为标签 1，单看标签不一定能区分它们。

核对形状时，从左到右依次是批次中的图片数、通道数、高和宽。缩放到 64×64 是本次练习的选择。Day 59 再学习图像预处理与数据划分。

参考 [PyTorch DataLoader 教程](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html#preparing-your-data-for-training-with-dataloaders)。

## 完成情况

实际运行通过，两批分别有两张和一张图。详见 [Day 58 记录](../records/day58-record.md)。
