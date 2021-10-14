import numpy
from PIL import Image
import numpy as np
import imtools

# 有关 numpy 存储图片的思考
# 我们知道 numpy 内部有类型 array，且 array 的数据类型默认情况下是 uint8
# 所以，我们可以判断，图片在 array 中是按照一个三维数组的形式进行存储的
# 由于 uint8 是 8 位，即每个维度的取值大小是必须在 0 ~ 255 之间的
# 我猜测这就是 RGB 色值，因为输出的 array 坐标值与取色器的结果是相同的

# im = np.array(Image.open('../data/001.jpg'))
# # im2 = 255 - im  # 对图像进行反相处理
# # im2 = 255.0 * (im/255.0)**2  # 对图像的像素求平方
# im2 = (100.0/255) * im + 100
# # 关于这里图像的转换为什么要使用 uint8，是对数组的数据格式进行一个强转
# img = Image.fromarray(np.uint8(im2))  # 将数组转为图像
# img.save('output/ChangePixelLower.jpg')

# 直方图均衡化实例
# im = np.array(Image.open('../data/001.jpg').convert('L'))
# im2, cdf = imtools.histeq(im)
# img = Image.fromarray(np.uint8(im2))
# img.save('output/ChangeGrayPixel.jpg')

# 图像平均
# imgList = imtools.get_imageList('../data')
# out = Image.fromarray(imtools.compute_average(imgList))
# out.save('output/averageImage.jpg')