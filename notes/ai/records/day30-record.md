# Day 30 每日记录

日期：2026-10-27。主题：读取 CSV、选列与 loc/iloc。用户自行完成练习并纠正列名大小写后，助手运行确认，按核心范围收尾。

## 实践与验证

- 用户在 scripts/pandas_basics.py 中新增 day30 函数，使用 pd.read_csv 读取 1/output/samples.csv，编码 utf-8-sig，打印内容、shape 与列名。
- 开始布置时该 CSV 表头为 path、label，数据是旧 cat/dog 示例；本日后续核对时实际文件已变为 Path、Label，三条记录对应丰川祥子、汐见萤、汐见萤。最新代码正确使用当前实际大小写，不将旧表内容当成当前数据。
- 用户分别选择 df['Path']、df[['Path']]、df[['Path','Label']]，正确得到 Series、一列 DataFrame、两列 DataFrame；使用 Path 列代替原任务的 label 列，目标等价。
- iloc[:2] 取前两行，iloc[-1] 取末行，iloc[0] 取首行，均正确。
- 用户使用 df.copy()，把副本索引改为 [10,20,30]，分别打印 dfcopy.iloc[1] 和 dfcopy.loc[20]，两者都指向相同的第二条样本，行名为 20、Label 为汐见萤。用户选择对比整行而非单个标签值，接受核心等价实现。
- 使用实际 C:/Users/24718/miniforge3/envs/image-class-conda/python.exe，以 -X utf8 -B 运行当前脚本入口；读取表为 (3,2)，所有选取输出正确，退出码 0，无报错。
- 未单独练习 loc 的行切片或组合行列标量选取，不记为已实践；相关规则已在教程讲解，不额外要求机械补写或口头考核。

## 本日问题：KeyError 与列名大小写

用户提供 KeyError: 'label'，代码片段同时含有小写 path。助手只读检查源码与 CSV，发现当前表头为 Path,Label；Pandas 列名区分大小写，因此 label 不等于 Label，path 不等于 Path。

解释报错原因后，建议使用实际列名 df['Path']、df[['Path']]、df['Label']，并通过 df.columns 核对列名。用户自行完成修改，最新运行不再报错；没有代改 CSV 或核心脚本。

## 收尾与接续

Day 30 核心练习完成，用户代码采用等价的自主组织方式。结束后统一更新本记录、任务状态、总进度和总体计划；总进度不收录具体问答。

未安装依赖、修改环境配置或进行 Git 暂存、提交、推送。下一学习日 Day 31：条件筛选、缺失值与重复记录处理，等待用户要求开始，不提前创建任务或代写练习。
