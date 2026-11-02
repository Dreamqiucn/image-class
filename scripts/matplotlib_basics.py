import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
labels=["a","b","c"]
counts=[5,3,7]
values = [10, 20, 30, 70, 80, 90]
# pixels=np.array([0,50,100],[150,200,255])
with Image.open("1/汐见萤/shiomi2.webp") as image:
    gray=image.convert("L")
    pixels=np.array(gray)
print(pixels.shape)
print(pixels.ravel().shape)
fig,ax=plt.subplots()

#柱状图bar
# ax.bar(labels,counts)

#直方图hist
# ax.hist(values,bins=[0,50,100],edgecolor="black")
               #分组区域0-50 50-100 黑色边框

ax.hist(pixels.ravel(),bins=32,range=(0,256))
                       #分成32块 范围是从0-256，如果不写range那么会是从最小到最大
ax.set_title("Image brightness distribution")
ax.set_xlabel("Pixels brightness")
ax.set_ylabel("Pixels count")

plt.show()