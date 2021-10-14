from PIL import Image
import numpy as np
from scipy.ndimage import filters
from imageio import imwrite
import PyQt5
import skimage


# use gaussian with a gray picture
# im = np.array(Image.open('../data/001.jpg').convert('L'))
# im2 = filters.gaussian_filter(im, 10)
# Image.fromarray(im2).save('output/gaussian1.jpg')

# use gaussian with a colorful picture
im = np.array(Image.open('../data/001.jpg'))
print(im.shape)
im2 = np.zeros(im.shape)
for i in range(3):
    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], 10)
#  im2 = np.uint8(im2)
imwrite('output/imsave.jpg', im2)

#  时间有点赶，我大致写下我对一张 RGB 图像在数组中存储的理解
#  三维数组的本质是说一张图片存储为 R，G，B 三种通道的图，可以把它分为 3 个二维数组图，平面意思
#  所以，我们输出的图像数组，其实是许多个三维立体的纵切面数组，它们表示中间层的图像值。