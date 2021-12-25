"""
Resimler veya videolar üzerindeki hedeflenen nesneleri algılamakta kullanılır.
Tespit edeceğimiz her nesnenin haar like özellikleri vardır.
haar cascadeler xml uzantılı dosyalardır.
https://github.com/opencv/opencv/tree/master/data/haarcascades
raw
ctrl+a
masaüstünde metin belgesi oluştur,kodları içine yapıştır.
.xml uzantısını unutma
.xml uzantılı dosya masaüstüne gelsin.
"""

"""
2. Temel Algoritma

A. İlgili kütüphaneyi, görüntüyü ve haar cascade dosyasını dahil et.

img=cv2.imread("...")
body_cascade=cv2.CascadeClassifier("...")

B. Görüntüyü boz tonlara çevirerek üzerinde ilgili nesneyi ara

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies=body_cascade.detectMultiScale(gray,1.1,5)

C. Resim üzerinde tespit ettik, bulunan nesneyi işaretle.

for(x,y,w,h) in bodies:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

"""

