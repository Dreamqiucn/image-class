import pandas as pd
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
day30()