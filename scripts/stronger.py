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
day44()