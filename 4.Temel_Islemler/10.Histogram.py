"""
Aydınlık nok. karanlık nok. konstrat degerleri ile ilgili cıkarım yaparız.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img= np.zeros((500,500),np.uint8)  # 500 e 500 siyah ekran
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
#        0 dan 60 a kadar - kaca kadar gittigi - renk - ici dolu dikdörtgen

cv2.imshow("img",img)

""" 
kaç deger/deger aralıgı
plt.hist(img.ravel(),256,[0,256]) #cizip
plt.show()  #görecegiz
"""

#img = cv2.imread("people.jpg")
#cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

