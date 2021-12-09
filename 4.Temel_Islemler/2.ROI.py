# Region of interest --> ilgi alanı

import cv2

img =cv2.imread("people.jpg")
# print(img.shape[:2])

roi = img[60:200, 300:400] #1.dikey pikselleri tarıyoruz 2.yatay pikselleri tarıyoruz.

cv2.imshow("roi",roi)
cv2.imshow("people",img)
cv2.waitKey(0)
cv2.destroyAllWindows()