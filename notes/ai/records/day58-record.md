# Day 58：DataLoader 批量读取图片

2026-11-15 完成。用户在 scripts/torch_week9.py 中为三张图片统一 RGB 和 64×64 尺寸，转为 CHW Tensor，用 DataLoader 按两张一批读取。

- 在 image-class-conda 实际运行通过。启用 shuffle 后，这次得到形状 (2, 3, 64, 64)、标签 [1, 1]，以及形状 (1, 3, 64, 64)、标签 [0]。三张图全部读出。
- 讨论了 resize 的宽高参数、缩放时怎样计算像素、最近邻和双线性插值，以及 shuffle 怎样改变取样顺序。用户希望新用法先讲用途、参数和具体输出，再布置练习。
