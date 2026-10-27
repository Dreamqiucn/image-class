import pandas as pd
s=pd.Series([1,2,3],name="first")
print(s,s.dtype,s.shape)
list1=[
    {"path":"1/丰川祥子/saki.webp","label":"丰川祥子","width":"x"},
    {"path":"1/汐见萤/shiomi.webp","label":"汐见萤","width":"y"},
    {"path":"1/汐见萤/shiomi2.webp","label":"汐见萤","width":"z"}
]
list2=pd.DataFrame(list1)
print(list2,list2.shape,list2.dtypes,list2.columns,list2.head(2),list2["label"])