# Day 12：文件夹名作为图片类别

日期：2026-10-14。任务量约 60 分钟，不限制实际耗时。核心代码由用户实现；沿用 scripts/file_scanner.py 中的 Imagesacnner。

## 目标与输入输出（约 10 分钟）

之前的 count 按后缀统计。今天以输入数据根目录的第一层子目录名作为类别，收集每张图片的路径与标签，再统计每个类别数量，为后续 CSV 清单与模型数据读取准备。

示例目录：

```text
sample_images/
├── cat/
│   ├── a.jpg
│   ├── backup/
│   │   └── b.PNG
│   └── readme.txt
├── dog/
│   └── c.jpeg
├── output/
│   └── ignored.jpg
└── loose.jpg
```

本日约定：第一层 cat、dog 是类别；cat 内子文件夹的图片仍归 cat。根目录散放的 loose.jpg 没有类别，本日跳过。按 excluded 排除目录、按 included 判断图片后缀并转小写；不检查图片真实内容，不下载数据集。空类别可以不出现在统计字典中，空数据根目录返回空列表和空字典。

样本列表的形状示意（顺序不作为验收要求）：

```python
[
    (Path("sample_images/cat/a.jpg"), "cat"),
    (Path("sample_images/cat/backup/b.PNG"), "cat"),
    (Path("sample_images/dog/c.jpeg"), "dog"),
]
```

类别统计：{"cat": 2, "dog": 1}。

## 两个关键概念（约 10 分钟）

- self.p.iterdir() 只遍历根目录第一层，方便确定哪个文件夹代表哪个类别。
- category_dir.rglob("*") 继续遍历该类别下全部层级的文件。
- category_dir.name 是类别文件夹的名字；不能直接把每个图片的 parent.name 当标签，否则 cat/backup/b.PNG 会被错标为 backup。
- (image_path, label) 是一个二元素元组；把多个这样的元组放进列表，保存路径与标签的对应关系。
- for image_path, label in samples 可以解包一条记录，与之前 items() 解包两个值相似。

## 动手实现（约 30 分钟）

给 Imagesacnner 增加两个方法，保留原有 count 与 collect_suffixes：

```python
def collect_samples(self):
    # 返回 [(图片的 Path, 类别字符串), ...]
    pass

def count_categories(self):
    # 调用 collect_samples，返回 {类别: 数目}
    pass
```

collect_samples 的顺序提示：
1. 建立空列表。
2. 遍历 self.p 的第一层，跳过文件与 excluded 中的类别目录。
3. 在每个类别目录中递归遍历，跳过非文件、位于排除目录中的文件和不支持的后缀。
4. 将 (图片路径, 当前第一层类别目录名) 加入列表。
5. 循环结束后返回列表。

计数沿用熟悉的 counts[label] = counts.get(label, 0) + 1 思路。这里只给提示，不要求逐字照示例实现。

主程序创建图片扫描器后，调用并打印 count_categories 的结果；继续使用 Day 11 的异常处理与重试。不要求重写已有统计方法，不增加 CSV 导出或图片训练任务。

## 简短验收（约 10 分钟）

准备一个方便的小目录，例如上面的 cat/dog 样本，可以使用已有图片；只按后缀判断时，空测试文件也能检查扫描逻辑。

一次有意义的验证应包括类别名、嵌套图片、大小写后缀、非图片、排除目录和根目录散放图片：列表路径与标签正确，对应计数 cat: 2、dog: 1。文件顺序可能变化，不比较列表排列顺序。空数据根目录返回 [] 和 {}。

理解两点：
1. 为什么先用 iterdir 找类别，再用 rglob 找图片？
2. cat/backup/b.PNG 的标签为什么仍是 cat？

已有 Day 11 输入检查不要求机械重复全套。根据实际代码与关键理解收尾，不把程序运行成功等同于全部理论掌握。

任务在开始时保存；本日实际过程、问题与验证结果，等任务完成后才统一更新 records/day12-record.md 和总进度。未完成前不提前创建 Day 12 学习记录。Git 提交与推送由用户操作。

## 收尾状态：2026-10-15

核心任务完成。用户实际返回 (dirs, photos)，路径保存为绝对路径字符串，功能成立。修正类别目录筛选以及内部文件、排除路径段、图片后缀筛选后，独立样本实际结果 cat: 2、dog: 1；三条图片路径与标签正确，嵌套图片仍归 cat。非图片、目录本身、根目录散放图片与排除目录正确跳过；空目录返回 ([], []) 与 {}，实际脚本运行正常。详细过程与问题统一保存在 records/day12-record.md，未代改核心代码或提交、推送 Git。
