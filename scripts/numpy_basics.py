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
#11.创建 (2, 3, 4) 数组，用 transpose(2, 0, 1) 调整轴顺序，检查形状，并核对一个元素换位置后值是否相同。
def answer_11():
    a=np.arange(1,25).reshape(2,3,4)
    b=a.transpose(2,0,1)#换之后的轴顺序是 列 表 行
    print(b)
    print(a[1, 1, 2] == b[2, 1, 1])
#12.自选两个形状相同的小数组，计算 a + 10、a * 2、a + b、a * b。
def answer_12():
    a=np.arange(1,13).reshape(3,4)
    b=np.arange(2,6)
    print(a)
    print(b)    
    print(a*b)#数值的计算，线性运算
    print(a*2)
#13.创建整数数组，用 astype(np.float32) 转换，打印前后的数据和 dtype。
def answer_13():
    a=np.arange(1,13).reshape(3,4)
    b=a.astype(np.float32)
    print(a,a.dtype,b,b.dtype)
#14.创建一个 2 行 3 列的 uint8 模拟像素数组，包含 0、255 和中间值；转为 float32 后除以 255.0，打印前后的数据、dtype 和 shape。
def answer_14():
    a=np.arange(1,7).reshape(2,3)
    a=a.astype(np.uint8)
    b=a.astype(np.float32)/255.0
    print(a,a.dtype,a.shape)
    print(b,b.dtype,b.shape)
#15.比较 [250] 的 uint8 数组直接加 10，与先转为 float32 再加 10 的结果。
def answer_15():
    a=np.array([250],dtype=np.float32)
    b=a.astype(np.uint8)#uint数据类型的数值上限是255，过了就会从0开始算
    print(a+10,b+10)
def answer_day26():
    a = np.arange(1, 13).reshape(3, 4)
    b = np.arange(1,5)
    c = np.arange(1,4).reshape(3,1)
    print((a+b)*c)
    print(a.sum(),a.mean(),a.min(),a.max())
    print(a.sum(axis=0),a.sum(axis=1))
    print(a.mean(axis=0),a.mean(axis=1),a.min(axis=1),a.max(axis=0))
    row_mean=a.mean(axis=1,keepdims=True)
    print(row_mean)
    d=a-row_mean
    print(d)
    # d=[]
    # for i in a:
    #     x=i.mean()
    #     d=np.append(d,x)
    # d=d.reshape(a.shape[0],1)
    # print(d)
answer_day26()