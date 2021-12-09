import cv2

img= cv2.imread("people.jpg")

#bgr dan rgb çevir
#img1= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#cv2.imshow("people",img)
#cv2.imshow("people klong rgb",img1)

#bgr dan hsv

img_rgb= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow("people klon",img)
#cv2.imshow("people",img_rgb)
cv2.imshow("people klon",img_hsv)
#cv2.imshow("people klon",img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()

