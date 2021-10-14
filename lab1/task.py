import cv2

img = cv2.imread('fruits.png')
ims = img.shape
print(ims)
cv2.imshow('201941412108 Lei Zekun', img)
key = cv2.waitKey()
if key == ord('s'):
    cv2.imwrite('fruits.jpg', img)
    cv2.destroyAllWindows()