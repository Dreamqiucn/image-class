# Day 69 每日记录

日期：2026-11-23。主题：模型参数保存、加载和预测。

用户在 scripts/torch_weel10.py 的 day68 末尾使用 torch.save(layers.state_dict(), "output/day68.pth")，同时添加 day69 函数，创建相同的 CNN 结构，用 torch.load(weights_only=True, map_location="cpu") 与 load_state_dict 加载权重，设置 eval 并在 no_grad 中预测。图像使用 RGB、64×64、转 Tensor、通道换序、除以 255，验证预处理的翻转概率为 0。

当前文件入口仅调用 day69，和训练定义在同一文件，但单独运行预测进程不会调用 day68 或进行训练；用户未新建单独脚本，也未单独打印类别编号，按实际预测功能接受当前范围。训练函数的保存操作位于 plt.show() 之后，交互式图窗未关闭时尚未执行保存。现有 output/day68.pth 存在，但本次未重新运行训练来独立核验其来源。

Mac Conda Python 实际运行 day69，正常退出。两张输入分别输出 logits 约 [-3.2405, 3.2495] 与 [-3.5352, 3.6106]，均映射为汐见萤。独立加载该权重，并核对模型 state_dict 中各项与文件字典完全相同；未对比训练模型保存前后的同一图片 logits。批次大小 2、逐图前向和输出路径对应均在当前两张图片与 shuffle=False 条件下实测有效。

用户字典还定义 2=GPT、3=DeepSeek，但模型最后的 Linear 输出只有两个分数，argmax 只能是 0 或 1；其他输入也会被归为两个已训练类别之一，不能说明模型学会 GPT 或未知类别识别。索引 i*batch_size+ii 依赖当前不打乱、按原顺序遍历；不对其他采样方式保证。

当日解释 map_location="cpu"、weights_only=True 对 state_dict 的含义；权重字典可包含 bias、缓冲区，不是只按名为 weight 的键过滤。回答 DataLoader 的 batch_size、逐图遍历与 unsqueeze、数字字典映射；用户学习核心代码由其自行编写。

按当前范围核心完成，未伪造指标、未代改核心学习代码或操作 Git。下一学习日 Day 70 休息或可选复盘，等待用户要求开始。
