# Day 52：Tensor 运算、形状与设备

日期：2026-11-10。用户自行编写练习，当天结束后统一记录。

## 运算和形状

```python
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x + 2)
print(x.reshape(3, 2))
print(x.unsqueeze(0).shape)
print(x.unsqueeze(0).squeeze(0).shape)
```

输出分别为 `[[3,4,5],[6,7,8]]`、`[[1,2],[3,4],[5,6]]`、`torch.Size([1, 2, 3])` 和 `torch.Size([2, 3])`。reshape 改变形状而元素个数保持，unsqueeze 新增长度为 1 的轴，squeeze(0) 仅在该轴长度为 1 时移除。

## CPU 和 GPU

```python
x = torch.tensor([1.0, 2.0])
print(x.device)
if torch.cuda.is_available():
    y = x.to("cuda")
    print(y.device)
    print((y + 1).cpu())
    print(x.device)
```

CUDA 可用时输出 cpu、cuda:0、tensor([2., 3.])、cpu；实际以环境为准。`to` 返回结果，原变量 x 仍在 CPU；通常参与同一运算的 Tensor 应在同一设备。

## 今日任务

1. 自建二维 Tensor，练习加法、reshape 和 unsqueeze/squeeze，打印值及 shape。
2. 检查 CUDA 可用时将 Tensor 放到 GPU 并计算，把结果返回 CPU；打印设备。
3. 解释 `.to("cuda")` 的返回值与原变量的关系，无需扩展复杂模型。

参考：[Tensor 入门](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)。

## 完成情况

用户代码运行成功，完成形状变化和 CUDA 计算并返回 CPU；用户进入 Day 53。详情见 [当日记录](../records/day52-record.md)。
