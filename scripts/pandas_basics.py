import pandas as pd
import csv
def day29():
    s=pd.Series([1,2,3],name="first")
    print(s,s.dtype,s.shape)
    list1=[
        {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":"x"},
        {"path":"1/汐见萤/shiomi.webp","label":"汐见萤","width":"y"},
        {"path":"1/汐见萤/shiomi2.webp","label":"汐见萤","width":"z"}
    ]
    list2=pd.DataFrame(list1)
    print(list2,list2.shape,list2.dtypes,list2.columns,list2.head(2),list2["label"])
def day30():
    csv_path="1/output/samples.csv"
    df = pd.read_csv(csv_path,encoding="utf-8-sig")
    print(df,df.shape,df.columns)
    print(df["Path"])#一维
    print(df[["Path"]])#二维
    print(df[["Path","Label"]])
    print(df.iloc[:2])
    print(df.iloc[-1])
    print(df.iloc[0])
    dfcopy=df.copy()#复制一下
    dfcopy.index=[10,20,30]#改变索引 列的
    print(dfcopy.iloc[1],dfcopy.loc[20])#iloc是查数目找，loc是查标签索引找
def day31():
    list1=[
        {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":"x"},
        {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":"x"},
        {"path":"1/丰川祥子/saki.webp","label":None,"width":None},
        {"path":"1/汐见萤/shiomi.webp","label":"汐见萤","width":"y"},
        {"path":"1/汐见萤/shiomi2.webp","label":"汐见萤","width":"z"}
    ]
    list2=pd.DataFrame(list1)
    print(
        list2[
        (list2["label"]=="丰川祥子")
        &
        (list2["width"]=="x")
        ]
        )
    print(list2.isna().sum())
    print(list2.dropna(subset=["path","label"]))
    print(list2.drop_duplicates(subset=["path"]))
def day32():
    list1=[
        {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":1},
        {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":2},
        {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":None},
        {"path":"1/汐见萤/shiomi.webp","label":"汐见萤","width":4},
        {"path":"1/汐见萤/shiomi2.webp","label":"汐见萤","width":5}
    ]
    l=pd.DataFrame(list1)
    print(l["path"].value_counts())
    print(l["width"].value_counts(normalize=True))
    print(l.groupby("label").size())
    print(l.groupby("label")["width"].mean())
def day33():
    rows = [
        {"path": "A/a.jpg", "label": "A"},
        {"path": "B/b.jpg", "label": "B"},
        {"path": "A/c.jpg", "label": "A"},
        {"path": "C/d.jpg", "label": "C"},
    ]
    rows = pd.DataFrame(rows) 
    new={"A":"x","C":"y"}
    rows["n"]=rows["label"].map(new)
    print(rows)
    print(rows[rows["n"].isna()])
    new["B"]="z"
    rows["n"]=rows["label"].map(new)
    print(rows)
    rows2=pd.DataFrame({
    "label": ["A", "B"],
    "n": [0, 1],
    "dream":[1,2]
    })
    rows=rows.merge(rows2,on="label",how="left")
    print(rows)
def day34():
    rows = [
        {"path": "A/a.jpg", "label": "A"},
        {"path": "A/a.jpg", "label": "A"},
        {"path": "A/b.jpg", "label": None},
        {"path": "A/c.jpg", "label": "A"},
        {"path": "B/d.jpg", "label": "B"},
    ]
    rows=pd.DataFrame(rows)
    rows=rows.dropna(subset=["label","path"])
    rows=rows.drop_duplicates(subset="path")
    rows.to_csv("output/rows.csv",index=False,encoding="utf-8-sig")
    counts=rows["label"].value_counts()
    ratio=rows["label"].value_counts(normalize=True)
    stats=pd.DataFrame({
        "counts":counts,
        "ratio":ratio
    }).reset_index()
    print(stats)
    stats.to_csv("output/stats.csv",index=False,encoding="utf-8-sig")
    with open("output/stats.csv","r",encoding="utf-8-sig",newline="")as file:
        reader=csv.DictReader(file)
        print(list(reader))
day34()
