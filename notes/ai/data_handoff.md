# 图片数据交接记录

更新于 2026-11-24。供另一台 Mac 上继续处理动漫人物识别项目时参考。这里记录目前的素材整理情况，不代表数据已经完成清洗或可以直接用于训练。

## 目标和约定

- 识别 Day 71 已确定的角色，类别编号和完整名单见 [Day 71 任务](daywork/day71.md#已确定的首版范围)。
- 优先收集官方立绘、原作截图和指定 AI 人设图，以单人且角色清晰的图片为主。
- `deepseek娘`、`claude娘`、`gpt娘` 是三个独立类别和文件夹；来源表的 `work` 都是 `AI同人`。
- 《哭泣少女乐队》这组的 `work` 使用“有刺无刺”，不额外增加 `band` 列。纯田真奈暂不补图；现有的 1 张是之前留下的。
- 用户希望 MyGO、Ave Mujica、有刺无刺和梦限大的角色尽量达到每人 200 张；millsage 和 AI 娘尽量补充。

## 本机现状

- 原始素材：项目下 `data/raw/<角色名>/`，不按作品再套一层目录。不同图片的扩展名可能不同。
- 来源表：`data/manifests/sources.csv`；以 `path`（相对于 `data/raw`）、`class_id`、`label`、`work` 开头，其后保留来源、作者、授权说明、尺寸、SHA-256 和备注等字段。没有 `character` 或 `image_type` 列。
- `data/fixtures/` 是少量供脚本使用的测试图片，可以由 Git 跟踪；它不是完整数据集。
- `data/raw/` 和 `data/manifests/sources.csv` 被 `.gitignore` 忽略。**Git 提交或拉取不会传送这两部分**，另一台电脑需要单独复制；不要为了同步而将它们强行加入 Git。

2026-11-24 核对时，来源表有 4109 条记录，记录对应的文件均存在、能由 Pillow 打开且 SHA-256 与表一致。`data/raw/` 实际有 4116 个文件、约 2.40 GB；文件数比来源表多 7 个，尚未逐个核实多出的文件，因此不要把文件总数直接当作已登记样本数。以下数量均来自来源表：

| 作品或分组 | 已登记数量 |
| --- | --- |
| 迷途之子 / MyGO | 高松灯、长崎素世、千早爱音、立希、要乐奈各 200 |
| 颂乐人偶 / Ave Mujica | 三角初华、丰川祥子、若叶睦、八幡海玲、祐天寺若麦各 200；纯田真奈 1 |
| 有刺无刺 | 卢帕、海老冢智、安和昴、河原木桃香、井芹仁菜各 200 |
| 梦限大 | 仲町阿拉蕾、峰月律、藤都子各 200；宫永野乃花 163；千石由乃 195 |
| millsage | 汐见萤 7、伊泽枣 5、琴平凪 7、滨崎茉幌 5、和泉朋花 7 |
| AI同人 | deepseek娘 74、claude娘 24、gpt娘 21 |

## 素材来源与处理

- MyGO、Ave Mujica、有刺无刺使用了 BangumiBase 的公开角色截图包：分别见 [MyGO](https://huggingface.co/datasets/BangumiBase/bangdreamitsmygo)、[Ave Mujica](https://huggingface.co/datasets/BangumiBase/bangdreamavemujica)、[Girls Band Cry](https://huggingface.co/datasets/BangumiBase/girlsbandcry)。归档地址和内部文件名记录在来源表中。
- 梦限大部分图片来自用户 E 盘动画视频截帧及公开截图；具体来源以来源表为准。millsage 部分素材来自 [Haneoka](https://haneoka.org/jp/en/characters/16/)，AI 人设图部分来自 [梗鲸图库](https://aigengtu.com/characters)。
- 为去除字幕，对新增横向截图及部分此前的 MyGO、Ave Mujica 截图裁去了底部约 13%；梦限大截图也做了相应裁切。部分人物图本来就已裁切，处理方式以来源表的备注为准。
- 裁切并未逐张人工核验：有可能仍留字幕或画面文字，也可能裁掉角色身体的一部分。AI 人设中的文字有时属于原图内容，不一定是字幕。
- 曾按图片哈希和视觉相似度筛重、抽查角色，但并非逐张人工确认；截图仍可能相近、出现多人、错分、画质不佳或字幕残留。200 张表示数量，不代表 200 张都已适合训练。
- 原图与整理图的公开访问状态不等于训练和再发布授权；使用前需核对各来源和原作者的条件。
- Windows 上裁剪前备份在 `C:/Users/24718/Documents/Codex/2026-10-11/hi-3/day71-source-check/`：`mygo-ave-originals-before-subtitle-crop.zip` 和 `yumemita-originals-before-subtitle-crop.zip`。这是 Windows 本地备份，不在 Git 中，Mac 上不会自动出现。

## 给 Mac 的同步与后续工作

1. 先将本交接文件通过 Git 正常提交、推送，再在 Mac 拉取。当前写入这份文件本身不会自动提交或推送。
2. 另外复制 Windows 项目内的 `data/raw/` 和 `data/manifests/sources.csv` 到 Mac 项目相同的相对位置，例如使用移动硬盘或其他可靠的文件传输方式。两者应作为同一次快照一起复制；复制前先留意 Mac 端是否已有需要保留的数据，避免直接覆盖。
3. 在 Mac 上核对图片数、来源表和实际文件，尤其确认来源表之外的 7 个文件是什么；用 `path` 相对 `data/raw` 解析，不要硬编码 Windows 盘符。
4. 继续补梦限大未满的两位、millsage 和 AI 娘。入训练前检查角色标签、字幕、多人图、相似帧及来源授权，避免同一镜头的相近帧同时进入训练集和验证集。

此文件只作为数据工作交接；是否开始或完成之后的学习日，由用户决定。
