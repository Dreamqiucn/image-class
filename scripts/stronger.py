import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
def day43():
    image1=np.zeros((2,3))
    image2=np.ones((2,3))
    image_c=np.concatenate((image1,image2),axis=0)#连一块
    image_s=np.stack((image1,image2),axis=0)#看不懂
    # print(image_c)
    # print(image_s)

    image3 = np.zeros((2, 3, 3))
    image4 = np.ones((2, 3, 3))

    together=np.stack((image3,image4),axis=0)
    print(together[1].shape)
    together2=together
    together3=together.copy()
    together3[1,1,1,1]=2

    print(together,together3)
def day44():
    a = np.array([-40, 0, 40])
    print(np.where(a>=0,100,a))#三个值，第一个是条件，第二个是成立那么...，第三个是不成立要怎么样
    print(np.clip(a,-1,47))#三个值，第一个是对象，第二个是最低值，第三个最高值
    scores = np.array([
    [0.7, 11],
    [0.1, 0.11]
    ]) 
    scores1 = np.array([
    [0.7, 11],
    [0.1, 0.11]
    ])
    
    print(scores.argmax(axis=1))
    print(scores*scores1)
    print(scores1@scores)
def day45():
    rng=np.random.default_rng()

    print(rng.integers(0,10,size=5))#起始值，不包括的终止值，多少个
    a=np.random.default_rng(3)#种子
    b=np.random.default_rng(3)
    print(a.integers(0,5,5),b.integers(0,5,5),np.equal(a.integers(0,5,5),b.integers(0,5,5)))
    c=a.integers(0,5,5)
    print(c,a.permutation(c))#打乱顺序
def day46():
    df1 = pd.DataFrame({
        "label": [" A ", "B"],
        "width": ["200", None]
    })
    df2 = pd.DataFrame({
        "label": ["A"],
        "width": ["100"]
    })
    together=pd.concat([df1,df2],ignore_index=True)#ignore_index重新显示index而不是用之前的
    together["label"]=together["label"].str.strip()#去掉字符 左右的空格 。
    together["width"]=pd.to_numeric(together["width"],errors="coerce")#数字字符串变成数值
    filled=together["width"].fillna(1111)#none的值变成1111
    
    print(filled)
    print(together.sort_values("width",ascending=False).reset_index())#排列，默认根据从小到大，也就是ascending默认是true，但是关掉就是从大到小了
def day47():
    a=pd.DataFrame({
        "name":["shiomi","sakiko","soyo","shiomi"],
        "cup":["A","B","C","A"],
        "height":[165,167,168,None]
    })
    stats=a.groupby("name").agg(
        rows=("height","size"),# 新建列 计算之前height列的size，也就是有几个
        counts=("height","count"),#非none的有几个
        mean_width=("height","mean")
    )
    a["status"]="ok"
    a.loc[a["height"].isna(),"status"]="missing"
    #a.loc[行的条件, 要修改的列] = 新值
    print(a)
def day48():
    widths=[100,200,300]
    heights=[10,50,299]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))    
    axes[0].scatter(widths,heights)#散点图
    axes[0].set_xlabel("width")
    axes[0].set_ylabel("height")
    axes[0].set_title("image sizes")
    axes[0].grid(True)
    axes[1].bar(["A", "B"], [2, 1])
    axes[1].set_title("Sample counts")
    fig.tight_layout()
    #自动调间距
    fig.savefig("day48_practice.png")

    plt.show()
day48()