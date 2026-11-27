# Day 79：BatchNorm，理解训练与推理状态的区别

布置日期：2026-11-27。状态：已完成。建议运行环境：Mac 本地 CPU。预计 30–45 分钟。核心代码由你自行编写，按需验收。

## 今天的目标

搞懂 `nn.BatchNorm2d` 在 ResNet 里的位置和作用，并在一个精简实验里一次看清三件事：
1. `BatchNorm2d(C)` 保持 `(N, C, H, W)` 形状不变；
2. `train()` 模式下按当前批统计量归一化，并更新 `running_mean` / `running_var`；
3. `eval()` 模式下冻结 `running_mean` / `running_var`，只传 1 张图也能稳定预测。

## 核心原理

在 ResNet 里，卷积后通常接批归一化再激活：`Conv2d -> BatchNorm2d -> ReLU`。
- **`C` 怎么填**：`nn.BatchNorm2d(num_features)` 的参数必须等于前一层卷积的 `out_channels`（按通道独立归一化）。
- **`train()` 模式**：用**当前这一批**自己的均值和方差做归一化，同时后台用滑动平均更新 `running_mean` 与 `running_var`。
- **`eval()` 模式**：停止更新 `running_mean` / `running_var`，直接拿训练期间攒下来的统计量做归一化，单图预测也完全不受 batch 大小影响。

## 精简实验（做法一：1 个函数一次跑通）

在 `scripts/torch_week12.py` 里新增一个函数 `day79()`，按顺序串完下面几步：

1. **搭建并准备输入**：
   - 定义 `conv = nn.Conv2d(3, 8, kernel_size=3, stride=1, padding=1, bias=False)` 和 `bn = nn.BatchNorm2d(8)`；
   - 造一个偏置明显的假输入 `x = torch.ones(2, 3, 4, 4) * 10.0`（注意：`x` 经过随机初始化的 `conv` 后数值会变小、不再全为 10；如果想在输出均值和 `running_mean` 上看到非常直观的“接近 0 / 远离 0”对照，也可以另试一个直接把全 `10.0` 喂给 `nn.BatchNorm2d(3)` 的写法）。
2. **`train()` 模式跑一次**：
   - 先确认处于 `bn.train()`（新建层默认就是训练模式，显式写出来更清楚）；
   - 运行 `out = bn(conv(x))`（或直接对 `bn` 测），打印 `out.shape`、`out.mean()`，以及 `bn.running_mean[:3]`（会看到它从初始 `0` 开始向这批数据的均值移动）。
3. **`eval()` 模式只传 1 张图再跑一次**：
   - 切换为 `bn.eval()`；
   - 只取第 1 张样本 `x[:1]`（`batch_size=1`）再跑一次前向，打印 `out_eval.mean()` 和此时的 `bn.running_mean[:3]`（确认 `running_mean` 彻底冻结不变，且单图输入不报错）。

## 验收标准

- 在 Mac 上独立运行 `day79()` 通过，清楚看到：
  - 形状保持 `(2, 8, 4, 4)`；
  - `train()` 后 `running_mean` 发生变化，`eval()` 后完全冻结；
  - `eval()` 下单样本 `x[:1]` 顺利运行。
- 能用自己的话说明：`BatchNorm2d` 的通道参数从哪来，以及为什么验证/预测单图时一定要切 `eval()`。

## 记录约定

验收完成并确认结束当天任务后，再统一写入 `day79-record.md` 与总进度记录；核心代码由用户自行编写，不自动执行 Git 提交或推送。

## 收尾

2026-11-27 已完成。用户按精简单函数方案在 `scripts/torch_week12.py` 中编写 `day79()` 并在 Mac 上实测通过，完成 `train()` / `eval()` 下形状与 `running_mean` 冻结验证。见 [Day 79 记录](../records/day79-record.md)。
