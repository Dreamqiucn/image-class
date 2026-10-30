# Day 34：保存整理后的样本表与类别统计表

布置日期：2026-10-30。状态：核心完成。预计 45 至 60 分钟，接续 Day 33。核心学习代码由用户自己编写，AI 提供说明和排错，不代写完整流程。

## 今天的目标

把此前的 DataFrame、缺失处理、去重和类别统计连起来，保存两份可再次读取的 CSV：整理后的样本表，以及类别数量与占比统计表。重点是保存结果与检查文件，不要求重新做所有旧练习或修复扫描器。

## 当前环境与输入

Day 29 至 Day 33 已按记录完成。Day 31 的缺失处理和去重曾分别作用于原表，今天只在本次使用的表里把处理结果接起来；不要求回头改 Day 31。

当前 Mac 项目中没有 1/output/samples.csv，Mac 的 image-class-conda 环境也尚未安装 Pandas；此前 Pandas 验证记录来自 Windows。不要把 Windows 上已安装等同于 Mac 已安装，也不要要求用户先重新导出旧 CSV 才能开始。若继续在这台 Mac 学习，由用户在终端执行：

```bash
conda install -n image-class-conda pandas
```

该命令只作为安装说明，本次任务布置没有执行安装。已有可用 Pandas 的 Windows 环境可以直接学习。

## 练习数据

在 scripts/pandas_basics.py 中新增 day34，或自选文件。可以沿用自己的小样本；也可用下面五条练习记录。这些路径只是练习表中的字符串，不要求文件真实存在，不代表正式角色名单。

```python
rows = [
    {"path": "A/a.jpg", "label": "A"},
    {"path": "A/a.jpg", "label": "A"},
    {"path": "A/b.jpg", "label": None},
    {"path": "A/c.jpg", "label": "A"},
    {"path": "B/d.jpg", "label": "B"},
]
```

上面是输入数据，不产生终端输出。转成 DataFrame 并打印时，内容为：

```text
      path label
0  A/a.jpg     A
1  A/a.jpg     A
2  A/b.jpg   NaN
3  A/c.jpg     A
4  B/d.jpg     B
```

缺失值可能显示为 NaN、None 或 <NA>，取决于版本与 dtype；本题以 isna 的判断为准。

## 新用法一：to_csv 保存表格

DataFrame.to_csv 可以代替自己使用 csv.writer 逐行写表格。

```python
from pathlib import Path
import pandas as pd

example = pd.DataFrame({"label": ["A", "B"], "count": [2, 1]})
output_dir = Path("output/day34")
output_dir.mkdir(parents=True, exist_ok=True)
example.to_csv(output_dir / "example.csv", index=False, encoding="utf-8-sig")
```

to_csv 写入指定路径时不自动打印表格。此示例保存的 example.csv 内容为：

```csv
label,count
A,2
B,1
```

index=False 表示不把左边的行索引写成额外一列；不会删除表中的数据列。encoding="utf-8-sig" 用于兼顾中文 CSV 的读取。相对输出路径以终端当前工作目录为基准；从项目根目录运行即可。上面 example.csv 只是演示，不是必须额外交付的第三个文件。

## 新用法二：把计数结果整理成两列

value_counts 或 groupby.size 返回的 Series，标签通常在索引里。可使用 reset_index，把它们变成真正的列：

```python
counts = pd.Series([2, 1], index=["A", "B"], name="count")
counts.index.name = "label"
table = counts.reset_index()
print(table)
```

输出：

```text
  label  count
0     A      2
1     B      1
```

标签现在是 label 数据列，因此保存时使用 index=False 也不会把标签丢掉。可以使用其他自己理解的写法组织统计表，不强制套用这个示例。

## 自己实践

1. 创建或读取一个包含 path、label 的样本表。本次输入先去掉 path 或 label 缺失的行，再按 path 去重，把返回结果保存到同一个整理流程中。打印整理前后行数。不要只打印两次独立清洗的结果而继续使用原表。
2. 根据整理后的表，生成包含 label、count、ratio 的类别统计表。count 是该类样本数，ratio 是该类数量除以整理后的总数量，取 0 至 1 的小数即可。
3. 创建 output/day34 目录，分别保存 samples_clean.csv 与 class_stats.csv。两份文件都不带额外行索引，原始数据不用覆盖；类别统计应来自同一份整理后样本。
4. 用 read_csv 读回这两份文件，打印内容或行数，核对与内存中的结果一致。最后在聊天中写一两句实际发现，例如重复和缺失各去掉多少记录、哪个类别更多。无需额外写长报告。

若使用上述五条记录，预期整理后是三条：

```text
      path label
0  A/a.jpg     A
3  A/c.jpg     A
4  B/d.jpg     B
```

清理后内存表的索引可能不连续，这是正常情况；保存不带索引的 CSV 再读回后，默认索引会重新成为 0、1、2，无需为此增加重构。

类别统计应等价于：

```text
  label  count     ratio
0     A      2  0.666667
1     B      1  0.333333
```

输出排列、显示的小数位数可以不同，不必把 ratio 强制改成字符串百分比。这是这组练习数据的预期结果，不是用户已经运行出的成果。

## 验收与范围

- 两个 CSV 可以读回，没有额外的 Unnamed: 0 索引列。
- 样本表没有必要字段缺失及重复路径；不要求今天检查图像是否能打开、内容是否重复或路径是否真实存在。
- 统计表 count 总和等于整理后样本数；非空表的 ratio 总和应接近 1。
- 用户能说明统计来自清理后的表，及 index=False 的作用；结合实现和输出检查，不强制口头考试。
- 自选有效数据与等价实现可接受；本次选择非空小样本即可，不增加空数据报表、复杂冲突处理、merge/map 重做、绘图或训练任务。若用实际数据发现问题，按需要帮助处理，不扩大当天必做范围。

## 记录约定

结束后按实际代码、运行结果和用户决定统一整理 records/day34-record.md，再更新总进度；日内问答先在聊天中进行。不代改学习代码、Git 暂存、提交或推送，不自动打开任务文件，不提前创建 Day 35 任务。

## 收尾状态

2026-10-30 核心完成。用户自行新增 day34，串联 dropna 与按路径去重，通过两次 value_counts 分别取得数量与占比，组成 DataFrame 后 reset_index，保存 output/rows.csv 和 output/stats.csv，并用 csv.DictReader 读回统计表。counts 复数列名、实际文件名及 csv 模块读回均接受，不强制照模板改写。

Mac 的 image-class-conda 中实际确认 Pandas 3.1.0 可用。在独立临时目录准备 output 文件夹后运行原脚本，正常退出；验收额外读回两个 CSV，确认样本数为 3、A=2/B=1、占比总和接近 1，必要字段无缺失、路径不重复、无额外索引列。项目现有输出未覆盖。用户代码依赖 output 已存在，当前项目该目录存在；不把自动建目录记为已实现。

用户代码未打印清洗前后行数，未自行读回样本表或提交文字发现；不记作用户已完成这些展示步骤，按核心清洗、统计、保存和读回结果通过收尾，不机械追加。问答与工程操作见当日 records。下一学习日 Day 35 休息或可选复盘，之后 Day 36 进入 Matplotlib。
