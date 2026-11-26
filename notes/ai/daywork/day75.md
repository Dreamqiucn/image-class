# Day 75：按分组划分训练、验证与测试集

布置日期：2026-11-26。状态：按当前范围核心完成。预计 45–60 分钟。核心代码由用户自行编写；助手按需解释与验收。

## 今天的目标

编写脚本读取整理后的样本总表 `data/manifests/samples.csv`，按 `class_id` 分层、按 `group_id` 分组，划分并保存固定的训练、验证与测试清单（`data/manifests/train.csv`、`data/manifests/val.csv`、`data/manifests/test.csv`），保证同一原图或同源镜头变体不会跨集合泄露，并在后续训练和调参期间严格隔离测试集。

## 输入数据现状

已核对本机 `data/manifests/samples.csv`：

- 字段：`path, class_id, label, work, width, height, sha256, group_id, exclude_from_train, exclude_reason`
- 规模：共 **4,507** 张图片、**29** 个类别（`class_id` 0–28）、**4,407** 个独立 `group_id`；当前所有样本 `exclude_from_train == 0`（代码中仍建议显式过滤一次，养成防御性习惯）
- 同源组情况：共 **90** 个多图分组（包含 **190** 张图片，单组最多 **6** 张），**0** 个跨类别分组
- 各类别分组数范围：最少 **66** 组（`deepseek娘`，71 张图），最多 **200** 组（`千早爱音`，200 张图）

## 核心思路与避坑点

1. **为什么要按 `group_id` 划分，而不是直接对行随机打乱？**
   同一个 `group_id` 里可能装着同一镜头截帧、原图裁剪或轻微变体。如果直接按图片行随机切分，同一原图的相似变体就会同时出现在 `train` 和 `val`/`test` 里，导致验证/测试分数虚高（数据泄露），无法反映面对全新图片时的真实泛化能力。
2. **为什么要先按 `class_id` 分层，再对每类内部的 `group_id` 划分？**
   本数据集最小类只有 66 组，最大类有 200 组。如果把 4,407 个组混在一起全局随机切分，小类可能在 `val` 或 `test` 中数量过少甚至波动很大；先按 `class_id` 分层，再在每个类别内部各自切分 `group_id`，才能保证每个角色在三个集合里都有稳定比例。
3. **划分比例怎么选？**
   推荐 **`70% / 15% / 15%`**（最小类 66 组约分得 `46 / 10 / 10` 组，验证集和测试集每类样本更有代表性）；也可以选 **`80% / 10% / 10%`**（约 `53 / 7 / 6` 组，留给训练稍多几张）。确定一个比例并写死在脚本里即可。
4. **常见避坑点：**
   - **按组划完后，各集合的实际“图片张数”比例会略微偏离组数比例**：因为多图分组必须整组移动，不可拆开一个 `group_id`。不要为了凑整张数而破坏分组完整。
   - **保证严格可复现**：遍历 `class_id` 前先排序（如升序），在每个类别内取出唯一 `group_id` 后先 `np.sort(...)` 再传给 `rng.permutation(...)`，最后用整数切片：先算 `n_val = int(n * val_ratio)`、`n_test = int(n * test_ratio)`、`n_train = n - n_val - n_test`，避免舍入漏掉或重复分组。

## 几个关键用法小提示

```python
# 固定随机种子并打乱排序后的 group_id
rng = np.random.default_rng(42)
shuffled_groups = rng.permutation(np.sort(groups))

# 按 group_id 集合把原表对应行筛选出来
train_part = sub_df[sub_df["group_id"].isin(train_groups)]

# 保存固定清单（UTF-8 BOM，不写入多余索引列）
train_df.to_csv("data/manifests/train.csv", index=False, encoding="utf-8-sig")
```

此片段不完整，变量 `groups`、`sub_df`、`train_groups`、`train_df` 需自行构建，直接运行不会产生预期输出。

## 自己实践

建议新建脚本（例如 `scripts/split_dataset.py`），自己完成以下 5 步：

1. **读取与过滤**：读取 `data/manifests/samples.csv`，过滤 `exclude_from_train == 0`，打印并确认可用总样本数（4,507）与类别数（29）。
2. **按类分组切分**：按升序遍历每个 `class_id`，提取该类去重并排序后的 `group_id` 列表，使用固定随机种子（如 `42`）打乱后按选定比例（推荐 `70% / 15% / 15%`，或 `80% / 10% / 10%`）切分成三组 `group_id`，再筛选原表对应行分别拼接得到 `train_df`、`val_df`、`test_df`。
3. **保存固定清单**：输出 `data/manifests/train.csv`、`data/manifests/val.csv`、`data/manifests/test.csv`（`index=False`、`encoding="utf-8-sig"`），保持 `path` 为相对于 `data/raw` 的相对路径，不要硬编码本机或 Windows 绝对路径。当前 `.gitignore` 已放行 `data/manifests/`，之后你可由 Git 同步这几份清单到 Windows 端，保证两端划法完全一致。
4. **编写程序自检**：在脚本里用 `assert` 和汇总打印验证：
   - 行数守恒：`len(train) + len(val) + len(test) == len(usable_df)`；
   - 两两零重叠：三份清单在 `path`、`group_id` 和 `sha256` 上交集均为空；
   - 类别全覆盖：三份清单均完整包含全部 29 个类别；
   - 打印每个类别的 `train / val / test` 数量对照表，重点检查样本较少类别（`deepseek娘`、`claude娘`、`gpt娘`、`纯田真奈`）。
5. **复现检查与隔离约定**：连续运行脚本两次，确认输出结果完全一致；清单确定后把 `test.csv` 封存，后续训练调参和选模型只看 `train.csv` 与 `val.csv`，最终定版评估才用 `test.csv`。

今天暂不做 Day 76 的分布图表绘制，也不涉及 PyTorch `Dataset` 或模型训练代码。

## 验收

- 能清楚解释两点：为什么按 `group_id` 而不是按图片行随机划分，以及为什么后续调参期间要隔离 `test.csv`。
- 独立脚本运行后成功生成 `data/manifests/train.csv`、`data/manifests/val.csv`、`data/manifests/test.csv`，且保留原始相对路径与完整字段。
- 代码中的 `assert` 检查全部通过：总行数守恒、`path` / `group_id` / `sha256` 跨集合零交集、29 类齐全、小类在验证集和测试集均有合理样本量。
- 相同随机种子下两次运行结果一致。

## 记录约定

用户结束后按实际代码、输出和问答统一记录；不代写核心学习代码，不暂存、提交或推送，不提前开始 Day 76。

## 收尾状态

用户自行编写 `scripts/split_dataset.py` 并运行生成 `data/manifests/train_csv.csv`（3,187 行）、`data/manifests/val_csv.csv`（659 行）、`data/manifests/test_csv.csv`（661 行），合计 4,507 行。脚本实现 `exclude_from_train == 0` 过滤、固定随机种子 `42`、按 `class_id` 升序遍历、类内唯一 `group_id` 排序后打乱及 `70% / 15% / 15%` 切片、列表收集与 `pd.concat(..., ignore_index=True)` 合并，并编写了总数守恒、`group_id` 交集为空和 29 类覆盖的 `assert` 检查（检验后在代码中注释保留）。独立核验 `path`、`group_id`、`sha256` 跨集合零重叠，29 类在三个集合均有覆盖，重复运行文件哈希完全一致。文件名采用 `train_csv.csv` / `val_csv.csv` / `test_csv.csv`，未在脚本内打印每类对照表，按实际功能接受当前范围；后续读取时对应使用该文件名即可。详情见 [records/day75-record.md](../records/day75-record.md)。
