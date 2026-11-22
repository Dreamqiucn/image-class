# Day 67：训练模式、验证模式与验证指标

布置日期：2026-11-22。状态：按用户调整的范围核心完成。预计 45–60 分钟。核心练习由用户自己编写，助手按需解释和检查。

## 今天的目标

在 Day 66 的 CNN 训练中接上独立的验证流程：训练时启用训练模式；每轮训练结束后，启用验证模式并在 no_grad 下遍历验证集，计算验证 loss 和正确率。

## 当前项目情况

- scripts/torch_weel10.py 的 day66 有训练样本、new_photo_list 和 val_loader，但尚未遍历验证集。
- 当前验证集仅一张图片 photos/汐见萤/shiomi3.png，训练列表三张图。路径不同不代表已做过图片内容去重；本次只用于理解流程，结果不能评价泛化。
- photo_process 默认 tran=1，会以 100% 概率水平翻转；验证 Dataset 应传入 tran=0，让验证不发生随机翻转。
- Mac 当前 torch 2.15.0 可用。今天可使用 CPU，不要求安装依赖或使用 GPU。

## 三个用法

1. layers.train() 设置训练模式；layers.eval() 设置验证模式。它们会影响 Dropout、BatchNorm 等对模式敏感的层。当前网络只有 Conv2d、ReLU、MaxPool2d、Flatten、Linear，切换模式通常不会让同一输入的输出发生变化。它们不会自动训练，也不会自动关闭梯度。
2. with torch.no_grad(): 让其代码块内通常不记录梯度，用于验证前向计算；它不会自动切换 eval 模式，也不会自行禁止用户显式调用 optimizer.step()。
3. 每轮先训练，接着独立验证。验证不调用 backward 或 optimizer.step；下一轮训练开始前重新调用 layers.train()，因为上一轮结束时模型处于 eval 模式。两套统计变量分开。

示意结构（只展示流程，不是可直接运行的完整答案）：

```python
for epoch in range(训练轮数):
    layers.train()
    # 遍历 train_loader，计算 loss 并更新参数

    layers.eval()
    with torch.no_grad():
        # 遍历 val_loader，前向计算及统计，不更新参数
        pass
```

代码示意没有 print，运行本片段本身不产生输出。训练与验证的每批 loss 默认是批内平均；要得到整轮平均，用每批 loss.item() 乘该批样本数累计，再除以该阶段实际样本总数。

## 自己实践

1. 在现有练习基础上新增 day67 或自选文件，沿用 Day 66 的网络、损失函数、优化器与训练循环。明确验证 DataLoader 使用独立的 new_photo_list，给验证 Dataset 传入 tran=0。
2. 每轮训练前调用 layers.train()；训练完成后调用 layers.eval()，在 with torch.no_grad() 内遍历 val_loader，计算 logits、loss、预测类别。
3. 分别累计验证的样本总数、正确数和按批次大小加权的 loss，计算验证平均 loss 与 accuracy=正确数/样本数。每轮打印训练和验证指标，正确数/总数也可一起显示。当前验证有一张图，accuracy 只能是 0 或 1，loss 不一定下降。
4. 检查训练与验证路径列表没有相同路径；这只能发现路径相同，不等同于内容查重。用自己的代码说明为什么验证时需要 eval 和 no_grad。

不要求今天画图、保存模型、训练正式数据或新增额外网络层。可以参考 [Module.eval 文档](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.eval) 与 [torch.no_grad 文档](https://docs.pytorch.org/docs/stable/generated/torch.no_grad.html)。

## 验收

- 训练流程仍能更新模型；每轮能独立运行验证，验证环节不调用 backward 或 optimizer.step。
- 验证 Dataset 不执行随机翻转；每个 epoch 开始调用 train，验证时调用 eval 和 no_grad。
- 验证平均 loss 按实际遍历样本加权，accuracy 基于实际正确数及样本数；训练与验证统计互不混用。
- 验证集仅一张图时，如实说明结果有限，不把指标当作正式模型表现。按实际运行和用户理解判断，不强制额外口头考试。

## 记录约定

用户结束后统一记录实际代码、运行与问答；不代写学习代码，不暂存、提交或推送，不提前创建 Day 68。

## 收尾状态

用户明确不要求计算 accuracy，以验证正确数为当前范围。用户在训练后使用 eval 和 no_grad，独立计算验证 loss 与正确数，验证 Dataset 使用 tran=0。Mac Conda Python 实际运行 20 轮正常，首轮验证 loss 约 0.0999、正确 1/1；末轮约 0.0035、正确 1/1，数值是随机训练的一次结果，非泛化结论。

验证 loss 按批样本数累计并除以 len(new_photo_list)，对于当前全部一张验证图、无丢弃批次正确；用户未按实际遍历数累计 total，未来更换采样或丢弃批次时需调整。路径字符串不同，但未执行内容去重；用户未单独实现路径检查，不记为已完成。未打印 accuracy 按用户要求接受。未改变用户学习代码或操作 Git。
