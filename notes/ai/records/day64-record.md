# Day 64：Conv2d 与卷积输出形状

2026-11-20 核心完成。用户用 RGB 图片、3×3 卷积核和 8 个输出特征图练习前向，确认已分别运行三组 stride 和 padding。核对保存的脚本时，当前是 (1, 0)，独立运行得到 (2, 8, 62, 62) 和 (1, 8, 62, 62)。按公式，(1, 1) 输出高宽均为 64，(2, 1) 输出高宽均为 32。

用户最初认为 (1, 0) 保留高宽。在聊天中代入公式核对：无填充时是 64 - 3 + 1 = 62，每边填充一格后是 66 - 3 + 1 = 64。

## 今天的问答

- `photo_process` 缺少 `__len__` 时，开启 shuffle 的 DataLoader 无法读取数据集大小。在类里实现 `__len__(self)`，返回 `len(self.sample)`。
- `def __getitem__(num)` 少了 `self`。取样本时 Python 会把数据集对象和下标一起传入。
- `from PIL import Image` 导入的是模块。用 `with Image.open(path) as image` 打开图像，在退出代码块时关闭文件。
