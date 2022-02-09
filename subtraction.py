import cv2
image1=cv2.imread('star.jpg')
image2=cv2.imread('diamond.jpg')
newImage=cv2.subtract(image1,image2)
cv2.imwrite('subtracted.jpg',newImage)