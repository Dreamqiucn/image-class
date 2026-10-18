from pathlib import Path
from PIL import Image
from file_scanner import Imagesacnner,Folderscanner

def image_inf():
    for i in photos:
        with Image.open(i) as image:
            width,height = image.size
            print("图片名称",i.stem,"文件后缀",i.suffix,"宽x高",width,"x",height,"颜色模式",image.mode)

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
            print(photos)
            image_inf()
            break
        except OSError as Error:
            p = Path(input(str(Error)+"\n"+"请重新输入"))