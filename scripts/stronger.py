import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

image1=np.zeros((2,3))
image2=np.ones((2,3))
image_c=np.concatenate((image1,image2),axis=0)
image_s=np.stack((image1,image2),axis=0)
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