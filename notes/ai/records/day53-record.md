# Day 53：PyTorch 自动求导

日期：2026-11-11；2026-11-12 用户进入 Day 54。

- 用户自行实现 x=2.0、y=x**x 的自动求导，并通过重新计算 y 再 backward 观察累积、使用 x.grad.zero_ 清空梯度。
- 在 image-class-conda 中运行成功，三次梯度依次约 6.7726、13.5452、6.7726，与 x^x 的导数在 x=2 处一致。
- 问答涉及多元素输出不传参数调用 backward 报错、梯度与导数、requires_grad、backward 与 .grad 的作用；更正无参数 backward 可处理单元素输出，不限零维标量。
