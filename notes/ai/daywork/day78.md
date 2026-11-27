# Day 78：复核卷积层的输入输出维度，为跳跃连接做形状准备

布置日期：2026-11-27。状态：进行中。建议运行环境：Mac 本地 CPU（无需 GPU，全部用小张量即可跑通）。预计 45–60 分钟。核心代码由你自行编写，我按需解释与验收。

## 今天的目标

第 11 周我们要手写残差块（ResNet 的核心积木）。残差块之所以叫“残差”，核心操作就是把输入 `x` 绕过主分支直接加到卷积输出 `out` 上：

```text
output = out + x
```

在 PyTorch 里，两个 4 维特征图 `(N, C, H, W)` 要想逐元素相加，**四个维度 `N`、`C`、`H`、`W` 必须一个不差地完全一致**。今天我们先专门用几个短小的形状实验，把卷积前后维度变化彻底踩实。

## 形状公式回顾

对单层 `nn.Conv2d`（默认 `dilation=1`），输入张量形状为 `(N, C_in, H_in, W_in)`：
- 批次 `N` 不变；
- 输出通道 `C_out = out_channels`；
- 输出高和宽分别按下面公式计算：

```text
H_out = (H_in + 2 * padding - kernel_size) // stride + 1
W_out = (W_in + 2 * padding - kernel_size) // stride + 1
```

注意在 PyTorch 里，你可以直接用假张量验证模型或卷积层形状，不需要每次都读图片：

```python
x = torch.randn(2, 16, 56, 56)  # 模拟 2 张图、16 通道、56×56 的特征图
```

## 自己动手实验

建议新建一个脚本（例如 `scripts/day78_conv_shapes.py`），在 Mac 上用 `torch.randn` 完成下面 3 组对照实验。**每组都先自己口算/手算输出形状，再打印代码结果核对**：

1. **实验一：连续两层“保尺寸、同通道”卷积（主分支直连准备）**
   - 创建模拟特征图 `x = torch.randn(2, 16, 56, 56)`；
   - 定义两层 `nn.Conv2d`：输入输出通道都是 `16`，`kernel_size=3, stride=1, padding=1`；
   - 让 `x` 依次通过这两层，打印每一步形状；
   - 验证直接写 `res1 = out2 + x` 能否成功，并打印 `res1.shape`。

2. **实验二：观察“升通道 + 步幅降采样”造成的形状不匹配**
   - 继续用 `x = torch.randn(2, 16, 56, 56)`；
   - 定义两层卷积模拟下采样阶段：
     - 第一层：`in_channels=16, out_channels=32, kernel_size=3, stride=2, padding=1`
     - 第二层：`in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1`
   - 手算经过这两层后的输出形状并打印确认；
   - 思考并观察：此时如果还像实验一那样直接算 `out + x`，为什么会报错？具体是哪几个维度对不上？

3. **实验三：用 `1×1` 卷积把跳跃分支对齐（投影分支形状准备）**
   - 再单独定义一个只用于跳跃分支的卷积层：`skip = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=1, stride=2, padding=0)`；
   - 手算 `shortcut = skip(x)` 的输出形状（`kernel_size=1, stride=2, padding=0` 带入上面公式），再跑代码打印 `shortcut.shape`；
   - 验证 `(out + shortcut).shape` 是否能够正常相加；
   - **数学彩蛋加练**：把输入高宽改成奇数 `55`，即 `x_odd = torch.randn(2, 16, 55, 55)`，分别再手算并运行一次实验二的 `out` 和实验三的 `shortcut`，看看它们出来的尺寸还能不能严格对齐（以及从公式上看是为什么）。

## 验收标准

- 在 Mac 上独立运行脚本通过，终端清楚打印出实验一、实验二、实验三（含 `56×56` 与 `55×55`）的形状结果，并与手算一致；
- 能用自己的话说明：
  1. 什么参数组合下的 `3×3` 卷积会保持通道和高宽完全不变；
  2. 当主分支做了升通道或 `stride=2` 下采样时，为什么需要 `1×1` 卷积且配合对应的 `stride`；
  3. 为什么 `kernel_size=3, padding=1, stride=2` 和 `kernel_size=1, padding=0, stride=2` 在奇偶尺寸下算出来的高宽总是一样。

## 记录约定

完成验收并确认结束当天任务后，再统一写入 `day78-record.md` 与总进度记录。核心代码由用户自行编写；不代写核心学习代码。
