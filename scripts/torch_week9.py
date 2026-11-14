import torch
from PIL import Image
def day57():
    photo_list=list([("1/丰川祥子/saki.webp",0),("1/汐见萤/shiomi.webp",1),("1/汐见萤/shiomi2.webp",1)])
    class photos(torch.utils.data.Dataset):
        def __init__(self,sample):
            super().__init__()
            self.sample=sample
        def __len__(self):
            return len(self.sample)
        def __getitem__(self,num):
            path,label=self.sample[num]
            with Image.open(path) as image:
                image.convert("RGB")#不会转换image本身，应该是新建个变量来存的
                return image.convert("RGB"),label
    x=photos(photo_list)
    #因为__init__里面就要sample所以创建函数就需要写，而num是只有调用————getitem————时才需要的所以不必要这时候写
    # x.__len__() = len(x)
    print(len(x))
    # print(x.__getitem__(2)) = x[2]
    image,label=x[2]
    print(image.mode,label)
day57()
            