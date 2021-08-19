import cv2
import numpy as np

citra = cv2.imread('taipei101.png')
hasil = cv2.flip(citra,1)
gab = np.hstack((citra,hasil))

cv2.imshow('hasil pencerminan',gab)
cv2.waitKey(0)