# Day 19：集合去重、排序与类别编号

布置日期：2026-10-21。约 60 分钟任务量，不限制实际耗时。Day 17 已完成；Day 18 按用户要求跳过。今天按原计划学习集合、排序和 enumerate，将文字类别转换为整数编号。Day 20 保留工具整合，Day 21 休息或补漏，Day 22 再开始 NumPy。

## 今天的目标

从现有扫描器的样本列表出发，做到三件事：同一路径只保留一条样本；取得去重并排序的类别；从 0 开始编号，并将类别到编号的映射保存为 JSON。核心代码由用户编写，不重做 Day 18 的宽高/颜色模式 CSV。

## 1. set：去重与判断是否出现过（约 10 分钟）

```python
names = ["dog", "cat", "dog"]
unique_names = set(names)
print(unique_names)
```

结果只保留 cat 和 dog，但集合不保证按固定顺序排列。不要对集合使用 unique_names[0]。

另一个用途是记录已经出现的内容：

```python
seen = set()
seen.add("a.jpg")
print("a.jpg" in seen)  # True
```

set() 创建空集合；{} 是空字典。今天用集合完成成员判断，不要求背集合运算大全。

## 2. sorted：让类别顺序固定（约 10 分钟）

```python
classes = sorted(set(names))
print(classes)  # ['cat', 'dog']
```

先 set 去掉重复类别，再 sorted 得到排好顺序的新列表，原始 names 不会因此被修改。sorted 是函数；列表自己的 sort() 会修改原列表，其返回值是 None，不要写 classes = names.sort()。

同一组类别无论扫描输入顺序如何，都能得到相同排序。字符串默认排序不等于中文拼音排序；本日直接使用默认顺序，不引入额外排序库。

## 3. enumerate：同时得到位置编号和内容（约 10 分钟）

```python
for index, label in enumerate(classes):
    print(index, label)
```

输出：

```text
0 cat
1 dog
```

enumerate 默认从 0 开始，每次给出 (编号, 元素)。index 和 label 是普通变量名，含义由得到的数据决定。也可以 enumerate(classes, start=1)，但今天为了给类别编号使用默认的 0 开始。

将每一项存进字典，就能建立 label → index 的对应关系；例如 class_to_idx['cat'] 取得 0。用户自行写循环和赋值，不要求学习字典推导式才能完成。

后续训练中，整数编号可以用于表示类别；模型输出的编号也需要用保存的对应关系解释。排序保证同一组类别的编号稳定，不保证增加/删除类别后旧编号仍不变，因此要保存并复用映射。

## 4. 接上现有样本（约 20 分钟）

建议新建 C:/Users/24718/Desktop/image-class/scripts/prepare_labels.py；也接受在现有脚本新增合适函数。不要命名为 json.py，避免遮蔽标准库。无需安装新依赖，沿用当前项目环境。

现有接口：

```python
samples = scanner.collect_samples()[1]
```

samples 每一项是 (路径字符串, 类别)，不是只有路径，也不是图片对象。后续处理要保留两项，不要为了去重丢掉标签。

自己实现：

1. 遍历 samples，使用一个空集合记录已经见过的路径，用另一个列表保存去重后的 (path, label)。路径出现过就跳过，否则记录路径并保留样本。
2. 从去重后的样本收集类别，用 set 去重，再 sorted 排序。
3. 用 enumerate 从 0 开始，建立 class_to_idx 字典。
4. 打印去重前后数量、类别列表和 class_to_idx。
5. 沿用已学 JSON 保存方式，将映射保存在输入根目录的 output/class_to_idx.json。父目录可用 mkdir(parents=True, exist_ok=True) 创建；使用 ensure_ascii=False、indent=2 便于查看中文类别。

例如输入：

```python
samples = [
    ("cat/a.jpg", "cat"),
    ("dog/b.jpg", "dog"),
    ("cat/a.jpg", "cat"),
]
```

应得到两条样本，类别 ['cat', 'dog']，映射 {'cat': 0, 'dog': 1}。去重以完整路径字符串为判断依据；同一个文件名位于不同目录仍是不同路径。现有扫描器已输出 resolve().as_posix()，今天沿用该表示，不要求另写跨平台路径身份系统。

这只是路径去重：不同路径下即使图片内容完全相同，也不会因此去掉。今天不做文件哈希或图像内容查重。

## 5. 完成标准（约 10 分钟）

- 现有样本进入自己的处理逻辑，得到去重样本、排好顺序的类别以及类别到整数的映射。
- 现有扫描器正常情况下往往本来就没有重复路径。临时使用 samples + samples[:1] 加入一条重复记录，证明去重后数量不变；不用复制真实图片制造重复。
- 将输入样本顺序反过来，类别排序和 class_to_idx 不变；不要求反复扫描目录来测试这个纯数据处理逻辑。
- 保存的 JSON 可以读回，其键是类别字符串，值是从 0 开始的整数，与内存字典一致。类别名称以当前实际目录为准，不要求必须叫 cat/dog。
- 能说明 set 为什么适合去重、为什么编号前要 sorted、enumerate 每次给出哪两项。

今天只布置，不提前记完成。任务保存于 notes/ai/daywork/day19.md；问答先在聊天中进行，完成后再统一创建 records/day19-record.md、更新进度。核心代码由用户编写，不自动暂存、提交或推送 Git。

## 收尾状态：2026-10-21

按用户调整范围完成。用户在 inspect_images.py 中对样本元组 set 去重，提取标签后 sorted(set(labels)) 排序，用 enumerate 建立类别→整数的 photos_idx，最终映射为 丰川祥子: 0、汐见萤: 1。用户不要求补充去重前后数量、类别和字典等额外终端打印。

实际还实现了 output/labels.json 保存；在已有 output 的临时真实图片目录中运行脚本，正常三条样本、倒序并附加重复的四条样本均得到三项样本集合和相同类别编号，保存 JSON 独立读回一致。样本集合按 (路径, 类别) 元组去重，不是通用仅按路径去重；原 photos 读图列表未改为去重结果。save_json 暂依赖父目录存在，未声称自动创建目录。按当前扫描器和核心练习范围收尾，整合留到 Day 20。

详细过程与问答统一保存在 records/day19-record.md。未代改核心代码，未 Git 暂存、提交或推送。下一学习日 Day 20，之后 Day 21 休息或补漏、Day 22 NumPy。
