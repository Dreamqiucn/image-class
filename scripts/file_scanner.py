from pathlib import Path

class Folderscanner:
    def __init__(self,p,excluded,included):#默认第一个参数代表对象自己
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
p = Path(".")
excluded={".venv", ".git", "__pycache__", "output"}
included={".jpg", ".png", ".jpeg", ".webp"}

scanner=Folderscanner(p,excluded,included)
scanner_photo=Imagesacnner(p,excluded,included)
print(scanner.count())
print(scanner_photo.count())