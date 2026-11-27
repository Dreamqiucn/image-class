# Day 80 每日记录

日期：2026-11-27。主题：残差连接 `x + F(x)`，理解主分支和跳跃分支。

用户自行在 `scripts/torch_week12.py` 中编写 `day80()`，搭建五层主分支 `main_path`（两层 `Conv2d(16, 16, 3, stride=1, padding=1, bias=False)` 配合两层 `BatchNorm2d(16)` 与中间一个 `nn.ReLU()`），用独立变量 `fx = main_path(x)` 保留原始 `x = torch.randn(2, 16, 56, 56)` 后计算 `out = torch.relu(fx + x)`。

过程中发现并修复两处代码细节：
1. 初版 `Conv2d(16, 16, 3, 1, bias=False)` 将位置参数 `1` 传给了默认的 `stride=1`、漏掉 `padding=1`（默认 `0`），导致特征图从 `56×56` 缩为 `52×52` 无法与 `x` 相加；用户自行补全 `stride=1, padding=1` 后修复尺寸问题。
2. 打印行曾误写 `out,shape` 触发 `NameError`，用户改为 `out.shape` 后重新验证通过。

在 Mac Conda Python（`torch 2.15.0`）实测运行通过，输出 `torch.Size([2, 16, 56, 56])` 连续三份一致。用户未额外打印 `fx.min()/max()` 或 `fx * 0 + x` 验证行，并在聊天中准确答出第二个 `ReLU` 放在 `fx + x` 之后的原因：“为了让 `fx` 有正有负，不然永远非负（`>= 0`）了”。当日问答另涵盖 `nn.Conv2d` 默认 `stride=1, padding=0` 及 `torch.relu` 与 `nn.ReLU` 的调用区别。

按当前范围核心完成，未代写核心学习代码，未操作 Git。下一学习日为 Day 81（手写同通道、同尺寸的 `BasicBlock` 并检查前向结果形状）。
