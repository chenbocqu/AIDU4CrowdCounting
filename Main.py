import json
import tarfile

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

tar = tarfile.open("E:/baidu_ai/data/baidu_star_2018_train_stage1.tar")
tar.extractall("E:/baidu_ai/data/data194/")
tar.close()

img_fold = 'E:/baidu_ai/data/data194/baidu_star_2018/image/'
# 读取数据
with open('E:/baidu_ai/data/data194/baidu_star_2018/annotation/annotation_train_stage1.json', 'r') as f:
    ann_train = json.load(f)

ann = ann_train.get('annotations')
length = len(ann)
print(length)

# 读取图片
I = mpimg.imread('E:/baidu_ai/data/data194/baidu_star_2018/image/' + ann[1].get('name'))
print(I.shape)
plt.imshow(I)
locs = ann[0].get('annotation');

x = locs[1].get('x')
y = locs[1].get('y')
point = np.array([x, y])
print(point)
