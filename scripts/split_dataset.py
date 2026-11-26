import pandas as pd
import numpy as np
import csv
df = pd.read_csv("data/manifests/samples.csv")
df=df[df["exclude_from_train"]==0]
#只留可以使用的数据
rng=np.random.default_rng(42)
#随机种子，为了保持得到的值永远一样
train_parts=[]
val_parts=[]
test_parts=[]
for class_id in sorted(df["class_id"].unique()):
    #sorted是从小到大排序class_id，unique是去掉重复的，只留单独的class_id
    sub_df=df[df["class_id"]==class_id]
    #取子列
    group_id=rng.permutation(sorted(sub_df["group_id"].unique()))
    #打乱子列的group_id的顺序
    n_val=int(len(group_id)*0.15)
    n_test=int(len(group_id)*0.15)
    n_train=len(group_id)-n_val-n_test
    #实际上-两个n_val就好了
    train_group=group_id[:n_train]
    val_group=group_id[n_train:n_train+n_val]
    test_group=group_id[n_train+n_val:]
    #切出来train val test需要的group_id
    #下面是对应group_id取子列里面找自己需要的内容
    # 注意，这里是加到列表里面了，因为加到列表里最后一起concat比每轮都concat效率高
    train_parts.append(sub_df[sub_df["group_id"].isin(train_group)])
    val_parts.append(sub_df[sub_df["group_id"].isin(val_group)])
    test_parts.append(sub_df[sub_df["group_id"].isin(test_group)])
train_df = pd.concat(train_parts, ignore_index=True)
val_df = pd.concat(val_parts, ignore_index=True)
test_df = pd.concat(test_parts, ignore_index=True)

#下面是检验
# assert len(train_df)+len(val_df)+len(test_df)==len(df)
# assert set(train_df["group_id"])&set(val_df["group_id"])==set()
# assert set(train_df["group_id"])&set(test_df["group_id"])==set()
# assert set(test_df["group_id"])&set(val_df["group_id"])==set()
# assert train_df["class_id"].nunique()==29
# assert val_df["class_id"].nunique()==29
# assert test_df["class_id"].nunique()==29

train_df.to_csv("data/manifests/train_csv.csv",index=False,encoding="utf-8-sig")
val_df.to_csv("data/manifests/val_csv.csv",index=False,encoding="utf-8-sig")
test_df.to_csv("data/manifests/test_csv.csv",index=False,encoding="utf-8-sig")
