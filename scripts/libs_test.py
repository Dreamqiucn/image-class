import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
# 设置中文字体为微软雅黑
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

paths=[("1/汐见萤/shiomi2.webp","汐见萤"),("1/汐见萤/shiomi.webp","汐见萤"),("1/丰川祥子/saki.webp","丰川祥子")]
photos=[]
for path in paths:  
    with Image.open(path[0]) as image:
        image1=image.convert("RGB")
        pixel=np.array(image1)
        pixel_mean=pixel.mean()
        photos.append([path[1],path[0],float(pixel_mean)])
photos=pd.DataFrame(photos)
photos=photos.rename(columns={0:"label",1:"path",2:"pixel_mean"})
photos_mean=photos.groupby("label")["pixel_mean"].mean()
print(photos_mean)
fig,ax=plt.subplots()
bars=ax.bar(photos_mean.index,photos_mean.values)
ax.bar_label(bars)
plt.show()