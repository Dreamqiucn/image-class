import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# 设置中文字体为微软雅黑
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

# 让坐标轴上的负号正常显示
plt.rcParams["axes.unicode_minus"] = False

def day36():
    labels=["a","b","c"]
    counts=[5,3,7]

    fig,ax=plt.subplots()
    #柱状图bar
    ax.bar(labels,counts)

    ax.set_title("Samples per class")
    ax.set_xlabel("Class")
    ax.set_ylabel("Count")

    plt.show()

def day37():
    values = [10, 20, 30, 70, 80, 90]
    fig,ax=plt.subplots()

    #直方图hist
    ax.hist(values,bins=[0,50,100],edgecolor="black")
                #分组区域0-50 50-100 黑色边框

    with Image.open("1/汐见萤/shiomi2.webp") as image:
        gray=image.convert("L") #灰度图只有亮度
        pixels=np.array(gray)

    ax.hist(pixels.ravel(),bins=32,range=(0,256))
                        #分成32块 范围是从0-256，如果不写range那么会是从最小到最大

    ax.set_title("Image brightness distribution")
    ax.set_xlabel("Pixels brightness")
    ax.set_ylabel("Pixels count")

    plt.show()

def day38():
    with Image.open("1/汐见萤/shiomi2.webp") as image:
        gray=image.convert("L")
        pixels=np.array(gray)
        rgb=image.convert("RGB")
    with Image.open("1/丰川祥子/saki.webp") as image:
        rgb2=image.convert("RGBA")
    # print(pixels.shape)
    # print(pixels.ravel().shape)
    fig,axes=plt.subplots(1,2)

    axes[0].imshow(rgb)
    axes[0].set_title("汐见萤")
    axes[1].imshow(rgb2)
    axes[1].set_title("丰川祥子")
    axes[0].axis("off")
    axes[1].axis("off")
    plt.show()
def day39():
    epochs = [1, 2, 3, 4]
    train_loss = [1.2, 0.9, 0.7, 0.5]
    val_loss = [1.3, 1.0, 0.9, 0.8]
    fig, ax = plt.subplots()
    ax.plot(epochs, train_loss, marker="o",label="train loss")
    ax.plot(epochs, val_loss, marker="o",label="validation loss")
    #折线图 
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.set_title("Simulated loss")
    ax.legend()
    #显示右上角的图例，什么点代表什么label
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    #左边下边到哪里
    fig.savefig("simulated_loss.png")
    #保存图片
    plt.show()
def day40():
    matrix=np.array([
        [3,1],
        [2,4]
    ])
    fig,ax=plt.subplots()
    image=ax.imshow(matrix,cmap="Blues")
    fig.colorbar(image, ax=ax)
    #颜色参考
    labels = ["A", "B"]
    ax.set_xticks([0, 1], labels=labels)
    ax.set_yticks([0, 1], labels=labels)
    #坐标0,1处是 A B
    ax.set_xlabel("Predicted label")
    ax.set_ylabel("True label")
    ax.set_title("Simulated confusion matrix")
    for row in range(2):
        for column in range(2):
            ax.text(
                column,row,matrix[row,column],ha="center",va="center"
            )
            if row==column:
                print("正确的是",(row,column),matrix[row,column])
    plt.show()
day40()