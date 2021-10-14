import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
import numpy as np

# # first example
# # 读取图像到数组中
# im = array(Image.open('../data/001.jpg'))
#
# figure()
# # 绘制图像
# imshow(im)
#
# # 一些点
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]
#
# # paint point with red star mark
# plot(x, y, 'r*')
#
# # paint line with two points that made before
# plot(x[:2], y[:2])
#
# # add title to show picture that painted
# title('Plotting: "out.jpg"')
# savefig("outputStarLine.jpg")
# show()


# # second example
# # add image to array
# im = array(Image.open('../data/001.jpg').convert('L'))
#
# # new an image
# figure()
# # not use color information
# gray()
# # display the outline image in the upper left corner of the origin
# contour(im, origin='image')
# axis('equal')
# axis('off')
# plt.savefig('outputOutline.jpg')
# show()

# # third example
# im = array(Image.open('../data/001.jpg').convert('L'))
# 
# figure()
# hist(im.flatten(), 128)
# plt.savefig('outputHist.jpg')
# show()

# # fourth example
# goinput() 交互需要执行操作： Settings | Tools | Python Scientific | Show Plots in Toolwindow，去掉对勾
# im = array(Image.open('../data/001.jpg'))
#
# imshow(im)
# print('Please click 3 points')
# x = ginput(3)
# print('you clicked: ', x)
# show()