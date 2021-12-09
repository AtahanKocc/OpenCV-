#Pikseller

import cv2
import numpy as np

img =cv2.imread("people.jpg") #örnek resmi projeye dahil ettik
dimension = img.shape #resmin boyutlarını ve kanal verisini verir.
print(dimension)

color = img[150,200] #pikselin renk değerine erişiyoruz. bgr değerlerini verir.
print("BGR: ", color)

blue = img[150,200,0]
print("Blue: ", blue)

green =img [150,200,1]
print("Green: ",green)

red =img [150,200,2]
print("red: ",red)

#deger degistirme
#img[150,200,0] = 100
#print("new blue: " , img[120,200,0])


blue1= img.item(150,200,0)
print(blue1)

img.itemset((150,200,0),161)  #blue1 degiskeni ile değişiklik yapmıyoruz.
print("new blue1: ",img[150,200,0])


cv2.imshow("Klon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#her bir piksel üç adet rengi tutar.

