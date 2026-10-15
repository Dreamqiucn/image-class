from pathlib import Path

class Folderscanner:
    def __init__(self,p,excluded,included):#默认第一个参数代表对象自己
        if not p.exists():
            raise OSError(f"路径不存在：{p.resolve()}")
        if not p.is_dir():
            raise OSError(f"路径不是文件夹：{p.resolve()}")
        self.p=p
        self.excluded=excluded
        self.included=included
    def collect_suffixes(self):
        suffixes=[]
        for i in self.p.rglob("*"):
        #这个i得到的是路径
            if not i.is_file():
                continue
            if any(part in self.excluded for part in i.parts):#任何部分（/a/b/c/包含在excluded里面，对于i的每一部分来说）
                continue
            suffixes.append(i.suffix or "无后缀")
        return suffixes
    def count(self):
        counts={}
        for i in self.collect_suffixes():
            counts[i]=counts.get(i,0)+1
        return counts
class Imagesacnner(Folderscanner):
    def collect_suffixes(self):
        suffixes = super().collect_suffixes()
        photosuffixes=[]

        for i in suffixes:
            inew=i.lower()#转小写
            if inew not in self.included:
                continue
            photosuffixes.append(inew)
        return photosuffixes
    def collect_samples(self):
        dirs=[]
        photos=[]
        for i in self.p.iterdir():#先扫第一层 和glob("*")效果一样
            if not i.is_dir() or i.name in self.excluded:
                continue  
            dirs.append(str(i.resolve()))#把文件夹的路径加到列表里面
            # scanner_i=Imagesacnner(i,excluded,included)
            for ii in i.rglob("*"):#再分别扫文每个件夹的图片
                # print(str(i.resolve()),scanner_i.count())
                if not ii.is_file():
                    continue

                if any(part in self.excluded for part in ii.parts):
                    continue

                if ii.suffix.lower() not in self.included:
                    continue
                photos.append((str(ii.resolve()),i.name))
        return dirs,photos
    def count_categories(self):
        sample=self.collect_samples()[1]#调用类里面自己的函数，使用self就可以
        photocount={}
        for path,label in sample:
            photocount[label]=photocount.get(label,0)+1
        return photocount
if __name__=="__main__":
    p = Path(input("请输入路径"))
    excluded={".venv", ".git", "__pycache__", "output"}
    included={".jpg", ".png", ".jpeg", ".webp"}
    while True:
        try:
            scanner=Folderscanner(p,excluded,included)
            scanner_photo=Imagesacnner(p,excluded,included)
            print("文件夹",scanner_photo.collect_samples()[0])
            print("图片分类",scanner_photo.collect_samples()[1])
            print("图片种类",scanner_photo.count_categories())

            print("各文件数目",scanner.count())
            print("图片数目",scanner_photo.count())
            
            break
        except OSError as Error:
            p = Path(input(str(Error)+"\n"+"请重新输入"))
