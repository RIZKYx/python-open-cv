import cv2

citra = cv2.imread('appleneg.jpeg',cv2.IMREAD_GRAYSCALE)
index = cv2.bitwise_not(citra)

cv2.imshow('hasil',index)
cv2.waitKey(0)

status = cv2.imwrite('D:/opencv/lemonnegative.png',index)
 
print("Image written to file-system : ",status)