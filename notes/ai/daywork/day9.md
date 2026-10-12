# Day 9：对象的方法——用自己的配置扫描和统计

日期：2026-10-12。任务量约 60 分钟，不限制实际耗时。

## 今天的目标

给现有 Folderscanner 增加 collect_suffixes() 和 count() 方法。创建对象时保存目录和排除规则，调用 scanner.count() 就能得到该对象配置对应的统计字典。

修改文件：C:/Users/24718/Desktop/image-class/scripts/file_scanner.py。
沿用用户现有类名 Folderscanner 与属性 self.p、self.excluded。

## 1. 认识方法调用（约 10 分钟）

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self.value

counter = Counter(10)
print(counter.add(3))  # 13
```

类里的普通实例方法通过对象调用时，会自动得到当前对象作为 self。counter.add(3) 可理解为 Counter.add(counter, 3)；amount 接收 3。

今天要让扫描器执行行为，而不只是保存配置。self.p、self.excluded 都是该对象已有属性，因此 count() 不需要调用者每次再传一遍目录与排除规则。

## 2. 增加两个方法（约 30 分钟）

保留现有 __init__，自己在类里面增加：

```python
def collect_suffixes(self):
    # 使用 self.p 遍历
    # 使用 self.excluded 排除目录
    # 收集后缀并返回列表
    ...

def count(self):
    # 调用当前对象的 collect_suffixes 方法
    # 用已有 count_labels 统计列表
    # 返回统计字典
    ...
```

提示：
- 原 count_file.py 的 collect_suffixes(root, excluded) 可以作为参考。
- 方法里将原来的 root 换成 self.p，excluded 换成 self.excluded。
- 调用当前对象的另一个方法使用 self.collect_suffixes()。
- 文件开头导入已有函数：from count_labels import count_labels。
- 保留已有空后缀显示规则，过滤 .venv、.git、__pycache__、output。
- 两个方法缩进在类内部，与 __init__ 同级。

目标调用方式：

```python
counts = scanner_a.count()
print(counts)
```

不要依赖主程序全局 p/excluded，确保方法读取的是当前对象的属性。

## 3. 验证不同目录的统计（约 10 分钟）

自己准备两个小目录；示例文件可以为空：

```text
data/
├── day9-a/
│   ├── a.py
│   ├── b.txt
│   └── output/
│       └── old.csv
└── day9-b/
    ├── c.txt
    └── sub/
        └── d.txt
```

分别用 Path("data/day9-a") 和 Path("data/day9-b") 创建扫描器，排除集合包含 output。

打印两个对象各自 count() 的结果，期望：
- day9-a：{".py": 1, ".txt": 1}，old.csv 不计入。
- day9-b：{".txt": 2}，子目录中的 d.txt 被计入。
- 字典打印顺序不作要求。

从项目根目录、已激活 .venv 的终端执行：

```powershell
python scripts/file_scanner.py
```

## 4. 理解检查（约 10 分钟）

1. 为什么 scanner_a.count() 不需要手动传 self、p 和 excluded？
2. 为什么 count 方法内调用收集方法写 self.collect_suffixes()？
3. collect_suffixes 与 count 各自返回什么，为什么要返回？

完成标准：两个方法按当前对象的配置工作，返回列表和字典；两组目录统计及 output 排除结果正确；能解释对象如何传入方法、方法如何读取属性和返回结果。

每日任务在开始时保存；Day 9 问答与验证结果等今日任务结束后再统一写 records/day9-record.md，并同步总进度。核心学习代码留给用户实现，不自动提交或推送。

