import os
from PIL import Image
from numpy import *


def get_imageList(path):
    """返回目录中所有 JPG 图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def im_resize(im, sz):
    """ 使用 PIL 对象重新定义图像数组的大小 """
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
    """ 对一幅灰度图像进行直方图均衡化 """

    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()  # 累积分布函数
    cdf = 255 * cdf / cdf[-1]  # 归一化

    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def compute_average(imlist):
    """ 计算图像列表的平均图像 """

    # 打开第一幅图像，将其存储再浮点型数组中
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            # 在操作两个 arrays 的时候，Numpu 会先比较两个元素的形状，所以这里只能处理两个形状相同的图片
            averageim += array(Image.open(imname))
        except:
            print(imname + '...skipped')
    averageim /= len(imlist)

    # 返回 uint8 类型的平均图像
    return array(averageim, 'uint8')
