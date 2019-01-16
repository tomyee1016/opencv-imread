import cv2 as cv
import numpy as np
img = cv.imread("E:/demo/images/cat.jpg")
cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)
#cv.imwrite('E:/demo/images/cat1.png',img)
k = cv.waitKey(0)
if k==27: #wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('a'):#wait for 's' key to save and exit
    cv.imwrite('E:/demo/images/cat1.png',img)
    cv.destroyAllWindows()