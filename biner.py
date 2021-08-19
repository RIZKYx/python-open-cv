#convert to biner

import cv2
import sys
import numpy as np

if len(sys.argv) != 3:
    print('masukan berkas atau nilai ambang')
else:
    berkas = sys.argv[1]
    ambang = int(sys.argv[2])
    citra = cv2.imread(berkas, cv2.IMREAD_GRAYSCALE)
    if citra is None:
        print('tidak dapat membaca berkas',berkas)

    else:
        jumBaris = citra.shape[0]
        jumKolom = citra.shape[1]
        hasil = np.zeros((jumBaris,jumKolom,),np.uint8)

        for baris in range(jumBaris):
            for kol in range(jumKolom):
                if citra[baris,kol] >= ambang:
                    hasil[baris,kol]= 255 
                print(citra[baris,kol])


        cv2.imshow('asli',citra)
        cv2.imshow('hasil',hasil)
        cv2.waitKey(0)
