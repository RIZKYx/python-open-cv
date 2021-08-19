import cv2

citra = cv2.imread('peppers.png')
hasil = citra.copy()

#pengolahan citra

tebal = 20
hitam = [0, 0, 0]

jumbaris = hasil.shape[0]
jumkolom = hasil.shape[1]

#bingkai diatas

for baris in range(tebal):
    for kolom in range(jumkolom):
        hasil[baris,kolom] = hitam

# bingkai dibawah
for baris in range(jumbaris - tebal -1, jumbaris):
    for kolom in range(jumkolom):
        hasil[baris,kolom] = hitam

#bingkai dikiri

for baris in range(tebal,jumbaris - tebal -1):
    for kolom in range(tebal):
        hasil[baris,kolom] = hitam

# bingkai di bawah

for baris in range(tebal,jumbaris - tebal -1):
    for kolom in range(jumkolom - tebal-1, jumkolom):
        hasil[baris,kolom] = hitam

cv2.imshow('gambar asal', citra)
cv2.imshow('gambar hasil',hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()