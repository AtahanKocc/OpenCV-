#Pencereleri yeniden boyutlandırma

import cv2

cv2.namedWindow("Atahan",cv2.WINDOW_NORMAL)
img= cv2.imread("atahan.jpg")

img=cv2.resize(img,(661,461))  #görmek istediğim boyut

cv2.imshow("Atahan",img)
cv2.waitKey(0)
cv2.destroyAllWindows()