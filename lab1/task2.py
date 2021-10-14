import numpy as np
import cv2

img = np.zeros((720, 600, 3), np.uint8)

# 最上面的红圈
img = cv2.ellipse(img, (256, 100), (30, 30), 120, 0, 300, (0, 0, 255), -1, cv2.LINE_AA)
# img = cv2.ellipse(img, (256, 100), (10, 10), 120, 0, 300, (255, 204, 0), -1, cv2.LINE_AA)
img = cv2.circle(img, (256, 100), 10, (255, 204, 0), -1, cv2.LINE_AA)

# 画左下的绿色
img = cv2.ellipse(img, (226, 160), (30, 30), 0, 0, 300, (0, 255, 0), -1, cv2.LINE_AA)
img = cv2.circle(img, (226, 160), 10, (255, 204, 0), -1, cv2.LINE_AA)

# 画右下的蓝色
img = cv2.ellipse(img, (290, 160), (30, 30), -60, 0, 300, (255, 0, 0), -1, cv2.LINE_AA)
img = cv2.circle(img, (290, 160), 10, (255, 204, 0), -1, cv2.LINE_AA)

# 3.画文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (160, 240), font, 2, (255, 255, 255), 8, cv2.LINE_AA)

# 显示并回收资源
cv2.imshow('draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()