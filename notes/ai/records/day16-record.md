# Day 16 每日记录

布置、学习与收尾日期：2026-10-17。核心目标：读取 JSON 配置控制扫描，将 CSV 读回统计保存为 JSON 汇总。按用户要求在实际完成后统一整理本日过程与问题。

## 实际实现与验收

- 用户建立 config/scanner.json，包含 excluded 与 included 数组。脚本新增 --config；未提供时由主程序选择 config/scanner.json，提供时使用指定文件，保留 root 与 --output。
- read_json 使用 json.load 读取，分别用 set 转换两项并返回。主程序使用配置中的排除目录与图片后缀创建 Imagesacnner，配置实际参与扫描。
- read_samples 返回 rows, counts，主程序只调用一次并接收返回值；save_summary 使用本次读回的行数与类别计数字典，不重新读取 CSV。
- save_summary 保存 root、csv_path、total、counts，位置在实际 CSV 的同级 summary.json。路径使用 resolve().as_posix() 转成正斜杠字符串；json.dump 使用 ensure_ascii=False、indent=2。
- 用户对配置读取、汇总写入使用 utf-8-sig，本次汇总读回也按 utf-8-sig 解析。接受此自主选择，不将其误记成无 BOM 的 utf-8 输出，也不以编码风格阻塞本日收尾。
- read_json 和 save_summary 使用主程序已初始化的模块全局变量；用户已讨论并理解全局变量可用，此处沿用 CLI 脚本的组织方式，没有强制改为完整传参设计。read_json 仍调用两次取两项、存在旧注释及不可达 return 等非核心整理项，未追加机械重构要求。
- 首次汇总误用了 read_json 的返回值，total 变成排除目录数量，counts 变成后缀集合，json.dump 报 set 不可序列化。后续改为 CSV 的 rows 与 counts。
- 另一次将 read_samples(output)[0]、[1] 分别写入汇总，加上主程序独立调用，导致三次读取与打印。最终改为主程序 rows,counts = read_samples(output)，汇总直接复用两项。
- 2026-10-17 在独立临时目录运行实际脚本，复制用户配置作为该目录的默认 config/scanner.json，不修改用户原配置或现有输出。样本含 cat/a.jpg、cat/backup/b.PNG、dog/c.jpeg、cat/readme.txt、output/ignored.jpg、cat/output/ignored.png、loose.jpg。
- 默认配置实际读回三条，cat: 2、dog: 1。独立读取 CSV 核对三条绝对路径与标签，独立 json.load 读取 summary，total、counts、root 和 csv_path 与实际结果精确对应。
- 使用另一份只含 included=[".jpg"] 的配置，并通过 --output 指定新建多层目录内的中文文件名：实际只读回 cat/a.jpg，一条、cat: 1；summary 在自定义 CSV 同级，字段正确。证明 --config 真正改变扫描规则，而不只是打印了配置。
- 有效空目录导出后，summary 为 total: 0、counts: {}，与 CSV 读回一致。
- 三种情况实际脚本均退出码 0、无标准错误，且读回数量提示每次只出现一次。临时测试目录自动清理，没有修改用户的配置或练习输出。
- 结论：Day 16 核心功能完成，任务收尾后统一记录。不将运行成功等同于所有理论都已独立考核通过；没有额外要求 try/except，也没有代改学习代码、Git 暂存、提交或推送。

## 本日问题与解释

### 1. set 是干什么的

set 将可遍历数据转换为集合，元素唯一、排列顺序不保证。JSON 的 included/excluded 数组读回是列表，set 转换后与原代码手写的后缀或排除集合一致，适合成员判断。列表在本例也能完成成员判断，不是必须转换；空集合是 set()，空花括号是字典。没有宣称集合能通过下标访问或保持原列表顺序。

### 2. 读取配置为什么不用 utf-8-sig

无 BOM 的 UTF-8 JSON 可用 utf-8；utf-8-sig 在读取时兼容有无 BOM，若有会去掉它。若用普通 utf-8 解码保留开头 BOM 后交给 json.load，可能报 Unexpected UTF-8 BOM。写入时 utf-8-sig 会添加 BOM；JSON 常用无 BOM 的 utf-8，之前 CSV 用 utf-8-sig 便于 Excel 识别中文。本日用户选择配置和汇总均使用 utf-8-sig，实际验证通过。

### 3. 路径显示中的双反斜杠怎么改成正斜杠

字典或列表表示字符串时的双反斜杠通常是转义显示，实际路径只有一个反斜杠。若确实希望统一使用正斜杠，可用 p.resolve().as_posix() 和输出 Path 的 resolve().as_posix()，返回值已是字符串，不必再 str。最终 summary 两项采用该写法。

### 4. Object of type set is not JSON serializable

读取真实脚本确认 summary 的 total 使用 len(read_json()[0])，counts 使用 read_json()[1]。该函数返回配置排除集合和后缀集合，不是图片数据；于是 total 数值来源错误，counts 是 JSON 默认不支持的 set。应复用 read_samples 返回的 rows 和 counts，而不是仅 list(集合) 消除报错；后者仍保存了错误的数据来源。字典、列表等基础类型可按默认方式写入，Path 和 set 如需保存则需先转成合适的基础表示。

### 5. 为什么数量和类别统计重复出现三次

主程序 read_samples 一次，汇总里 read_samples(output)[0] 和 read_samples(output)[1] 又各调用一次；下标是在每次函数执行完成后取返回项，并不会复用之前的调用。每次都会读取文件并执行函数里的打印。结合用户使用全局变量的当前写法，主程序接收 rows,counts，再在 save_summary 里直接使用这两个值。最终已只读取和打印一次。

### 6. 能不能只在直接执行它时打印

解释独立调用与作为其他表达式的一部分调用都会执行同一个函数体，Python 不会自动只为前者打印。可增加 show=True 参数，在 if show 中打印；只取数据时传 show=False。另说明 __main__ 判断文件启动方式，不能区分同一文件中的不同函数调用。本例最终使用调用一次并复用返回值，没有采用 show 参数，示例不记作实际实现。

### 7. ensure_ascii=False 是什么意思

默认 True 把中文等非 ASCII 字符写成 Unicode 转义形式，False 则原样输出。两种形式在正确解码 JSON 后数据相同，False 便于人阅读；文件编码仍由 open 的 encoding 控制。indent=2 设置嵌套层级的美化缩进。

### 8. Day 16 是否完成

读取实际源代码和配置后，用默认配置、仅 JPG 配置加自定义输出、空目录三种有意义的情况运行实际脚本，再独立读回 CSV 和 summary。所有对应字段正确、输出重复问题已解决，确认核心任务完成后统一更新记录，没有提前写完成状态。

## 接续

下一学习日为 Day 17：用少量真实图片学习 Pillow 读取宽高与颜色模式。届时核对环境及依赖，不把现有空占位图片当作可解码图片。等待用户要求开始，不提前安装或生成后续任务。

官方参考：https://docs.python.org/zh-cn/3.12/library/json.html 。
