#contoh cermin citra
import numpy as np
import cv2


citra = cv2.imread('taipei101.png')
jumbaris, jumkolom = citra.shape[:2]

matriks = np.float32([[-1,0,jumkolom],
                    [0,-1,jumbaris ]])
hasil = cv2.warpAffine(citra,matriks,(jumkolom,jumbaris))

gab = np.hstack((citra,hasil))
cv2.imshow('hasil penggabungan',gab)
cv2.waitKey(0)