10.9 Day 1
根据dsh建了个环境，尽可能手动吧，有不会的问ai，但执行还是我自己，需要理解
10.10 Day 2+3
弄了个遍历数数的，查各种文件后缀的文件有几个，好累
10.11 Day 4+5
day4 只是拆分成了几个板块，没学东西
day5 把自动补全代码功能关了，学的时间慢了，但学到新东西了，创建文件，csv，和文件操作有关的
10.12 Day 6+7+8+9
这天是晚自习带电脑去的，因为提前把作业写完了
day6 只是优化一下输入逻辑
day7 只是第一周的善后工作，比如说文件命名加上时间，优化了泔水，以及第一周readme
day8 学习类，对象，给我一种局部环境的感觉
day9 把查找，统计的逻辑放到类/对象里面
10.13 Day10
day10 继承 重写 super调用,重新在类里定义函数就是重写，super().就是调用父类的函数
10.14 Day11
day11 关于错误回弹，raise try except
10.15 Day12
day12 并没有学什么新语法，只是完成任务
10.16 Day13+14
day13 新建文件export_samples.py专门输出csv统计文件的，之后学习了csv的DictReader,读csv文件的
day14 只是第二周的善后工作罢了，
10.17 Day15+16
day15 命令行参数使用，但真有人这么用吗，给ai用的吧
day16 json文件的读取与写入
10.18 Day17+18
day17 读取图片信息
day18 是修改没用的棍母，直接跳了
10.21 Day19+20+21
day19 距离上一次写是三天前了，前两天光ai生成小视频了,day19学了个set()集合去重，sort（）排序，en....()生成编号的
day20 最后的python任务，串联起流程，生成json和csv
day21 依旧总结
10.22 Day22+23
day22 学习Numpy，嗯，刚刚开始没强度
day23 学习切区域，筛选
10.23 Day24+25
day24 学了转换reshape，transpose换行列表轴的序列 .T把顺序正着的顺序完全换过来
day25 学习线性运算，uint8类型，astype转化数组类型
10.24 Day26
day26 简单的append，shape[0]=len（a），线性运算，keepdims=True是每个用列表来存东西
10.25 Day27
day27 今天算是深刻复习了一遍numpy，之前学的浅，好多没理解到位，这东西挺抽象的，建了个个knowledge文件夹用于整理知识点
10.26 Day28
day28 收工Numpy！
10.27 Day29+30
day29 学习pandas，一维series，二维dataframe
day30 iloc和loc，读取csv
10.28 Day31+32
day31 学了个筛选，去重，去空的
day32 学习了占比，数目，数据计算这一种
10.29 Day33
day33 映射map是映射字典的，merge是根据另外一个表的进行补充的，都是补充数组的
10.30 Day34
day34 生日快乐！计算思维电脑课做的，只是让我完成任务
11.1 Day35
day35 整体复习了一遍Numpy和pandas，做了一万个问题
11.2 Day36+37+38
day36 入门matplotlib，先把这个单词背了 柱状图 bar
day37 直方图+获取图片亮度 hist
day38 显示图片+多张ax imshow
11.3 Day39+40+41+42
day39 折线图来一个 plot
day40 学习 混淆矩阵 和热力图ax.imshow(np数组，cmap=“颜色”)
day41 完成了贯穿Numpy pandas matplotlib的小任务 
day42 没啥用，加了个在学pytorch之前的巩固numpy pandas matplotlib的周
11.4 Day43+44
day43 学习numpy的concentrate和stack
day44 学习Numpy的where查找和clip限制，以及个argmax找下标，@矩阵乘法
11.5 Day45
day45 学习Numpy的随机值，随机种子（不同的东西输入它就保持同一个结果）以及打乱顺序
11.8 Day46+47+48+49
day46 学习pandas的合并表，把数字字符串变成数值，自动填充未nan的值
day47 分组agg，列的loc条件判断
day48 matplotlib散点图
day49 修整
11.9 Day50+51
day50 开始pytorch！
day51 建立个tensor数组，tensor和numpy的互换
11.11 Day52+53
day52 tensor的运算，cpu，gpu转换，unsqueeze加减轴
day53 求导
11.12 Day54
day54 构建个小网络
11.13 Day55
day55 计算损失值，分数，目标数这一种
11.14 Day56+57
day56 重新捋一遍pytorch这周学的东西
day57 完成个农村自建dataset
11.15 Day58
day58 在day57基础上修改，学习dataloader分组
11.16 Day59
day59 训练集分流，反转图片，像素换到0-1
11.17 Day60
day60 真正测试训练，loss越来越小，20次训练
11.18 Day61
day61 再次狠狠理解MLP，梳理训练流程，今天完成的任务其实只是制定一组之后光训练它，加了新的照片gpt.png和shiomi3.png,这是开始学有史以来最难的一天
11.19 Day62+63
day62 实现完整的训练流程，写图片处理类photos，设定model，创建dataloader，for训练，在每个for里遍历完创建的dataloader的全部内容，先获得logits，算loss，backward，再step优化
day63 复盘week9的内容
11.20 Day64
day64 卷积模型开始入门
11.21 Day65
day65 给day64多加几道加工工艺
11.22 Day66+67+68
day66 给CNN加上训练流程
day67 加上验证阶段
day68 加上csv导出，matplotlib画折线图
11.23 Day69+70
day69 导出day68的权重pth，接入day69，专门用来预测是哪个图片的
day70 收尾week10
11.23-26 Day71 72 73 74
准备图片素材
11.26 Day75 76
day75 写了个分离train val test数据集的脚本
day76 通过matpltlib展示图片数量，随机四张图片
以及再次清洗与增加图片素材
11.27 Day77 78 79 80
day77 复盘这week11
day78 认识resnet需要的主分支和跳跃分支
day79 了解batchnorm，以及它的train eval模式
day80 串一遍残差完整流程
11.28 Day81 82
day81 写block类来代替流程
day82 把昨天的block改成可以自定义输入与输出通道的