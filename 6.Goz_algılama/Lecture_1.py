"""
Resımden goz algılama
"""

import cv2

img=cv2.imread("C:\\OpenCv\\test_images\\face.png")

face_cascade = cv2.CascadeClassifier("C:\\OpenCv\\haarCascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:\\OpenCv\\haarCascade\\eye.xml")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray,1.3,7) #yuz kord aldık

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)


img2= img[y:y+h,x:x+w] #yuzumun oldugu degisken olacak.
gray2 = gray[y:y+h,x:x+w]

eyes = eye_cascade.detectMultiScale(gray2)

for(ex,ey,eh,ew) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

