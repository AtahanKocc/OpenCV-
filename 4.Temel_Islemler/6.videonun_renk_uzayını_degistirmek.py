import cv2

cap= cv2.VideoCapture("patla.mp4")

while True:
    ret,frame= cap.read()  #cap.read hem frame i hemde true false döndürür. Framleri okuduk.
   # frame= cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY) griye dönüştürürüz.
    if ret== False:
       break
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF== ord("q"):
        break

cap.release()  #video capture sınıfını kapatır.
cv2.destroyAllWindows()


# Tek tek framleri çekip gri moda dönüştüreceğiz.
# tek tek hepsini okuyup dönüştüreceğiz.

"cap.read(), bir bool döndürür (Doğru/Yanlış). Çerçeve doğru okunursa, , Doğru olacaktır. Böylece bu Dönüş değerini kontrol ederek videonun sonunu kontrol edebilirsiniz."