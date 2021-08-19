#contoh translasi citra
import numpy as np
import cv2
import math

citra = cv2.imread('taipei101.png')
jumbaris, jumkolom = citra.shape[:2]

matriks = np.float32([[1,0.25,0],[0,1,0]])
hasil = cv2.warpAffine(citra,matriks,(int(1.4  * jumkolom),jumbaris))

gab = np.hstack((citra,hasil))
cv2.imshow('hasil penggabungan',gab)
cv2.waitKey(0)