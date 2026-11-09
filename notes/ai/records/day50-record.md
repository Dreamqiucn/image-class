# Day 50：PyTorch 安装和环境验证

日期：2026-11-09。用户选择开始 Day 51，Day 50 结束。

- 用户自行在 image-class-conda 安装 PyTorch；实际检查 torch 2.14.1+cu130、CUDA 13.0，识别 RTX 5070 Ti Laptop GPU。
- 在激活的 Conda 环境中手动调用用户的 torch_basic.py 的 day50()，CPU 和 CUDA 均成功前向计算 14.0，反向梯度 [2.0,4.0,6.0]。检查时文件定义了函数但未在末尾调用，因此以手动调用的结果为证据。
- 问答解释 backward、梯度、x.grad.cpu().tolist()；tolist 可以自行转到 CPU。未将已讲解内容记为完全掌握。
