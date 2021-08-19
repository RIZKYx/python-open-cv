import cv2
import numpy as np

#buat citra berwarna hitam
citra = np.zeros((512,512,3),np.uint8)
alpha = np.zeros((512,512),np.uint8)

spaceman = cv2.imread('exp.png',-1)
jumbaris = spaceman.shape[0]
jumkolom = spaceman.shape[1]

citra[0:jumbaris,0:jumkolom,:] = spaceman[:,:,0:3]
alpha[0:jumbaris,0:jumkolom] = spaceman[:,:,3]
cadar = cv2.merge((alpha,alpha,alpha))
kebalikan = cv2.bitwise_not(cadar)

cv2.imshow('cadar',cadar)
cv2.imshow('kebalikan',kebalikan)

goldhill = cv2.imread('goldhill.png')

hasil_and= cv2.bitwise_and(goldhill,kebalikan)
cv2.imshow('hasil',hasil_and)
print(hasil_and.shape)

hasil_add = cv2.add(hasil_and,citra)
cv2.imshow('hasil add',hasil_add)

cv2.waitKey(0)