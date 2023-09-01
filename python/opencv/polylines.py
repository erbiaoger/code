import numpy as np
import cv2 as cv

# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))


cv.waitKey(0)
cv.destroyAllWindows()