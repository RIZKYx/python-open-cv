#pembuatan garis tegak dan mendatar with arrow
#melalui titik tengah citra

import cv2
import sys

if len(sys.argv) == 1:
    print('masukan berkas / gambar')

else:
    berkas = sys.argv[1]
    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
    if citra is None:
        print('tidak dapat membaca citra', citra)
    else:
        jumbaris = citra.shape[0]
        jumkolom = citra.shape[1]
        xtengah = jumkolom // 2
        ytengah = jumbaris // 2

        #buat garis tegak

        cv2.arrowedLine(citra,(xtengah,0),(ytengah,jumbaris - 5),[128,128,128],5)

        #buat garis mendatar

        cv2.arrowedLine(citra, (0,ytengah),(jumkolom - 5,ytengah),[128,128,128],5)

        #tampilkan citra
        cv2.imshow('hasil',citra)

        cv2.waitKey(0)