#pengebluran menggunakan bilateral filter

import cv2
import numpy as np

citra = cv2.imread('open cv/Image/simba.png')
blur1 = cv2.bilateralFilter(citra,10,75,75)
blur2 = cv2.bilateralFilter(citra,10,150,150)

hasil = np.hstack((citra,blur1,blur2))

cv2.imshow('hasil',hasil)
cv2.waitKey()
 