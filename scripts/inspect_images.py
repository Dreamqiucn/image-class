from pathlib import Path
from PIL import Image
from file_scanner import Imagesacnner,Folderscanner
import json
def image_inf():
    for i in photos:
        with Image.open(i) as image:
            width,height = image.size
            print("图片名称",i.stem,"文件后缀",i.suffix,"宽x高",width,"x",height,"颜色模式",image.mode)
def save_json():
    json_path=p /"output/labels.json"
    with open(json_path,"w",encoding="utf-8")as file:
        json.dump(photos_idx,file,ensure_ascii=False,indent=2)
    print("输出labels.json成功："+json_path.resolve().as_posix())

if __name__ == "__main__":
    p = Path(input("请输入路径"))
    excluded={".venv", ".git", "__pycache__", "output"}
    included={".jpg", ".png", ".jpeg", ".webp"}
    while True:
        try:
            scanner=Imagesacnner(p,excluded,included)
            photos=[]
            for i in scanner.collect_samples()[1]:
                photos.append(Path(i[0]))
            photos_set=set(scanner.collect_samples()[1])#集合去重
            labels=[]#类型列表
            for path, label in photos_set:
                labels.append(label)
            labels=sorted(set(labels))#类型去重
            photos_idx={}
            for idx,label in enumerate(labels):#enumerate先返回编号，再返回内容
                photos_idx[label]=idx
            image_inf()
            save_json()
            break
        except OSError as Error:
            p = Path(input(str(Error)+"\n"+"请重新输入"))