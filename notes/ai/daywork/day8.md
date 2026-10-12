# Day 8：类与对象——让扫描器保存自己的配置

日期：2026-10-12。第二周第 1 个学习日，任务量约 60 分钟，不限制实际耗时。

## 今天的目标

认识 class、对象、__init__ 和 self；自己写 FolderScanner 类，创建两个扫描器对象，让它们保存不同的目录与排除规则。

练习文件：C:/Users/24718/Desktop/image-class/scripts/folder_scanner.py。
今天完成配置保存和对象操作；后续 Day 9 再给对象增加扫描、统计方法。

## 1. 认识类和对象（约 15 分钟）

类描述一类对象的数据和行为，对象是由类创建的具体实例。属性是对象保存的数据，方法是对象可以调用的函数。

先理解一个小例子：

```python
class Student:
    def __init__(self, name):
        self.name = name

a = Student("小明")
b = Student("小红")

print(a.name)
print(b.name)
```

- class Student：定义一个类。
- Student("小明")：创建一个对象。
- __init__：对象创建时自动执行的初始化方法。
- self：当前正在初始化的对象，由 Python 自动传入；调用 Student 时只填写 name。
- name：方法接收的参数。
- self.name：这个对象保存的属性。

创建 a 时 self 指 a 对应的对象，创建 b 时 self 指 b 对应的对象。可将 self 初步类比为 JS 的 this，但 Python 在方法参数中显式写出它。

参考：https://docs.python.org/zh-cn/3.12/tutorial/classes.html 。

## 2. 自己实现 FolderScanner（约 25 分钟）

在练习文件里写：

```python
from pathlib import Path

class FolderScanner:
    def __init__(self, root, excluded):
        # 把 root 保存为 self.root
        # 把 excluded 保存为 self.excluded
        ...
```

约定 root 传入 Path 对象，excluded 传入集合；先不增加类型转换或扫描功能。

再自己完成：
1. 创建 scanner_a：目录 Path("scripts")，排除集合 {".venv", ".git", "__pycache__", "output"}。
2. 创建 scanner_b：目录 Path("notes")，排除集合 {".git"}。
3. 分别打印两个对象的 root 与 excluded 属性。
4. 将 scanner_a.root 改为 Path("data")，再次打印两个对象的目录。

两个集合分别创建。集合打印顺序不固定，比较包含的名称即可。

从项目根目录、使用已有项目环境运行：

```powershell
python scripts/folder_scanner.py
```

若没有激活项目环境，可从项目根目录直接执行：

```powershell
& ".\.venv\Scripts\python.exe" "scripts\folder_scanner.py"
```

## 3. 验证对象各自保存配置（约 10 分钟）

修改前：scanner_a.root 为 scripts，scanner_b.root 为 notes。
修改 scanner_a.root 后：scanner_a.root 为 data，scanner_b.root 仍为 notes。
两个对象的 excluded 集合内容各自与创建时一致。

这一步修改的是已有对象的属性，不需要重新创建对象。目录名称在今天只是配置值，设置属性不会创建或扫描目录。

## 4. 理解检查（约 10 分钟）

用自己的话回答：
1. FolderScanner 和 scanner_a 分别是什么？
2. __init__ 在什么时候执行，为什么创建对象时不用手动传 self？
3. self.root = root 左边和右边分别表示什么？

完成标准：两个对象正确保存不同配置，修改一个对象的 root 后另一个不变，能解释初始化方法和 self 的作用。

每日任务开始时保存为 notes/ai/daywork/day8.md。具体学习过程、问题及解释等待今日任务完成后，统一写入 records/day8-record.md；当天结束再同步 progress_record.md。

收尾状态（2026-10-12）：用户在 scripts/file_scanner.py 实现 Folderscanner，保存 self.p、self.excluded，创建两个对象并运行得到 data notes。类与实例、初始化时机及 self 命名已讲解纠正。用户明确跳过更换排除集合、修改对象路径的简单验证并直接进入 Day 9；按此调整结束本日，不把跳过项写成实测通过。记录已统一整理到 records/day8-record.md。

