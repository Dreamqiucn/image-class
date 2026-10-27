# Day 30：读取 CSV、选列与 loc/iloc

布置日期：2026-10-27。预计约 60 分钟，接续 Day 29。使用已有 Pandas，不安装依赖，核心练习由用户自己编写。

## 今天的数据与目标

已只读核对现有 C:/Users/24718/Desktop/image-class/1/output/samples.csv，使用 utf-8-sig 可读取，当前为三行两列，列名 path、label，标签 cat、cat、dog。它是旧练习表，不要求重新导出或采集正式角色数据。表里的旧图片路径今天作为文本使用。

学会从 CSV 建立 DataFrame，选一列或多列，按标签与按位置选择行列，理解 loc 与 iloc 切片终点的区别。

## 1. read_csv

```python
import pandas as pd

csv_path = "C:/Users/24718/Desktop/image-class/1/output/samples.csv"
df = pd.read_csv(csv_path, encoding="utf-8-sig")
print(df.head())
print(df.shape)
print(df.columns)
```

read_csv 已经打开并解析 CSV，返回 DataFrame，不需要自己再用 csv.DictReader 转列表。第一行默认作为列名，默认行索引是 0、1、2。这里没有额外的 width 列，不要求补造。

文件参数可以是字符串或 Path。也可以自行用 input 获取 CSV 文件路径；使用相对路径时，它相对于运行时工作目录，绝对路径则明确指定文件。

## 2. 单列与多列

```python
print(df["label"])            # Series
print(df[["label"]])          # 一列 DataFrame
print(df[["path", "label"]])  # 两列 DataFrame
```

外层 [] 是选取操作；内层 ["path","label"] 是列名列表。取单个列名通常得到 Series，传列名列表得到 DataFrame，即使列表中只有一个名字。只包含 path、label 两列的当前原表和最后一项内容相同，但多列选择写法仍有意义。

## 3. iloc：按位置选

行列的位置从 0 开始，使用中括号，不是方法调用括号。

```python
print(df.iloc[0])        # 第一行，Series
print(df.iloc[:2])       # 前两行，DataFrame
print(df.iloc[-1])       # 最后一行
print(df.iloc[0, 1])     # 第一行第二列，当前为 cat
print(df.iloc[:2, 0:2])  # 前两行、前两列
```

iloc 的切片与 Python/NumPy 相同，不包含终点。df.iloc[0] 取一行时是一维，df.iloc[0:1] 保留一行二维表；二维表用单个行位置、单个列位置可以取到一个值。

## 4. loc：按索引标签与列名选

```python
print(df.loc[0])                    # 行索引标签为 0 的那一行
print(df.loc[0, "label"])           # 该行的 label
print(df.loc[0:1, ["path","label"]]) # 标签 0 到 1，包含 1
print(df.loc[:, "label"])           # 所有行，label 列，Series
print(df.loc[:, ["label"]])         # 保留为一列 DataFrame
```

loc 的数字也是标签，不表示“第几行”。当前默认索引恰好与位置相同，容易误以为两者完全一样。对于这里的唯一、有序索引，loc 的标签切片包含两端；iloc 的位置切片不包含终点。

## 5. 改一组索引，看清区别

```python
example = df.copy()
example.index = [10, 20, 30]  # 对当前三行表设置新的行标签
print(example.loc[20, "label"]) # 标签 20 的那行，cat
print(example.iloc[1, 1])        # 第二行第二列，也是 cat
print(example.loc[10:20])        # 标签 10、20 两行
print(example.iloc[0:1])         # 只有第一行，标签为 10
```

index 是行标签，columns 是列名，不会因为改 index 就修改图片的 label 列。对当前 example 使用 loc[1] 会找标签 1，因不存在而报 KeyError；不是第二行。iloc[20] 则要求第 21 行，不存在会报 IndexError。知道原因即可，不要求额外异常处理或特意运行报错。

| 对比项 | loc | iloc |
| --- | --- | --- |
| 选行依据 | 行索引标签 | 行的位置，从 0 开始 |
| 选列依据 | 列名 | 列的位置，从 0 开始 |
| 切片终点 | 标签切片通常包含终点；本日有序唯一索引示例包含两端 | 不包含终点 |
| 示例 | example.loc[20,"label"] | example.iloc[1,1] |

## 自己实践

继续在 scripts/pandas_basics.py 加入自己的 Day 30 函数，或新建自选文件：

1. 读入上面的现有 CSV，查看内容、shape、columns。也可自己输入这个文件的完整路径，选一种方式即可。
2. 分别取 label 单列、只含 label 的一列 DataFrame、path 与 label 两列，观察 type 或 shape 的不同。
3. 使用 iloc 取前两行、最后一行及第一行的 label；使用 loc 按标签和列名选出对应内容，观察切片终点。
4. 为当前三行表的副本设置 [10,20,30] 索引，用 loc 和 iloc 分别取第二行的 label，核对值相同。可选对比两种切片，不要求额外问答。

不要求固定函数名、打印格式、保存新 CSV 或复用旧扫描程序。条件筛选、缺失值和重复记录留到 Day 31，不以旧导出脚本遗留问题阻塞今天。

## 记录约定

本文件只保存当天任务，尚未完成。每日问答和成果在本日结束后统一保存到 records/day30-record.md，再更新总进度；总进度不收录具体问答。不代写核心练习，不进行 Git 暂存、提交或推送，不提前创建 Day 31 任务。

参考：[Pandas 读取表格](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)、[选择子集](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)、[索引规则](https://pandas.pydata.org/docs/user_guide/indexing.html)。

## 收尾状态：2026-10-27

核心完成。用户新增 day30 函数，完成 CSV 读取、单列与多列表格选择、iloc 行选取，以及自定义索引 [10,20,30] 后的 loc/iloc 同行对比。实际 Conda Python 运行全部当前练习，输出正确，退出码 0。

注意：收尾时实际 CSV 已改为 Path、Label 两列，样本为角色图片，最新代码按当前大小写选取；上方初始教程小写示例应以实际 df.columns 为准。用户已自行解决大小写引起的 KeyError。

接受选择 Path 列、对比整行等自主等价写法，不要求补写所有切片组合。详细问答与验证统一保存于 records/day30-record.md。下一学习日 Day 31 条件筛选、缺失值与重复记录处理，等待用户要求开始；未代改核心代码、环境或进行 Git 暂存、提交、推送。
