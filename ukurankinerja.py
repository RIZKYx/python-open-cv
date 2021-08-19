#pengukuran kinerja dua proses untuk
# melakukan inversi citra

import cv2
import numpy as np

citra = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)

#proses 1
awal = cv2.getTickCount()

jumbaris = citra.shape[0]
jumkolom = citra.shape[1]
hasil = np.zeros((jumbaris,jumkolom),np.uint8)
        
for brs in range(jumbaris):
     for kol in range(jumkolom):
        hasil[brs,kol] = 255 - citra[brs,kol]



akhir = cv2.getTickCount()
selangwaktu = (akhir - awal)/ cv2.getTickFrequency()
print('proses waktu 1: ',selangwaktu,' detik.')

print(cv2.getTickFrequency())

#proses 2

awal = cv2.getTickCount()
hasil = 255 - citra

akhir = cv2.getTickCount

akhir = cv2.getTickCount()
selangwaktu = (akhir - awal)/ cv2.getTickFrequency()
print('proses waktu 2: ',selangwaktu,' detik.')
