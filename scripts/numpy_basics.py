import numpy as np
#1.创建一个包含 4 个数字的一维数组。
def answer_1():
    a=np.array([1,2,3,4])
    print(a)
    print(a.shape,a.ndim,a.size,a.dtype)
#2.创建一个 2 行 3 列的二维数组。
def answer_2():
    a=np.array([[1,2,3,4],[5,6,7,8],[5,6,7,8]],dtype=np.float32)
    print(a)
    print(a.shape,a.ndim,a.size,a.dtype)
        #行列多少，几维，多少个数，数据类型
#3.取出第三行第二列的数字。
def answer_3():
    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # print(a)
    print(a[2,1])
#4.取出最后一行、第三列。
def answer_4():
    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # print(a)
    print(a[2,:])#第三列一整行
    print(a[:,2])#一整列和第三行
#5. 取出右下角两行两列的区域，打印它的 shape。
def answer_5():
    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(a)
    print(a[-2:,-2:])
    print(a[-2:,-2:].shape)
#6.筛选大于 6 的数字，再筛选大于等于 4 且小于等于 9 的数字。
def answer_6():
    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(a)
    print(a[a>6])#数组
    print(a[(a>=4)&(a<=9)])
#7.对比 a[0] 和 a[0:1] 的内容及 shape。
def answer_7():
    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(a[0])#第一行一维
    print(a[0:1])#切片，0-1行 切出来的是二维
    print(a[0].shape)
    print(a[0:1].shape)
#8.创建包含 1～12 的一维数组，分别变成 (3, 4) 和 (2, 6)。
def answer_8():
    a=np.arange(1,13)#从1-12
    b=a.reshape(3,4)
    c=a.reshape(2,6)
    print(b,c)
#9.尝试 reshape(4, -1)，再把其中一个二维数组变回一维。
def answer_9():
    a=np.arange(1,13)
    b=a.reshape(-1)#直接-1是1维，1,-1是二维
    c=a.reshape(4,-1)
    print(b,c)
#10.比较 (3, 4) 数组的 .T 与 .reshape(4, 3)，观察元素位置。
def answer_10():
    a=np.arange(1,13)
    b=a.reshape(4,3)
    c=a.reshape(3,4).T
    print(a,b,c)
#创建 (2, 3, 4) 数组，用 transpose(2, 0, 1) 调整轴顺序，检查形状，并核对一个元素换位置后值是否相同。
def answer_11():
    a=np.arange(1,25).reshape(2,3,4)
    b=a.transpose(2,0,1)#换之后的轴顺序是 列 表 行
    print(b)
    print(a[1, 1, 2] == b[2, 1, 1])

answer_4()