# Day 17：用 Pillow 读取真实图片

布置日期：2026-10-18。约 60 分钟任务量，不限制实际耗时。Day 16 已完成配置读取与汇总保存，今天从“收集文件路径”前进到“读取图片信息”。核心学习代码由用户编写。

## 今天的目标

使用 Pillow 打开少量真实图片，得到宽、高和颜色模式；再复用 Imagesacnner.collect_samples() 的结果，逐张显示路径、类别与图片信息。今天不增加 CSV 列、不训练模型；元信息 CSV 留到 Day 18。

## 1. 环境与依赖（约 10 分钟）

当前以用户最新选择为准，使用 main 分支和 image-class-conda：C:/Users/24718/miniforge3/envs/image-class-conda/python.exe。曾临时切回 .venv 排查延迟；实际脚本约 0.10 秒，发现 Python 环境扩展发送命令前可能等待 Shell 集成，已将该项目等待上限设为 500 毫秒，用户反馈改善后要求重新试用 Conda。VS Code 新终端直接激活 image-class-conda，运行按钮的实际响应仍由用户验证。

在项目的新终端中确认解释器：

```powershell
python -c "import sys; print(sys.executable)"
```

Conda 环境已能导入 Pillow 12.3.0，environment.yml 已包含 pillow，无需重复安装。今后新建这套环境可执行：

```powershell
conda env create -f environment.yml
```

完成后检查当前 Python 能否导入：

```powershell
python -c "import PIL; print(PIL.__version__)"
```

安装包名是 Pillow，代码导入用 PIL。若编辑器运行按钮仍记住 .venv，在“Python: 选择解释器”中选择 image-class-conda；终端环境与运行按钮的解释器需要一致。不要同时激活 .venv 和 Conda。修改默认解释器路径不保证覆盖编辑器已缓存的选择。

保留备用的项目 .venv（已安装 Pillow 13.0.0，依赖记在 requirements.txt）；当前 Conda 环境以 environment.yml 描述。不要把整个环境目录放进 Git。

## 2. 准备真实图片（约 5 分钟）

布置时 C:/Users/24718/Desktop/image-class/1/cat/a.jpg、cat/backup/b.PNG、dog/c.jpeg 和 output/ignored.jpg 均是 0 字节占位文件。此前扫描文件名可以通过，并不代表它们能作为图片打开。学习过程中用户已将类别目录中的占位文件替换为真实 WebP；最终结果见收尾状态。

在 1/cat 和 1/dog 中放入两三张可以正常查看的真实 JPG 或 PNG 图片即可，可复制自己的图片，不必下载正式数据集。替换占位文件或删除占位文件后放入真实图片均可；文件名不影响读取练习。仅把文字文件改成 .jpg 也不能得到真实图片。

## 3. 先理解一张图片（约 15 分钟）

单张图片示范，路径换成实际存在的文件：

```python
from pathlib import Path
from PIL import Image

image_path = Path("1/cat/真实图片.jpg")

with Image.open(image_path) as image:
    width, height = image.size
    print("宽：", width)
    print("高：", height)
    print("颜色模式：", image.mode)
```

- Image.open 接受路径，返回图片对象；这里的 image 不再是路径字符串。
- image.size 是 (宽, 高) 元组，单位为像素。width, height = image.size 是已学过的拆包赋值。也可以用 image.width、image.height。
- image.mode 是字符串。RGB 通常是红、绿、蓝三个颜色通道；RGBA 在 RGB 外增加透明度通道；L 是灰度模式。它与 JPG、PNG 等文件格式不是一回事；一张 PNG 可以是 RGB，也可以是 RGBA 等其他模式。
- with 在退出代码块时关闭关联资源。只在块内读取并打印这些属性即可；不必写 image.close()。
- Image.open 通常先读取文件头，尺寸和模式可由头部取得；成功取得这些属性不等同于已经完整解码全部像素。今天只学习读取信息，不把它写成完整的坏图检测工具。

不要给 Image.open 加文本编码参数 encoding；读取图片与之前读取 CSV/JSON 文本不同。

## 4. 接上现有扫描器（约 25 分钟）

建议新建 C:/Users/24718/Desktop/image-class/scripts/inspect_images.py，让它成为今天的练习入口；保留已有导出功能。也接受其他能独立运行、功能正确的组织方式。

复用已有知识：

1. 获取数据根目录，可沿用 input + Path，或已学过的 argparse，不强制重写参数界面。
2. 从 config/scanner.json 读取 included/excluded，创建 Imagesacnner。无需为了今天重构 export_samples.py 中的全局变量函数；可在新入口直接读取配置。
3. collect_samples() 返回 (dirs, photos)，取第二项。photos 中每项是 (图片路径字符串, 类别)，不是字典。
4. 遍历这些样本，使用 Image.open 取得宽、高和 mode，显示路径、类别与信息。循环与函数如何组织由用户实现，不提供完整成品。

示意输出，数字以真实图片为准：

```text
cat | a.jpg | 640 × 480 | RGB
dog | c.png | 800 × 600 | RGBA
```

不要求为颜色模式特意凑齐 RGB、RGBA、L 三套图片。今日不新增批量错误恢复、图像缩放、模式转换或 CSV 元信息导出，避免扩大范围。

## 5. 完成标准（约 5 分钟）

- 当前 Conda 环境能导入 PIL，environment.yml 包含实际新增的 pillow 依赖。
- 至少两张有效图片可读出正数的宽、高和实际颜色模式；展示它们对应的路径和类别。
- 至少一张图片的宽高与图片查看器或文件属性中的尺寸相符。不以统一的示意数字代替真实读取。
- 读图输入来自扫描器的样本结果，而不只是写死两个文件名；不机械重测之前全部扫描和 CSV 功能。
- 能解释 image_path 与 image 的区别、image.size 的顺序，以及 PNG 与 RGBA 分别表示什么。

布置时仅保存任务，不提前创建 records/day17-record.md 或更新学习完成进度；完成后统一整理问答、实际改动与验证结果，实际结果见下方收尾状态。Git 暂存、提交、推送由用户操作。

官方参考：

- https://pillow.readthedocs.io/en/stable/installation/basic-installation.html
- https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
- https://pillow.readthedocs.io/en/stable/reference/Image.html

## 收尾状态：2026-10-18

核心目标完成。实际 Conda 解释器运行 inspect_images.py，输入 1 后成功读取扫描器收集的三张真实 WebP：saki 为 400 × 1000、RGBA；shiomi 为 1143 × 1647、RGBA；shiomi2 为 1440 × 1920、RGB。Windows 文件属性独立确认 saki 尺寸为 400 × 1000。路径先转为 Path，再使用 stem/suffix，with 内读取尺寸和颜色模式，脚本退出码 0。

按实际实现范围收尾：未单独逐行显示类别，入口仍使用固定 included/excluded；没有把重复接入 JSON、类别逐行显示或理论口述记成已完成。下一天整理元信息 CSV 时保留扫描器的标签。环境切换与运行延迟排查、问答和验证已统一写入 records/day17-record.md；未代改核心代码或执行 Git 暂存、提交、推送。
