# Day 75 每日记录

日期：2026-11-26。主题：按分组分层划分训练、验证与测试集。

用户自行编写 `scripts/split_dataset.py`，读取 `data/manifests/samples.csv`（4,507 行，29 个类别，4,407 个独立 `group_id`），先筛选 `exclude_from_train == 0`，再使用 `np.random.default_rng(42)`、按 `sorted(df["class_id"].unique())` 依次遍历每个类别，对类内 `sorted(sub_df["group_id"].unique())` 随机打乱，按 `70% / 15% / 15%`（`n_val = int(len(group_id) * 0.15)`、`n_test = int(len(group_id) * 0.15)`、`n_train = len(group_id) - n_val - n_test`）切分 `group_id`，通过 `sub_df[sub_df["group_id"].isin(...)]` 筛回对应行并存入列表，最后在循环外 `pd.concat(..., ignore_index=True)` 合并并导出为 UTF-8 BOM 编码的 `data/manifests/train_csv.csv`、`data/manifests/val_csv.csv`、`data/manifests/test_csv.csv`。

用户在脚本中编写了总行数、`group_id` 两两交集为空、三集合类别数等于 29 的 `assert` 检查（检验通过后在文件中注释保留），未在脚本中单独打印每类数量对照表。Mac Conda Python 实际运行 `scripts/split_dataset.py` 正常退出，独立核验生成结果：
- 样本数：`train_csv.csv` **3,187** 行、`val_csv.csv` **659** 行、`test_csv.csv` **661** 行，合计 **4,507** 行（无遗漏或重复）。
- 零泄露检验：三份清单在 `path`、`group_id`、`sha256` 上的两两交集均为空集。
- 类别覆盖：三份清单均包含全部 29 个类别；样本较少类别分布合理（`deepseek娘` 51/11/9，`claude娘` 55/11/11，`gpt娘` 55/11/11，`纯田真奈` 65/13/13）。
- 可复现性：重复运行 `scripts/split_dataset.py`，三份 CSV 的 SHA-256 前缀保持一致（`e4df91f890522281`、`525df4244c2236a2`、`6670a3aba2b19e42`）。

当日问答与解释涵盖：为什么要按 `group_id` 整组划分并按 `class_id` 分层、测试集隔离原因、`exclude_from_train == 0` 作为软删除开关的作用、`df`（DataFrame）命名习惯、`sorted(df["class_id"].unique())` 去重与固定随机序列顺序的关系、`sub_df[sub_df["group_id"].isin(...)]` 外层筛选与布尔 Series 的区别、为什么 `.isin` 筛选后保留原表图片编号顺序但实际已完成随机抽样（通过跳号验证），以及为什么循环内用列表 `.append` 收集、循环外用 `pd.concat` 一次性拼接。

按当前范围核心完成，未代写核心学习代码，未操作 Git。下一学习日为 Day 76：使用 NumPy、Pandas、Matplotlib 分析正式数据集类别分布与样例并保存图表。
