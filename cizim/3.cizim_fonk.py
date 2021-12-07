import cv2
import numpy as np

#çizim yap. veri tipi unit8 kullan
canvas=np.zeros((512,512,3),dtype=np.uint8) +255
#print(canvas)

# Çizgi
#        tuval   1.çiz baş nok. 2.bitiş nok. 3.renk  4.kalınlık
cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)

cv2.line(canvas,(100,50),(200,250),(0,0,255),thickness=3)


#dikdörtgen çizmek

#sol üst köşe 20,20 sağ alt köşe 50,50
cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),thickness=8)
#içi dolu dikdörtgen için thickness=-1


#daire çizelim
#1. merkez 250 yarıçap 100
cv2.circle(canvas,(250,250),100,(0,0,255),thickness=5)
#içi dolu çember için =-1 yap


# Üçgen

p1= (100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas,p1,p2, (0,0,0), thickness=4)
cv2.line(canvas,p2,p3, (0,0,0), thickness=4)
cv2.line(canvas,p1,p3, (0,0,0), thickness=4)

points= np.array([[[110,200],[330,200],[290,220],[220,250]]], np.int32)
#rastgele çizgi oluşturup sonra dikdörtgen elde ederiz.
cv2.polylines(canvas,[points],True,(0,0,100),5)


cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
