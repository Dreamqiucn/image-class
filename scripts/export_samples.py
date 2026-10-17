from pathlib import Path
import csv
from file_scanner import Imagesacnner
from datetime import datetime
import argparse

def save_samples(samples,p,output):
    (p / "output").mkdir(parents=True,exist_ok=True)
    timenow= datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
    # with open(f"{p}/output/samples_{timenow}.csv","w",encoding="utf-8-sig",newline="") as file:
    if output==None:
        (p / "output").mkdir(parents=True,exist_ok=True)
        output=(p.resolve()/"output/samples.csv")
        # print(output)
    output.parent.mkdir(parents=True,exist_ok=True)
    with open(output,"w",encoding="utf-8-sig",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["path","label"])
        for path,label in samples:
            writer.writerow([path,label])
        # print("输出成功："+str(p.resolve())+"\output\samples_"+timenow+".csv")
        print("输出成功："+str(output)+"\n")
    return output
def read_samples(csv_path):
    with open(csv_path,"r",encoding="utf-8-sig",newline="") as file:
        read=csv.DictReader(file)
        rows=list(read)
        counts={}
        #{}字典 ，[]列表
        #rows 是[{"path":"xxxx/xxxx.png","label":"cat"},{"path":"xxxx/xxxx.png","label":"cat"}]
        #是列表里面有好几个字典形式，字典的键是csv最顶端的那个，值是每一排的值
        for row in rows: 
        #row是{"path":"xxxx/xxxx.png","label":"cat"}
            # print(row["label"])
            #row["label"]就是字典里label的键值cat
            counts[row["label"]]=counts.get(row["label"],0)+1
            
        print("读回图片数目：",len(rows))#len列表的东西的数目
        print("类别统计：",counts)
if __name__ =="__main__":
    # p = Path(input("请输入路径"))
    parser=argparse.ArgumentParser(description="导出图片路径与类别")
    parser.add_argument("root",type=Path,help="图片数据根目录")
    parser.add_argument("--output",type=Path,help="输出csv文件路径")
    args=parser.parse_args()
    p = args.root
    output=args.output
    excluded={".venv", ".git", "__pycache__", "output"}
    included={".jpg", ".png", ".jpeg", ".webp"}
    scanner=Imagesacnner(p,excluded,included)
    samples=scanner.collect_samples()[1]
    # print(samples)
    csv_path=save_samples(samples,p,output)
    read_samples(csv_path)
