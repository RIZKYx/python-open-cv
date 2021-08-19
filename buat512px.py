#pembuatan citra 512 px

import cv2
import numpy as np


#buat citra berwarna hitam
citra = np.zeros((512,512,3),np.uint8)

spaceman = cv2.imread('exp.png',-1)
jumbaris = spaceman.shape[0]
jumkolom = spaceman.shape[1]

citra[0:jumbaris,0:jumkolom,:] = spaceman[:,:,0:3]

goldhill = cv2.imread('goldhill.png')
hasil = cv2.add(goldhill,citra)
cv2.imshow('hasil',hasil)

cv2.waitKey(0)