"""
kenarları saptayacağız.

input
minThreshold
maxThreshold
"""

import cv2

cap=cv2.VideoCapture(0)  #webcam görüntü çek

while 1:  #frameleri oku
    ret,frame = cap.read() #frame çek
    frame =cv2.flip(frame,1)
    edges = cv2.Canny(frame,100,200)  #framlerin köselerinin buldugumuz halini depoladık

    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





