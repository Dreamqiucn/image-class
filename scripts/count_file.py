from pathlib import Path
#import os
import sys
from count_labels import count_labels
def count_files(path):
    suffixes = []
    counts ={}
    for item in path.rglob("*"):
        #rglob是递归遍历所有文件夹，*表示所有文件
        if not item.is_file():            #如果不是文件
            continue
        if any(part in {".venv",".git","__pycache__"} for part in item.parts):            #如果是.venv或.git文件夹
            continue
        suffixes.append(item.suffix or "no_suffix")  #如果没有后缀就标记为no_suffix
        #后缀=item.suffix
        # counts[suffix] = counts.get(suffix,0) + 1
    counts = count_labels(suffixes)
    #导入的这个 数数模块 需要吃列表，而这个文件原生的是吃单个的，先遍历文件，参数不是列表
    return counts
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
    print(count_files(p))
