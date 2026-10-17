# Day 15：argparse 命令行参数

日期：2026-10-17。第三周仍以 Python 工具整合为主，按总体路线第四周再进入数据分析。本日约 60 分钟任务量，不限制实际耗时。核心代码由用户编写。

## 目标与最终用法（约 10 分钟）

沿用 scripts/export_samples.py，把主入口中 input 询问路径改为 argparse 解析命令行参数。运行时直接给扫描根目录，允许通过 --output 指定完整 CSV 文件路径。继续保留收集一次、保存、实际读回和类别统计的流程。

以下命令从项目根目录 C:/Users/24718/Desktop/image-class 的已激活 .venv 终端运行：

```powershell
python scripts/export_samples.py sample_images
python scripts/export_samples.py sample_images --output output/custom_samples.csv
python scripts/export_samples.py --help
```

这里 sample_images 是位置参数 root；--output 是可选参数，后面需要一个输出文件路径；不指定时默认保存到扫描根目录的 output/samples.csv。自定义示例则保存在项目根目录的 output/custom_samples.csv，两者是有意不同的目标位置。

路径带空格时用引号包起来，例如 "C:/数据/图片 样本"。相对路径以运行命令时的工作目录为基准，不自动相对于脚本所在目录。

## 1. 理解解析过程（约 10 分钟）

argparse 是 Python 标准库，无需安装。它读取命令行参数，依据你定义的规则转换并检查，默认提供 -h/--help。比手动按 sys.argv 下标取值更方便处理选项与帮助文本。

核心写法示例：

```python
import argparse

parser = argparse.ArgumentParser(description="导出图片路径与类别")
parser.add_argument("root", type=Path, help="图片数据根目录")
parser.add_argument("--output", type=Path, help="输出 CSV 文件路径")
args = parser.parse_args()
```

Path 沿用脚本已有导入：type=Path 传的是用于转换的类，不是先调用 Path()。解析后 args.root 是 Path 对象；不提供 --output 时 args.output 默认是 None，提供时是 Path 对象。Path 转换本身不检查文件夹是否存在，继续由扫描器初始化检查。

理解两种参数：root 必须给，位置参数在这里仅需一个目录；--output 可以不写，但写了这个选项就必须跟一个路径值。

## 2. 接入已有脚本（约 25 分钟）

只改现有入口与必要的文件路径传递，不重写扫描器或 CSV 计数逻辑：

1. 在 __main__ 中或 main() 内定义 parser、添加参数并调用 parse_args；不要在模块顶层解析，使导入仍无副作用。
2. 用 args.root 作为扫描目录；不再要求用户先启动程序再 input 路径。
3. 确定一个实际的 csv_path：提供 args.output 就使用它，否则使用扫描目录 / "output" / "samples.csv"。可用 if/else 明确表达。
4. 让 save_samples(samples, csv_path) 与 read_samples(csv_path) 使用同一完整 CSV 路径，避免自定义输出后仍读取旧默认文件。
5. 保存时用 csv_path.parent.mkdir(parents=True, exist_ok=True) 建立输出父目录，open 直接使用 csv_path。打印也使用这个实际路径的 resolve()。
6. 继续只收集一次样本；写入表头 path,label，读回后打印数量与类别统计。read_samples 可以沿用内部计数打印，不要求先完成 Day 14 的可选双返回值重构。
7. 用户于本日明确调整范围：不要求新增 try/except，也不要求交互重试界面。argparse 自己处理缺参数等命令格式错误；目录不存在等运行错误可保留原异常，不以友好错误提示阻塞本日验收。

只给提示与接口，核心整合由用户完成；同等功能的自主组织方式可接受。

## 3. 有意义的验收（约 15 分钟）

- --help 显示 root、--output 和说明，且不扫描或创建 CSV。
- 默认命令对 sample_images 生成其 output/samples.csv，实际读回 3 条、cat: 2、dog: 1。
- 自定义 --output 生成指定文件，并确实读回这一份；输出成功提示与实际文件位置一致。新目标的父目录不存在时能创建。
- 缺少 root 时由 argparse 提示缺参数。按用户调整后的范围，不额外要求无效扫描目录的 try/except 提示。
- 依然按后缀识别图片，不解码占位文件；空目录等已在 Day 13 验证过的行为只在新改动可能影响时针对性检查，不机械重复全套。

理解问题：
1. args.root 与 args.output 来自哪里，为什么前者必须给？
2. type=Path 做了什么，它能保证目录存在吗？
3. 为什么保存和读取都要接收同一个 csv_path？

## 记录时机

本日开始仅保存任务，尚未实现或验收。不创建 records/day15-record.md，也不提前写本日成果到 progress_record.md。日内先在聊天中答疑，完成后统一记录，不自动 Git 暂存、提交或推送。

官方参考：https://docs.python.org/zh-cn/3.12/howto/argparse.html 。

## 收尾状态：2026-10-17

按用户调整后的范围完成，不要求新增 try/except。实际帮助、默认输出、自定义多层目标目录创建和读回统计通过；保存函数返回最终文件路径，读取函数已使用同名形参，模块中没有全局 csv_path 时独立传参读取也通过。缺少 root 由 argparse 提示，退出码 2。详细过程与问答见 records/day15-record.md。未代改核心代码或进行 Git 提交。
