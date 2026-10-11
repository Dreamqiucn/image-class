from pathlib import Path
#import os
import sys
from count_labels import count_labels

#收集所有后缀
def collect_suffixes(root,excluded):

    suffixes =[]
    for item in root.rglob("*"):        
        #rglob是递归遍历所有文件夹，*表示所有文件
        if not item.is_file():
            continue
        if any(part in excluded for part in item.parts):
            continue
        suffixes.append(item.suffix or "无后缀")  #如果没有后缀就标记为无后缀
    return suffixes

#获得数目统计，实际上只是调用了count_labels模块
def count_files(path,excluded):
    suffixes = collect_suffixes(path,excluded)
    #获得所有后缀
    counts = count_labels(suffixes)#count_labels是导入的模块
    #导入的这个 数数模块 需要吃列表，而这个文件原生的是吃单个的，先遍历文件，参数不是列表
    return counts 

#打印而已    
def print_summary(counts):
    print("文件后缀统计结果：")
    for suffix, count in counts.items():#这两个参数按顺序排的，叫什么名字无所谓，for a，b in c.items()也可以
        print(f"{suffix}: {count}")
    print(f"总文件数: {sum(counts.values())}")    
if __name__ == "__main__":
    if len(sys.argv)<2:
        p=Path(input("请输入路径："))
        print(p.resolve())
        #绝对路径
        #print ("当前目录下的文件和文件夹：",sonfiles)
    else:
        p=Path(sys.argv[1])

    #sonfiles=[f.name for f in p.rglob("*") if f.name!=".venv"]
    #.name是为了字符串 不然就是WindowsPath('.venv')，rglob包括子文件夹。glob是只有这一层的
    # 这个只会去掉venv文件夹，不会去掉文件夹的内容
    # print(count_files(p, {".venv", ".git", "__pycache__"}))
    print_summary(count_files(p, {".venv", ".git", "__pycache__"}))