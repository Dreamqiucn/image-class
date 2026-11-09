# Day 51：Tensor 基础

日期：2026-11-09。用户确认结束。

- 用户在 scripts/torch_basic.py 中创建二维 Tensor 和 zeros Tensor，查看 shape、dtype、device；使用 to(torch.float32) 转换并打印结果。
- 创建 NumPy 数组，通过 from_numpy 建共享数据的 Tensor，使用 torch.tensor 创建独立副本，修改数组并打印两个结果，再通过 numpy() 转回数组。
- 在 image-class-conda 中实际运行成功，int64 转 float32 正常，共享 Tensor 显示修改后的 100，副本保留 3。zeros 已创建但未打印，不记为已检查其输出。
- 下一学习日 Day 52：Tensor 运算、维度与设备，等待用户开始。
