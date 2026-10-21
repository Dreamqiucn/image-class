from pathlib import Path
from PIL import Image
from file_scanner import Imagesacnner,Folderscanner
import json
import csv
def image_inf():
    global photos_number
    global photos_inf
    for i in photos:
        try:
            with Image.open(i) as image:
                image.load()
                # print("图片名称",i.stem,"文件后缀",i.suffix,"宽x高",image.size[0],"x",image.size[1],"颜色模式",image.mode)
                photos_number+=1
                photos_inf.append({
                    "图片名称":i.stem,
                    "图片后缀":i.suffix,
                    "宽":image.size[0],
                    "高":image.size[1],
                    "颜色模式":image.mode
                })
        except OSError as error:
            print("图片无法读取：", i, error)
            continue
def save():
    global summary
    csv_path = output_dir/"photos_samples.csv"
    json_path=output_dir /"photos_labels.json"
    summary_path=output_dir/"photos_summary.json"

    with open(csv_path,"w",encoding="utf-8-sig",newline="") as file:
        writer= csv.writer(file)
        writer.writerow(["Path","Label"])
        for path,label in samples:
            writer.writerow([path,label])
    print("输出photos_sample.csv成功："+csv_path.resolve().as_posix())

    with open(json_path,"w",encoding="utf-8")as file:
        json.dump(photos_idx,file,ensure_ascii=False,indent=2)
    print("输出photos_labels.json成功："+json_path.resolve().as_posix())

    with open(summary_path,"w",encoding="utf-8") as file:
        json.dump(summary,file,ensure_ascii=False,indent=2)
    print("输出photos_summary.json成功："+summary_path.resolve().as_posix())
def first():
    global labels
    global photos_set
    global photos
    global photos_idx
    global output_dir
    if not p.exists():
        raise OSError(f"路径不存在：{p.resolve()}")
    if not p.is_dir():
        raise OSError(f"路径不是文件夹：{p.resolve()}")
    output_dir = p / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    for i in scanner.collect_samples()[1]:
        photos.append(Path(i[0]))
    photos_set=set(scanner.collect_samples()[1])#集合去重
    
    for path, label in photos_set:
        labels.append(label)
        labels=sorted(set(labels))#类型去重

    for idx,label in enumerate(labels):#enumerate先返回编号，再返回内容
        photos_idx[label]=idx
if __name__ == "__main__":
    p = Path(input("请输入路径"))
    output_dir=Path('')
    excluded={".venv", ".git", "__pycache__", "output"}
    included={".jpg", ".png", ".jpeg", ".webp"}
    photos_inf=[]
    photos_number=0
    photos=[]
    photos_set={}
    labels=[]#类型列表
    photos_idx={}

    while True:
        try:
            scanner=Imagesacnner(p,excluded,included)
            dirs,samples=scanner.collect_samples()
            first()
            image_inf()
            summary={
                "图片数目":photos_number,
                "列表数目":len(labels),
                "所有图片":photos_inf
            }
            print(summary)
            save()
            break
        except OSError as Error:
            p = Path(input(str(Error)+"\n"+"请重新输入"))