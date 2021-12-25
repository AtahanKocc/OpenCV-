import cv2
img= cv2.imread("C:\\OpenCv\\test_images\\face.png") #resmi calismama dahil ediyorum.

face_cascade= cv2.CascadeClassifier('C:\\OpenCv\\haarCascade\\frontalface.xml')

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #haarlike özellik tespit

#resim üzerindeki yüzleri algılayalım. koordinatları degisken icinde sakla

faces=face_cascade.detectMultiScale(gray,1.3,7) #resim üzerindeki yüzlerin koord. bulup değisken icinde saklar.

#1.3 ölceklemdirme degeri kac oranında kücültürüz
# kac farklı pencerenin yüz bulmak istemesi 7 pencere

#sol üst kor; x,y - yükseklik ve genislik w,h

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #degiskenin icerisinde tuttuğu resim uzerinde isaretlemeler , sag alt koordiatınıda buluruz.

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



