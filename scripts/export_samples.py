from pathlib import Path
import csv
from file_scanner import Imagesacnner
from datetime import datetime
import argparse
import json
def save_samples(samples,p,output):
    # (p / "output").mkdir(parents=True,exist_ok=True)
    timenow= datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
    # with open(f"{p}/output/samples_{timenow}.csv","w",encoding="utf-8-sig",newline="") as file:
    with open(output,"w",encoding="utf-8-sig",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["path","label"])
        for path,label in samples:
            writer.writerow([path,label])
        # print("输出成功："+str(p.resolve())+"\output\samples_"+timenow+".csv")
        print("输出samples.csv成功："+str(output)+"\n")
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
        return rows,counts
    return rows,counts
def read_json():
    with open(config_path,"r",encoding="utf-8-sig") as file:
        config=json.load(file)
        #set()是集合形式，一个东西只会出现一次而不是列表，用{}表示，但一般{}是字典
        excluded=set(config["excluded"])
        included=set(config["included"])
        #json里面不能放集合！heis
        return excluded,included
def save_summary():
    summary={
        "root": p.resolve().as_posix(),
        "csv_path": output.resolve().as_posix(),
        "total": len(rows),
        "counts": counts
    }
    summary_path=output.parent /"summary.json"
    with open(summary_path,"w",encoding="utf-8-sig") as file:
        json.dump(summary,file,ensure_ascii=False,indent=2)
        #dump是写入，四个参数分别是 内容，文件在哪，允许中文等非ascii字符，缩进两格
    print("输出summary.json成功："+summary_path.resolve().as_posix())
if __name__ =="__main__":
    #配置命令行的东西
    parser=argparse.ArgumentParser(description="导出图片路径与类别")
    parser.add_argument("root",type=Path,help="图片数据根目录")
    parser.add_argument("--output",type=Path,help="输出csv文件路径")
    parser.add_argument("--config",type=Path,help="配置文件的路径")
    #应该是输入python scripts/export_samples.py 1 , ./1 , config.scanner.json，不过--代表不是必须输入
    
    args=parser.parse_args() #让args等于命令行里面获得到的值
    p = args.root

    #检查output是否加了
    output=args.output
    if output==None:
        (p / "output").mkdir(parents=True,exist_ok=True)
        output=(p.resolve()/"output/samples.csv")
    output.parent.mkdir(parents=True,exist_ok=True)

    #检查config是否加了，获取到excluded和included
    config_path=args.config
    if config_path==None:
        config_path=Path("config/scanner.json")
    excluded=read_json()[0]
    included=read_json()[1]
    #或者excluded,included=read_json()

    #获得图片列表
    scanner=Imagesacnner(p,excluded,included)
    samples=scanner.collect_samples()[1]
    
    #保存列表什么的到csv文件
    save_samples(samples,p,output)
    #读一下，并获得csv行数和文件计数
    rows,counts=read_samples(output)
    #生成总计文件
    save_summary()