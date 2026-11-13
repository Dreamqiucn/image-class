# Day 54：nn.Module 与线性层

日期：2026-11-12 开始，2026-11-13 用户开始 Day 55，Day 54 结束。

- 用户自行编写继承 nn.Module 的两层网络，中间使用 ReLU，修正 forward 未返回计算结果的问题；分别输入两个一维样本，打印输出与权重、偏置形状。
- 在 image-class-conda 实际运行成功，两次输出 shape 都为 (2,)，fc1 的权重为 (4,3)、偏置为 (4,)；两个样本是分别调用，并非批处理。网络未训练，初始化值及输出会变化。
- 问答解释 model(x) 通过 Module 的调用机制执行 forward、init 和 forward 参数的分工、ReLU、权重和偏置、Linear 初始化范围及随机种子。
