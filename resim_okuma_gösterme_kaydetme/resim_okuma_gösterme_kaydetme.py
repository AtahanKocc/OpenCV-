import cv2

""" 
#resimlerin matematiksel değerlerini okur.img değişkenine eşitler
img = cv2.imread("atahan.jpg",cv2.IMREAD_GRAYSCALE) # GrayScale gri tonlarda okur.
print(img) #matris verir.
#resimler bir sayıdır.
"""
img = cv2.imread("atahan.jpg",cv2.IMREAD_GRAYSCALE)
# Resimleri Gösterme  (resmin göster. pencere adı, )
cv2.namedWindow("image",cv2.WINDOW_NORMAL)  #pencere boyutlandırıyoruz.
cv2.imshow("image", img)
cv2.imwrite("atahan1.jpg",img)  #dosya kaydedeceğiz. klonladık.
cv2.waitKey(0) #mili saniye cinsindendir. 0 dersen sen kapatana kadar.
cv2.destroyAllWindows() # q tuşuna bastığında tüm pencereler kapansın.


# cv2.namedWindow ile cv2.imshow un pencere adı aynı isim olacak.
