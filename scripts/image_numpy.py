from PIL import Image
import numpy as np
image_path=input("请输入路径")
with Image.open(image_path) as image:
    image_info=np.array(image.convert("RGB"))
    print("打印 shape、ndim、dtype，取得图片高度和宽度。",image_info.shape,image_info.ndim,image_info.dtype,"高",image_info.shape[0],"宽",image_info.shape[1])
    print("a[0,0]",image_info[0,0])
    print("左上角10x10",image_info[0:9,0:9])
    print("输出第一页红色的宽高",image_info[:,:,0])
    print("平均值",image_info.mean(axis=(0,1)))#分别求三个页的每个行和列的平均值，得到[x x x]
    image_info1=image_info.astype(np.float32)/255.0
    print(image_info1.dtype,image_info1.shape,image_info1.max(),image_info1.min())