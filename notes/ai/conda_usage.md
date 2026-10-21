# 在 conda-test 分支试用 Conda

本项目保留原有 `.venv`，另用 Miniforge 提供的 Conda 创建 `image-class-conda`。Git 分支管理代码和环境说明文件；Conda 环境独立保存在仓库外，切分支不会自动切解释器。

## 环境描述

仓库根目录的 `environment.yml` 描述项目环境：Python 3.12、pip，使用 conda-forge。当前学习代码只依赖标准库，因此不预装 Pillow、NumPy 或 PyTorch。

在装好 Miniforge 的电脑上可用以下命令重建：

```powershell
conda env create -f environment.yml
```

命令在项目根目录运行。环境描述文件可以由用户自行提交到 Git，实际环境目录不提交。

## 日常使用

在 Miniforge Prompt 中，或本项目自动激活后的 VS Code PowerShell 终端中：

```powershell
conda activate image-class-conda
python --version
python -c "import sys; print(sys.executable)"
python scripts/export_samples.py --help
```

项目目录：`C:/Users/24718/Desktop/image-class`。激活后 Python 应位于 `C:/Users/24718/miniforge3/envs/image-class-conda/python.exe`。

如果当前终端已激活 `.venv`，先执行其 `deactivate`，再激活 Conda，避免两套环境叠加。切换后检查 `sys.executable` 是最直接的确认方法。

退出 Conda：

```powershell
conda deactivate
```

之后可以再次激活原项目环境：

```powershell
& "C:/Users/24718/Desktop/image-class/.venv/Scripts/Activate.ps1"
```

## VS Code

按 Ctrl+Shift+P，运行 Python: Select Interpreter，选择 `image-class-conda`。若列表没出现，可手动输入完整解释器路径：

```text
C:/Users/24718/miniforge3/envs/image-class-conda/python.exe
```

选择后关闭旧终端，创建新终端，再核对 Python 路径。VS Code 的解释器选择不会随 Git 分支自动切回；回到 main 使用旧环境时，也应选择 `.venv` 的解释器。

本项目 `.vscode/settings.json` 已增加 `Conda (image-class)` 终端配置：使用 Windows PowerShell，加载 Miniforge 自带 conda-hook.ps1 后激活 image-class-conda，并将它设为本项目新终端的默认配置。已有终端不会重新运行启动命令，需要关闭旧终端后新建。配置位于被 Git 忽略的 .vscode 目录，不会随 Git 分支自动切换；以后想恢复普通终端时，在 VS Code 的 Terminal: Select Default Profile 中选择 PowerShell。

Python 扩展曾记住旧 `.venv`，在 Conda 激活后又执行其 Activate.ps1，造成两个环境叠加。本项目现关闭 `python.terminal.activateEnvironment` 和 `python.terminal.activateEnvInCurrentTerminal`，由自定义终端启动命令负责激活 Conda。这不会删除 `.venv`，也没有修改其他项目的设置。已经叠加的终端需要关闭并重新创建。

终端激活与编辑器选中的解释器是两件事。扩展已缓存的旧选择可能继续用于运行按钮和调试；请在 Python: Select Interpreter 中明确选择 image-class-conda。仅设置 python.defaultInterpreterPath 不保证覆盖既有选择。

Miniforge 只为当前用户安装，没有注册为系统默认 Python，也没有向系统 PATH 添加整套 Python。本次没有执行全局 conda init 或修改用户 PowerShell profile；项目终端通过自己的启动命令激活目标环境，Miniforge Prompt 的 base 提示与项目终端不是同一套启动方式。

用户自行创建了 image-class-conda 环境；已用 Windows PowerShell 验证 hook 加载、环境激活及解释器路径。VS Code 实际新终端的显示需在用户新建终端后确认；没有自动执行 Git 提交或推送。
