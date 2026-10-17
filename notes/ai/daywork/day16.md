# Day 16：JSON 配置读取与汇总保存

日期：2026-10-17。约 60 分钟任务量，不限制实际耗时。沿用 scripts/export_samples.py 与已完成的 argparse、CSV 保存和读回流程。核心代码和练习配置由用户编写。

## 今天的目标

把 included、excluded 从代码里的固定集合移到 JSON 配置文件；实际读取配置参与扫描；将读回 CSV 得到的数量和类别统计保存成 summary.json。

本日不安装依赖、不读取真实图片、不训练模型，也不额外要求 try/except 或重试界面。日内先聊天，结束后才统一写学习记录。

## 1. 理解 JSON 与 Python 数据（约 10 分钟）

JSON 是文本数据格式，常用于配置与结果交换；不是 Python 源代码。其对象与数组读取后通常对应字典与列表：

```json
{
  "excluded": [".venv", ".git", "__pycache__", "output"],
  "included": [".jpg", ".png", ".jpeg", ".webp"]
}
```

这个示例读回后，最外层是 dict，config["included"] 是 list。JSON 键和字符串使用双引号，本日配置不要写注释或末尾多余逗号；数组用 []，不使用 Python 的集合写法。

两个新操作：

```python
import json

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)
```

json.load 接收打开的文件，解析并返回 Python 数据，不是返回文件路径。保存则用 json.dump(数据, 打开的文件)。不要把 load/dump 与处理字符串的 loads/dumps 混在一起，本日先掌握文件版本。

## 2. 配置真正接入扫描（约 20 分钟）

在项目中自行建立 config/scanner.json，即 C:/Users/24718/Desktop/image-class/config/scanner.json，使用上面的配置内容。

可新增 load_config(config_path) 普通函数，读取并返回配置字典。给现有 argparse 增加可选 --config：

```python
parser.add_argument(
    "--config",
    type=Path,
    default=Path("config/scanner.json"),
    help="扫描配置 JSON 路径",
)
```

这个相对默认路径以运行命令时的工作目录为基准。本日从项目根目录运行；需要换工作目录时，可以显式传入配置文件的完整路径，不要求增加自动路径定位功能。

主程序读取 args.config，把配置内容作为扫描器的实际输入。例如：

```python
excluded = set(config["excluded"])
included = set(config["included"])
```

随后继续使用 Imagesacnner(p, excluded, included)。集合转换沿用原接口；若用户直接使用列表且成员判断与功能正确，不以转换形式阻塞验收。关键是确实使用 JSON 配置，不要仅打印配置、实际仍使用旧固定集合。

保留 root 和 --output 的原有功能；根目录与输出位置继续由命令行决定，不再在 JSON 中增加同名设置，避免本日引入多套配置优先级。

## 3. 将读回统计写成 JSON（约 20 分钟）

建议让 read_samples 在保留读取和计数逻辑后返回 rows, counts；主程序接收结果，继续打印数量和统计，再组织汇总字典。这样结果可同时用于展示与保存，不需要重新扫描目录。

这是对之前可选双返回值练习的实际应用；如果采用同样能复用读回统计的其他组织方式，也可接受，不强制照某种函数模板。

汇总建议包含：

```python
summary = {
    "root": str(p.resolve()),
    "csv_path": str(csv_path.resolve()),
    "total": len(rows),
    "counts": counts,
}
```

文件位置使用 CSV 实际路径的同级：

```python
summary_path = csv_path.parent / "summary.json"
```

因此自定义 CSV 输出位置时，summary 也跟到那个目录。写入提示：

```python
with open(summary_path, "w", encoding="utf-8") as file:
    json.dump(summary, file, ensure_ascii=False, indent=2)
```

ensure_ascii=False 使中文等非 ASCII 字符原样输出；indent=2 让每层缩进两格便于阅读。只对整个汇总字典 dump 一次，不逐行拼 JSON、不连续追加多个 JSON 对象。

Path 与 set 不能直接按本日默认方式写进 JSON；路径先 str，集合若需要保存则转 list。本日 summary 的路径字符串、数字和计数字典可直接保存。

## 4. 有意义的验收（约 10 分钟）

当前项目样本目录已是 1，示例命令从项目根目录、已激活 .venv 的终端运行：

```powershell
python scripts/export_samples.py 1 --config config/scanner.json
```

- 默认配置读取后，原样本得到三条、cat: 2、dog: 1。summary.json 的 total 与 counts 和实际读回结果一致，root 与 csv_path 对应实际位置。
- 将配置的 included 暂时改为只有 [".jpg"]，再运行应只计 a.jpg，得到一条、cat: 1；大写 PNG 和 JPEG 不再计入。这个变式确认配置确实参与扫描，不仅是成功读取了文件。验收后可以恢复常用配置。
- 自定义 --output 时，CSV 与 summary 在同一目标目录；各字段、计数仍正确。既有扫描和输出目录排除规则保持。
- 空样本汇总应为 total: 0、counts: {}；只在与新 JSON 逻辑有关的范围针对性核对，不机械重测全部旧功能。
- summary 可用 json.load 再读回，核对内容与预期一致；不只看终端打印“成功”。

理解两个关键点：JSON 文件中的数组读回后是什么类型；为什么 summary 中的路径需要 str，以及为什么从读回结果生成汇总。

## 记录与边界

本日仅布置，尚未实现或验收。任务在开始时保存，不创建 records/day16-record.md 或提前更新本日完成进度；结束时统一整理问答和实测证据。核心学习代码由用户实现，不自动暂存、提交或推送 Git，不自动生成配置或新脚本替用户完成练习。

官方参考：https://docs.python.org/zh-cn/3.12/library/json.html 。

## 收尾状态：2026-10-17

核心任务完成。实际配置读入并控制扫描，CSV 只读取一次，复用 rows/counts 生成同级 summary.json，路径使用 as_posix。独立默认配置为三条、cat: 2、dog: 1；仅含 .jpg 的配置加自定义多层目标路径为一条、cat: 1；空目录为 total: 0、counts: {}。独立读回 CSV 和 JSON，数量、类别、根路径与输出路径一致，统计仅打印一次，脚本均正常退出。本日使用 utf-8-sig 写入与读回 JSON，接受自主组织方式；过程与问答已统一保存到 records/day16-record.md，未代改核心代码或执行 Git 提交。
