# Day 57：用 Dataset 读取一张图片和标签

日期：2026-11-14。今天用项目里已有的图片，练习用 `len(dataset)` 查看样本数，用 `dataset[0]` 取得一张图片和对应的整数标签。

## 先理解三个方法

- `__init__(self, samples)`：创建对象时，保存由 `(图片路径, 类别编号)` 组成的列表。
- `__len__(self)`：执行 `len(dataset)` 时调用，返回样本数量。
- `__getitem__(self, idx)`：执行 `dataset[idx]` 时调用，取出第 idx 个样本的路径和标签，打开图片并返回 `(图片, 标签)`。

先用两张已有图片手动建立列表。在项目根目录运行时，可用 `1/丰川祥子/saki.webp` 和 `1/汐见萤/shiomi.webp`，练习编号分别为 0 和 1。也可以自选另两张图片。

## 练习步骤

1. 从 `torch.utils.data` 导入 `Dataset`，定义子类并保存样本列表。
2. 在 `__getitem__` 中按索引取路径和标签，用 Pillow 读取图片并转成 RGB。可以先返回 Pillow 图片及整数标签。
3. 创建对象，用 `len(dataset)` 和 `image, label = dataset[0]` 验证。用上述列表时，数量是 2，首个标签是 0，`image.mode` 是 RGB。也可以用 `dataset[1]` 核对标签 1。

可选：用 `torch.from_numpy(np.array(image)).permute(2, 0, 1)` 将 RGB 图片转为 Tensor，在返回前打印或用调用方检查形状。形状从 `(高, 宽, 3)` 变为 `(3, 高, 宽)`。下一天 Day 58 将用 DataLoader 组织批次。

参考：[PyTorch 自定义 Dataset](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html#creating-a-custom-dataset-for-your-files)。

## 完成情况

2026-11-14 实际运行通过。三条样本中取出第三张图片，输出为 `RGB 1`。详情见 [Day 57 记录](../records/day57-record.md)。
