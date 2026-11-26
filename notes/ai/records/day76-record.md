# Day 76 每日记录

日期：2026-11-26。主题：使用 NumPy、Pandas、Matplotlib 分析正式数据类别分布与图片样例。

用户自行编写 `scripts/analyze_dataset.py`，读取 `data/manifests/samples.csv`（4,507 行，29 个角色类别），完成以下内容：

1. **Pandas 统计**：使用 `df["label"].value_counts()` 统计 29 个角色各自样本数，并编写了宽高均值 `df["width"].mean()`、`df["height"].mean()` 与打印语句（验证后在脚本中注释保留）。
2. **角色数量分布柱状图**：创建 `(14, 6)` 画布，使用 `ax1.bar(counts.index, counts.values)` 绘制 29 类降序柱状图，通过 `plt.xticks(rotation=45, ha="right")` 与 `fig1.tight_layout()` 解决横轴中文角色名重叠与裁切问题，设置标题与坐标轴名称，保存为 `output/角色图片数目统计.png`。
3. **随机不同角色样例网格图**：使用 `df.groupby("class_id").sample(1).sample(4)` 每次随机抽取 4 个不同角色各 1 张图片，拼接 `"data/raw/" + row["path"]` 后用 Pillow 打开转 RGB 并转为 NumPy 数组 `r = np.array(rgb)`（脚本中编写了 `print(row["label"], r.shape, r.mean())`，验证后注释保留）；在 `(1, 4)` 子图网格中用 `imshow` 显示图片、顶部子图标题显示相对路径 `row["path"]`、通过 `set_xticks([])` 和 `set_yticks([])` 代替 `axis("off")` 保留横轴并在图片正下方用 `set_xlabel(f'{row["width"]} x {row["height"]}')` 显示宽高尺寸，使用 `fig2.suptitle("随机图片")` 添加总标题，保存为 `output/随机图片.png`。

独立核验 `output/角色图片数目统计.png` 与 `output/随机图片.png` 两张图片均已生成且画面正常：柱状图 29 个中文角色名、坐标轴、标题完整无裁切；随机样例图 4 个角色（本次为 `藤都子/0125.webp` `1280 x 626`、`高松灯/0079.png` `1334 x 1002`、`井芹仁菜/0070.png` `449 x 723`、`海老冢智/0189.png` `481 x 476`）的顶部路径标题、底部宽高尺寸和总标题均清晰显示，直观呈现了不同来源素材的长宽比差异。

当日问答涵盖：为什么要抽样展示真实图片（核验路径与标签对应、观察长宽比差异、准备项目展示素材）、分析画图脚本与数据划分脚本的职责分离、`df.sample(4)` 与 `df.groupby("class_id").sample(1).sample(4)` 随机抽样写法、`fig.suptitle` 与 `ax.set_title` 的区别，以及为什么 `set_xlabel` 需传入单个 `f"..."` 字符串且不能与 `axis("off")` 同时使用（改用 `set_xticks([])` / `set_yticks([])`）。

按当前范围核心完成，未代写核心学习代码，未操作 Git。下一学习日为 Day 77（第十周休息或可选复盘，若跳过则进入第 11 周 Day 78 残差块准备）。
