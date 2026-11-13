# Day 53：PyTorch 自动求导与计算图

日期：2026-11-11。用户自行编写练习，结束后统一记录。

## 概念

requires_grad=True 让 PyTorch 记录相关运算供自动求导；backward 从标量输出逆向计算并将叶子 Tensor 的梯度累积至 .grad。例子假设 CPU 上浮点 Tensor。

```python
import torch
x = torch.tensor(3.0, requires_grad=True)
a = x ** 2
y = 2 * a + 1
print(y)
y.backward()
print(x.grad)
```

输出 `tensor(19., grad_fn=...)`（grad_fn 名称可能不同）和 `tensor(12.)`。y=2x²+1；dy/dx=4x，在 x=3 时为 12。计算关系为 x → a=x² → y=2a+1；反向使用链式法则 2×6=12。

## 梯度累积

```python
x = torch.tensor(3.0, requires_grad=True)
(x ** 2).backward()
print(x.grad)
(x ** 2).backward()
print(x.grad)
x.grad.zero_()
(x ** 2).backward()
print(x.grad)
```

输出依次为 `tensor(6.)`、`tensor(12.)`、`tensor(6.)`。第二次重新计算表达式生成新的计算图，梯度默认累加；zero_ 清空已有梯度。不能默认对同一个已释放的计算图直接重复 backward。

## 今日任务

1. 自定义浮点数 x，计算一个标量表达式 y，打印 y、执行 backward 并打印 x.grad；手算验证。
2. 两次重新计算同一表达式并 backward，观察梯度累积；清空后再算一次。
3. 解释 requires_grad、backward 与 x.grad 的关系；不要求今天自行实现优化器。

参考：[PyTorch 自动求导](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)。

## 完成情况

用户实现 x**x 的求导、梯度累积及清零；已实际运行验证，详情见 [当日记录](../records/day53-record.md)。
