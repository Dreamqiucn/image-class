import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
plt.rcParams["font.sans-serif"] = ["Hiragino Sans GB", "Microsoft YaHei", "SimHei", "Songti SC"]
plt.rcParams["axes.unicode_minus"] = False
df=pd.read_csv("data/manifests/samples.csv")
counts=df["label"].value_counts()
#获得角色图片数量
# width_mean=df["width"].mean()
# height_mean=df["height"].mean()
# print(counts,width_mean,height_mean)
fig1,ax1=plt.subplots(figsize=(14,6))
ax1.bar(counts.index,counts.values)
#index是角色名，values是数量
plt.xticks(rotation=45,ha="right")
#名字倾斜45°，防止名字重叠
ax1.set_title("角色图片数量分布")
ax1.set_xlabel("角色名")
ax1.set_ylabel("数量")
fig1.tight_layout()
#底部自动留空

sample_rows=df.groupby("class_id").sample(1).sample(4)
fig2,axes=plt.subplots(1,4,figsize=(12,4))
for i in range(4):
    row=sample_rows.iloc[i]
    img_path="data/raw/"+row["path"]
    with Image.open(img_path) as image:
        rgb=image.convert("RGB")
        r=np.array(rgb)
    # print(row["label"],r.shape,r.mean())
    axes[i].imshow(r)
    axes[i].set_title(row["path"])
    # axes[i].axis("off")
    # 只关横轴刻度尺，不关横轴本身
    axes[i].set_xticks([])                                   
    axes[i].set_yticks([])   
    axes[i].set_xlabel(f'{row["width"]} x {row["height"]}')
    fig2.suptitle("随机图片")
fig2.tight_layout()
fig1.savefig("output/角色图片数目统计.png")
fig2.savefig("output/随机图片.png")

plt.show()