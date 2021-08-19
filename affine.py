#contoh tranformasi affine

import cv2
import numpy as np

citra = cv2.imread('taipei101.png')
jumbaris,jumkolom = citra.shape[:2]

titik1 = np.float32([[10,10],[10,50],[50,50]])
titik2 = np.float32([[10,0],[20,50],[50,60]])

matriks = cv2.getAffineTransform(titik1,titik2)
hasil = cv2.warpAffine(citra,matriks,(jumkolom,jumbaris))

cv2.imshow('hasil tranformasi',hasil)
cv2.waitKey()
