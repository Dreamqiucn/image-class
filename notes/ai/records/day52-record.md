# Day 52：Tensor 运算、形状与设备

日期：布置 2026-11-10，2026-11-11 用户开始 Day 53，Day 52 结束。

- 用户自行实现 Tensor 加法、reshape、unsqueeze 和 squeeze；将 Tensor 复制到 CUDA 并计算后将结果带回 CPU。
- 在 image-class-conda 中运行 scripts/torch_basic.py 正常退出：shape 为 (1,2,3) 再变为 (2,3)，GPU 计算后返回 CPU 的结果为 [3,4,5,6,7,8]。用户代码未单独打印 GPU 上 y 的 device；运算实际经 CUDA 执行。
- 下一学习日 Day 53 学习自动求导与计算图。
