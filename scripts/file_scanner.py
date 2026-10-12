from pathlib import Path

class Folderscanner:
    def __init__(self,p,excluded):#默认第一个参数代表对象自己
        self.p=p
        self.excluded=excluded
if __name__ == "__main__":
    p = Path("data")
    p2 = Path("./notes")
    excluded={".venv", ".git", "__pycache__", "output"}
    scanner_a=Folderscanner(p,excluded)
    scanner_b=Folderscanner(p2,excluded)
    print(scanner_a.p,scanner_b.p)