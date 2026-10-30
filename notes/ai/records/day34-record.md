# Day 34 每日记录

日期：2026-10-30。主题：整理样本表、统计类别数量与占比、保存 CSV 和读回。用户询问是否完成后，助手读取实际源码并运行验证，按核心范围收尾。

## 实践与验收

- 用户在 scripts/pandas_basics.py 新增 day34，创建五条包含重复路径及缺失标签的练习数据，先按 label/path 删除缺失，再按 path 去重。两步返回结果接回同一个 rows，清理后保留 A/a.jpg、A/c.jpg、B/d.jpg 三条。
- 使用 rows['label'].value_counts() 得到 counts，value_counts(normalize=True) 得到 ratio，以两个 Series 组装 DataFrame，再 reset_index 将标签索引变成 label 数据列。实际统计为 A=2、B=1，占比约为 2/3、1/3。
- 保存 output/rows.csv 与 output/stats.csv，均指定 index=False、utf-8-sig。统计列名为 counts 而非示例的 count，属于可接受的自主命名。
- 用户通过 csv.DictReader 读回 stats.csv 并打印记录列表。CSV 文本经该方式读入的数值显示为字符串，这是正常读取行为。
- 使用 /Users/qiuyaojia/miniconda3/envs/image-class-conda/bin/python 以 -B 运行原脚本，工作目录为独立临时目录，验收先准备 output 子目录。脚本正常退出，无报错。未修改代码、未覆盖项目现有输出。
- 验收另外使用 Pandas 读回两份实际生成文件：样本表三行、必要字段无缺失、路径无重复，统计数量合计三条、占比总和接近 1，两份 CSV 均无多余索引列。
- 用户代码未实现 output 自动创建，当前项目已存在该目录；未打印清洗前后行数、未自行读回样本表、未提交文字发现，不把验收补充检查算作用户已写出的代码。不因文件名、展示方式或这些非核心步骤强制重做。

## 当日问答

1. count 与 ratio 如何保存：先构造包含标签、数量和占比的表，再 to_csv 即可一起保存。
2. reset_index 的作用：默认把旧索引变成数据列，并新建默认整数行索引；drop=True 丢弃旧索引；Series.reset_index(name=...) 可给原值命名，不能无区别地套用到 DataFrame。
3. 给一列赋两列表格的问题：value_counts().reset_index(...) 返回 DataFrame，不能把两列直接赋给 stats 的单列。
4. 用户希望直接使用 value_counts 获得占比，因此采用两次 value_counts，而不是额外手算除法；两个 Series 按标签索引对齐，组成 count/ratio 表格。
5. Series 与 DataFrame：选单列通常得到 Series，用列名列表选列得到 DataFrame；Series.value_counts 与 DataFrame.value_counts 都返回 Series，后者统计整行字段组合，可能形成多级索引。使用 type、ndim、shape 区分，不根据打印出来看似有几列判断。

上述知识按已解释和已实践记录，不把所有解释都标记为独立理解验收通过，也不追加口头考试。

## 环境与编辑器

- 用户要求 Mac VS Code 保留语法建议和 Tab 接受建议、关闭灰色行内代码补全。助手把用户设置 editor.tabCompletion 从 off 改为 on，保留 quickSuggestions 和触发字符建议开启、inlineSuggest.enabled=false，并安装、核对 ms-python.vscode-pylance 2026.4.1。未通过 UI 单独验收建议弹窗效果，未改变项目学习代码。
- Mac 最初未安装 Pandas，用户自行安装时遇到 Anaconda defaults 源 SSL EOF。助手提供只使用 conda-forge 的单次安装命令，没有关闭 SSL 验证或修改全局源配置；不能据此断定用户最终具体用了哪种安装方式。
- 本次验收实际确认 Mac 环境已可导入 Pandas，版本为 3.1.0。助手未代为执行 Pandas 安装，未修改依赖清单。

## 收尾与接续

Day 34 按核心范围完成，统一更新当日任务、总进度与总体计划接续点。下一学习日 Day 35 休息或可选复盘，Day 36 进入 Matplotlib；等用户要求开始。不代写后续核心代码，不 Git 暂存、提交或推送。
