# Day 76：用三大库分析正式数据的类别分布与图片样例

布置日期：2026-11-26。状态：按当前范围核心完成。预计 45–60 分钟。核心代码由用户自行编写；助手按需解释与验收。

## 今天的目标

串联 **Pandas、NumPy、Matplotlib（配合 Pillow）**，对正式动漫数据集（`data/manifests/samples.csv` 或已划分的 `train_csv.csv` / `val_csv.csv` / `test_csv.csv`）做一次真实的数据分析，并把生成的两张核心图表保存到 `output/` 目录（以后写项目报告或展示时也能直接用）：

1. **图表一（Pandas + Matplotlib）**：29 个角色的样本数量分布柱状图（保存到 `output/day76_class_counts.png`）。
2. **图表二（Pillow + NumPy + Matplotlib）**：抽取若干张真实角色图片（如 4 张或 6 张不同角色），用 NumPy 查看/统计图片像素数组（如形状 `shape` 或像素均值 `mean`），并画成带角色名标题的图片网格（保存到 `output/day76_sample_grid.png`）。

## 几个关键用法小提示

你之前在 `scripts/matplotlib_basics.py` 里已经用过 `ax.bar`、`imshow`、`subplots` 和中文字体设置。今天在正式数据上会用到下面几个小技巧：

```python
# 1. Pandas：按角色统计图片张数（按张数从多到少排，或按 class_id 排）
counts = df["label"].value_counts()
# counts.index 是角色名列表，counts.values 是对应的张数

# 2. Matplotlib：29 个角色名字较多时，画布设宽一点，横坐标文字斜着放防重叠
fig, ax = plt.subplots(figsize=(14, 6))
ax.bar(counts.index, counts.values)
plt.xticks(rotation=45, ha="right")
fig.tight_layout()  # 自动留出底部文字空间，防止保存图片时角色名被裁掉

# 3. Pillow + NumPy：读正式图片（注意 CSV 里的 path 是相对于 data/raw/ 的！）
full_path = "data/raw/" + row["path"]
with Image.open(full_path) as img:
    arr = np.array(img.convert("RGB"))
    # arr.shape 是 (高, 宽, 3)，arr.mean() 是整张图的平均像素亮度(0~255)
```

此片段不完整，变量 `df`、`row` 需要先在脚本中读取，且记得加上你在 `matplotlib_basics.py` 开头写过的两行中文字体设置（`plt.rcParams["font.sans-serif"]` 和 `axes.unicode_minus`）。

## 自己实践

可以新建 `scripts/analyze_dataset.py`（或在你顺手的脚本里编写），完成以下 3 步：

1. **用 Pandas 统计并打印正式数据概况**：
   - 读取 `data/manifests/samples.csv`（也可以同时读 `train_csv.csv`、`val_csv.csv`、`test_csv.csv`）；
   - 打印总样本数、29 个角色各自的图片数量（可以用 `value_counts()` 或 `groupby`），以及整表图片宽高（`width`、`height` 列）的平均值或最大/最小值。
2. **画第一张图：29 个角色的样本数量柱状图**：
   - 用 `plt.subplots(figsize=(14, 6))` 创建较宽的画布，用 `ax.bar(...)`（或横向柱状图 `ax.barh(...)`）画出 29 个角色的样本数；
   - 设置标题（`set_title`）、坐标轴标签（`set_xlabel` / `set_ylabel`），调用 `fig.tight_layout()` 后保存为 `output/day76_class_counts.png`。
3. **画第二张图：用 NumPy 分析真实图片并绘制样例网格**：
   - 从表里挑出 4 张（`2×2`）或 6 张（`2×3`）不同角色的图片行（例如用 `df.groupby("class_id").first().head(6)` 取前 6 个角色各第 1 张图）；
   - 循环读取 `"data/raw/" + path`，转成 RGB 的 NumPy 数组 `arr = np.array(...)`，打印每张图的 `arr.shape` 和像素均值 `arr.mean()`（保留 1~2 位小数）；
   - 把这几张图画在 `plt.subplots(2, 3, figsize=(10, 7))`（或 `1×4` / `2×2`）的子图网格里，每格标题写上角色名（也可以顺手把像素均值或尺寸写进标题），关掉坐标轴刻度 `axis("off")`，保存为 `output/day76_sample_grid.png`。

## 验收

- 脚本在 Mac 上独立运行通过，终端输出了类别数量统计以及抽样图片的 NumPy 数组信息（`shape` 或 `mean`）。
- 成功在 `output/` 下生成两张图片：
  1. 29 个角色样本分布柱状图（中文角色名清晰可读、未被裁切，带标题与坐标轴说明）；
  2. 至少 4 张真实角色图片的样例网格图（每张子图带角色标签，画面正常显示）。

## 记录约定

用户结束后按实际代码、输出和问答统一记录；不代写核心学习代码，不暂存、提交或推送，不提前开始 Day 77。

## 收尾状态

用户自行编写 `scripts/analyze_dataset.py` 并运行生成 `output/角色图片数目统计.png` 与 `output/随机图片.png`。脚本实现 `value_counts()` 统计、宽高均值与数组 `shape`/`mean` 检查（打印语句验证后注释保留）、29 类旋转标签柱状图，以及 `df.groupby("class_id").sample(1).sample(4)` 随机抽取 4 个不同角色绘制 `(1, 4)` 网格图（含 `suptitle` 总标题、子图路径标题与下方 `宽 x 高` 标签）。独立查看两张输出 PNG 均排版正常、中文清晰无裁切。输出文件名采用中文名，按实际功能接受当前范围。详情见 [records/day76-record.md](../records/day76-record.md)。
