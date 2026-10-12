# Day 6：换目录运行，验收文件统计工具

日期：2026-10-12。任务量约 60 分钟，不限制实际耗时。

## 今天的目标

让工具在不同工作目录下运行，输入错误后能重新选择要统计的目录，并写出简短使用说明。今天沿用已有代码，不安装新库。

修改文件：C:/Users/24718/Desktop/image-class/scripts/count_file.py。
使用说明：C:/Users/24718/Desktop/image-class/README.md。

## 1. 把路径检查放到统计之前（约 20 分钟）

当前主程序先调用 count_files，再由 save_csv 检查路径。保存时重新输入目录不会重新计算 counts。

目标流程：获取输入 → 检查并重新询问直到目录有效 → 统计一次 → 打印 → 保存。

自己写一个函数：

```python
def ask_directory(p):
    # 路径不存在：提示并重新输入
    # 路径是文件：提示并重新输入
    # 目录有效：返回这个 Path 对象
    ...
```

可以用昨天的递归，也可以用 while True。注意 input 返回字符串，要转换成 Path；调用函数得到的有效路径需要接收回来。

主程序按下面的结构连接：

```python
p = ask_directory(p)
counts = count_files(p, excluded)
print_summary(counts)
save_csv(counts, p)
```

只调用一次 count_files。将保存函数中的重新询问逻辑移到 ask_directory；save_csv 负责使用已确认的目录保存。

在 excluded 中加入 "output"，避免下一次扫描把自己生成的 CSV 统计进去。当前规则会排除路径中所有名为 output 的目录，今天将其约定为结果目录。

## 2. 用一个小目录验收（约 15 分钟）

自己创建 C:/Users/24718/Desktop/day6-test：

```text
day6-test/
├── a.py
├── b.txt
└── sub/
    └── c.txt
```

这三个文件可以为空。运行工具并传入该目录，期望：

```text
.py: 1
.txt: 2
总文件数: 3
```

CSV 应保存在 C:/Users/24718/Desktop/day6-test/output/suffixes.csv，表头为“后缀,数目”，统计行与屏幕结果一致；行顺序不作要求。

连续运行两次，仍应是三个文件；生成的 output/suffixes.csv 不应被计入。

再验证：
- 先输入不存在的路径，再输入有效目录：最终统计有效目录中的三个文件。
- 先输入 a.py 的文件路径，再输入有效目录：提示需要目录，然后正常统计。

## 3. 从另一个目录运行（约 15 分钟）

在 PowerShell 中执行：

```powershell
Set-Location C:\Users\24718\Downloads
& "C:\Users\24718\Desktop\image-class\.venv\Scripts\python.exe" "C:\Users\24718\Desktop\image-class\scripts\count_file.py" "C:\Users\24718\Desktop\day6-test"
```

& 用来执行引号中的程序路径。这条命令直接使用项目虚拟环境里的 Python，不需要再次激活环境。

验证仍统计三个文件，CSV 仍在 day6-test/output 下。

区分三个位置：
- 工作目录：这次是 Downloads，Path(".") 指这里。
- 脚本位置：image-class/scripts/count_file.py。
- 输入目录：day6-test，来自传入的参数。

相对输入路径按工作目录解释；使用完整路径时，不依赖当前工作目录在哪里。

## 4. 写使用说明并检查理解（约 10 分钟）

自己在项目 README.md 写清楚：
1. 工具做什么：递归统计文件后缀并导出 CSV。
2. 怎么运行：写出一条你实际成功执行的命令。
3. 输出位置：输入目录的 output/suffixes.csv。
4. 排除目录：.venv、.git、__pycache__、output。

理解检查：
- 为什么主程序要接收 ask_directory 的返回值？
- 切换到 Downloads 后，Path(".") 指哪个目录？
- 为什么第二次运行时要排除 output？

完成标准：路径错误时在统计前重试；统计只调用一次；同一测试目录运行两次结果稳定；换工作目录运行成功；README 中的命令与输出说明符合实际。

任务保存到 notes/ai/daywork/day6.md。每日问题和解释只写 records/day6-record.md；总进度仅记录学习目标、实践、完成情况与验证结果。Git 提交与推送由用户自行操作。

当前状态：任务已布置，用户尚未提交今日实现或运行结果，不标记完成。

