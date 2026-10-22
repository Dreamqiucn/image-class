import numpy as np
def answer_1():
    a=np.array([1,2,3,4])
    print(a)
    print(a.shape,a.ndim,a.size,a.dtype)
def answer_2():
    a=np.array([[1,2,3,4],[5,6,7,8],[5,6,7,8]],dtype=np.float32)
    print(a)
    print(a.shape,a.ndim,a.size,a.dtype)
        #行列多少，几维，多少个数，数据类型
answer_2()