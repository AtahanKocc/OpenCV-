# En boy oranı

import cv2

#img=resmin tutulduğu değişken
def resizewithAspectRatio(img,width=None, height=None, inter=cv2.INTER_AREA):

    dimension = None
    (h,w)= img.shape[:2]

    if width is None and height is None:
        return img

    if width is None:
        # orjinal boy bölü kullanıcının verdiği boy değeri
        r= height / float(h)
        dimension= (int(w*r),height)
    else:
       r=width/float(w)
       dimension = (width,int(h*r))

    return cv2.resize(img,dimension,interpolation=inter)

img= cv2.imread("atahan.jpg")
img1= resizewithAspectRatio(img,width=None, height=661, inter=cv2.INTER_AREA) #yeniden boyutlandırma
cv2.imshow("Original",img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()