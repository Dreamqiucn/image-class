# Day 29：Pandas 入门，Series 与 DataFrame

布置日期：2026-10-27。预计约 60 分钟，开始第五周。Day 28 复盘已结束，不强制先补考 NumPy。今天用少量手写图片路径和标签建立内存表格。

## 准备：用户手动安装

只读检查现有 C:/Users/24718/miniforge3/envs/image-class-conda/python.exe，当前找不到 pandas。助手未安装或修改环境。

在 Miniforge Prompt 或已能使用 conda 的项目终端手动执行：

```text
conda install -n image-class-conda -c conda-forge pandas
```

不需要另建环境。安装后用当前环境的 Python 运行 `import pandas as pd`、`print(pd.__version__)`，确认导入成功。之后可自行在 environment.yml 的 dependencies 下补充 pandas，记录依赖；助手本次未改该文件。

## 1. Pandas 处理什么

之前的 NumPy 主要处理数值数组。Pandas 常用于带行标签、列名的表格数据，例如图片路径、角色名称、宽高和是否有效。今天的路径和数值均为示例，不要求文件真实存在，不决定正式角色名单或采集数据集。

```python
import pandas as pd

s = pd.Series([640, 800, 1024], name="width")
print(s)
```

Series 是带索引的一维数据，可先理解为一列。默认行索引是 0、1、2；width 是这个 Series 的名字。

## 2. DataFrame 是二维表格

```python
rows = [
    {"path": "角色A/a.jpg", "label": "角色A", "width": 640},
    {"path": "角色A/b.jpg", "label": "角色A", "width": 800},
    {"path": "角色B/c.jpg", "label": "角色B", "width": 1024},
]
df = pd.DataFrame(rows)
print(df)
```

列表里的每个字典代表一行样本，字典的键作为列名。df 是普通变量名，不是固定语法；DataFrame 类名注意大小写。

可以把列作为列表放进字典，再 pd.DataFrame({"path":[...],"label":[...],"width":[...]})；这种使用普通列表作为列的写法，各列长度要相同。两种构造方式选择一种练习即可，不机械要求重复。

DataFrame 是表，Series 是带索引的一维数据；选出单独一列可以得到 Series：

```python
labels = df["label"]
print(labels)
print(type(df))
print(type(labels))
```

今天只用这一处选列认识两种对象，详细的选行、选列和 loc/iloc 留到 Day 30。

## 3. 查看表格信息

```python
print(df.shape)   # (3,3)：三行、三列
print(df.columns) # 列名
print(df.index)   # 行索引
print(df.dtypes)  # 每一列的数据类型
print(df.head(2)) # 前两行
```

shape、columns、index、dtypes 是属性，不加括号。head 是方法，需要括号；head() 默认看前五行，不足五行时返回全部现有行。默认显示在左侧的行索引不是数据列，不额外计入 shape 的列数。

同一张表不同列可以是不同 dtype，例如路径与标签为文本、width 为整数。字符串 dtype 的显示可能因 Pandas 版本或设置不同而变化，看实际结果，不要求固定输出 object 或 str。Series 使用 dtype（单数）查看本列类型，DataFrame 使用 dtypes（复数）查看各列类型。

## 自己实践

自己新建 scripts/pandas_basics.py；不要叫 pandas.py，以免遮住导入的库。核心代码自己写：

1. 独立创建一个 Series，例如几个模拟图片宽度，打印内容、shape、dtype，认识左侧索引。
2. 用至少三条手写样本建立 DataFrame，包含 path、label、width 三列。可用角色A、角色B等示例标签，数值自行填写，不需要扫描或读取真实图片。
3. 打印表格及 shape、columns、dtypes，用 head(2) 查看前两条；取出 label 列，查看内容与 type，区分 Series 和 DataFrame。

可以自行增加记录，不要求指定函数名、终端排版或口头考试。今天不读写 CSV、不做去重筛选或分组统计，不整合原扫描脚本。

## 完成与记录约定

能创建 Series 和 DataFrame，解释一行代表一条样本、一列代表一个属性，并能查看基本表格信息即可按核心范围收尾。已讲解或已安装不等于全部练习完成。

此文件只保存当天任务，尚未完成。每日问答和成果等本日结束后统一整理到 records/day29-record.md，总进度不收录详细问题。不进行 Git 暂存、提交或推送，不提前创建 Day 30 任务。

参考：[Pandas 表格入门](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)、[官方安装说明](https://pandas.pydata.org/docs/getting_started/install.html)、[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)、[head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)。

## 收尾状态：2026-10-27

按建表核心目标完成。用户自行编写 scripts/pandas_basics.py，创建 Series 与三行三列 DataFrame，查看属性、head(2) 和 label 列。实际 Conda Python 运行成功，Pandas 3.1.0 可用；表对象与单列分别为 DataFrame、Series。

width 使用 x、y、z 字符串占位，不记为已测量真实宽度或建立整数宽度列，不阻塞今天的建表练习。详细问答、运行结果及经授权整理 NumPy 笔记的过程统一保存到 records/day29-record.md。下一学习日 Day 30，等待用户要求开始；未代改核心代码、安装依赖或操作 Git。
