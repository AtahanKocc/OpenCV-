import cv2

#webcam üzerinden görüntü alalım.

cap= cv2.VideoCapture(0) #videodayı nereden okuyacağız? 0=webcam, pc de yer alan video için adres gir.

#kareleri tek tek okuyorum.
while True:
    ret, frame= cap.read()  #videodaki kareleri okumak için  doğru okursa ret true, yanlış false
    frame = cv2.flip(frame,1) #aldığınız her görüntüyü istediğiniz eksenlere yansıtır

    cv2.imshow("Webcam",frame) #görüntüyü aldığım değişken frame değişkeni
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release() #videoyu serbest bırakıyoruz.
cv2.destroyAllWindows()