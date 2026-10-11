# 第 1 天完整记录（AI 整理版）

这是第 1 天的历史记录，内容保留当时的检查与判断；未经后续验证的判断不应当作当前事实。
2026-10-11 更新：用户允许 AI 记录进入 Git，并将每日记录统一放在 `notes/ai/records/`。原来的“不进 Git”约定已取消。
`../../progress.md` 是本人的简版记录。

日期：2026-10-09

## 环境实测

```
python --version    Python 3.12.10
py -0p              只有 -V:3.12  C:\Users\24718\AppData\Local\Programs\Python\Python312\python.exe
where.exe python    真解释器 + C:\Users\24718\AppData\Local\Microsoft\WindowsApps\python.exe（商店占位程序）
git --version       git version 2.47.1.windows.2
conda --version     未安装
uv --version        未安装
nvidia-smi          NVIDIA GeForce RTX 5070 Ti Laptop GPU / 12227 MiB / 驱动 616.92 / CUDA UMD 13.4
```

结论：环境管理用 venv，`py -3.12 -m venv .venv`。避免直接写 `python`，可能命中商店占位程序。

显存是 12 GB，不是 32 GB（32 GB 指内存）。Blackwell 架构，装 PyTorch 时必须选支持它的版本 + CUDA 12.8 以上。

## 结构

- `image-classifier` 子目录已删除（原计划的嵌套结构），改名为 `image-class`，`.venv` 移到仓库根目录
- `.gitignore` 有 1 处问题：原本写的是 `.venv\`（反斜杠），Mac 上不生效，后来本人自己改成 `.venv/`
- `.gitignore` 行尾全是 LF，无 CRLF 混用

## 遇到并解决的问题

1. `where.exe python` 会返回商店占位程序 → 用 `py -3.12`
2. 终端未激活 venv 时跑 pip，实际用的是全局解释器 → 用 `.\.venv\Scripts\python.exe` 全路径
3. 残留 pip 进程持有目录句柄，导致改名失败 → 结束进程后成功
4. 改名后 VS Code 侧边栏显示过期内容（缺 `notes`、`data`）→ Reload Window 解决
5. `explorer.excludeGitIgnore: true` 导致所有被忽略的文件都不显示 → 改为 false，并在 `files.exclude` 里单独挡住 `.venv`

## Git

- 身份：Dreamqiucn / 2471822525@qq.com
- 远程：https://github.com/Dreamqiucn/image-class.git
- 提交：27bf15a "day 1"，4 个文件，已推送

## Python 基础诊断结论

题目：字典取值 / 统计类别次数 / 写一个拼接字符串的函数 / 是否写过文件读写。

- 第 1 题对：能认出字典，知道它类同 JS 的 Object
- 第 2 题错：把"统计出现次数"答成了异常处理的 `catch`，还没建立"字典做计数"的直觉
- 第 3 题思路对、语法错：写成 `def x(a){return ("你好"+a) }`，把 JS 的花括号混进了 Python
- 第 4 题：从未写过文件读写

→ 按"编程概念有基础、Python 语法接近零基础"安排。不讲基础概念，但每行代码都要能解释。

## 从总进度记录迁移的历史问答

2026-10-11 整理迁移；以下内容来自导入的历史对话，未新增实测。

- 解释建目录、创建 venv、激活环境和升级 pip 的命令。
- 澄清 image-classifier 是否为开发目录，处理嵌套目录与改名问题。
- 讨论 VS Code 不显示 .git、.venv 等目录的原因，按用户要求修改显示设置。
- 回顾第一天任务与未实现部分。
- 讨论 Git 换行转换以及 system/global/local 配置优先级；用户提到 core.autocrlf=input，是否最终设置成功未在当前聊天核实。
- 用户明确要求不自行提交；后续仅由用户执行提交和推送。
- 用户要求根目录不新增 AI 说明痕迹，说明和学习记录放 notes。

历史关于 pip 卡住原因、目录占用原因及 venv 可随意移动的断言没有在当前聊天独立验证，后续遇到问题应重新检查。
