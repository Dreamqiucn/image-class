# Day 5：保存 CSV，处理无效路径

任务量约 60 分钟，不要求卡住实际耗时。今天不用安装新库。

## 今天的目标

把文件统计结果保存成 CSV；输入不存在的路径或文件路径时，给出清楚的提示。

现有流程：目录 → 后缀列表 → 统计字典 → 屏幕输出。今天增加保存到文件。

修改文件：C:\Users\24718\Desktop\image-class\scripts\count_file.py。

## 1. 认识 CSV 和文件写入（约 10 分钟）

CSV 是文本表格，一行对应一条记录，逗号分隔不同列。

```csv
suffix,count
.py,2
.md,3
无后缀,2
```

Python 自带 csv 模块。先理解这个写表头的小例子：

```python
import csv

with open("example.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["suffix", "count"])
```

- "w"：写入模式，文件不存在就创建，已存在就覆盖。
- encoding="utf-8-sig"：保存中文，也方便 Excel 识别编码。
- newline=""：让 csv 模块处理换行，避免 Windows 下出现多余空行。
- with：代码块结束后自动关闭文件，出错时也会关闭。
- csv.writer(file)：创建写入器。
- writer.writerow(...)：写入一行。

## 2. 增加保存函数（约 20 分钟）

自己补齐：

```python
def save_csv(counts, output_path):
    # 使用 output_path 打开文件
    # 写表头
    # 遍历 counts.items()，逐行写入
    ...
```

输入是统计字典和输出路径。函数负责保存，不要求返回数据。

主程序按这个顺序连接：

```python
counts = count_files(p, {".venv", ".git", "__pycache__"})
print_summary(counts)
save_csv(counts, Path("notes/file_counts.csv"))
```

从项目根目录运行，确保 notes 文件夹存在。先统计 scripts 目录，方便检查结果，也避免生成的 CSV 影响下一次统计。

## 3. 检查输入路径（约 20 分钟）

在 collect_suffixes() 遍历前，用 root.exists() 和 root.is_dir() 检查：

- 不存在：提示“路径不存在”。
- 是文件：提示“请输入目录路径”。
- 空目录：正常返回空列表，CSV 只有表头。

检查失败时可以主动抛出异常，例如：

```python
raise ValueError("路径不存在")
```

主程序自己补齐：

```python
try:
    # 统计、打印、保存
    ...
except ValueError as error:
    print(f"输入错误：{error}")
except OSError as error:
    print(f"文件操作失败：{error}")
```

ValueError 处理主动报告的路径问题；OSError 处理文件操作错误。统计失败后不要继续保存成功结果。

## 4. 验收与记录（约 10 分钟）

| 输入 | 应有结果 |
| --- | --- |
| scripts | 打印统计结果，生成内容对应的 CSV |
| 一个空目录 | 总数为 0，CSV 只有表头 |
| 一个不存在的路径 | 显示清楚的错误提示 |
| scripts/count_labels.py | 提示需要目录 |

理解检查：

1. 为什么 "w" 模式第二次运行不会保留旧结果？
2. 为什么统计和保存要放在同一个 try 里面？

每日任务保存在 notes/ai/daywork/dayn.md；AI 将每日学习情况与具体提问记在 notes/ai/records/，整个学习过程汇总到 notes/ai/progress_record.md。个人进度记录由你按需要写入 notes/progress.md；Git 提交与推送由你操作。
