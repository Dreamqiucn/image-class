from pathlib import Path

class Folderscanner:
    def __init__(self,p,excluded):#默认第一个参数代表对象自己
        self.p=p
        self.excluded=excluded
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
if __name__ == "__main__":
    p = Path(".")
    excluded={".venv", ".git", "__pycache__", "output"}
    scanner=Folderscanner(p,excluded)
    print(scanner.count())