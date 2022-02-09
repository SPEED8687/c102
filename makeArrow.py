import cv2
from cv2 import line
image=cv2.imread('galaxy.jpg')
startPoint=(0,0)
endPoint=(250,250)
color=(0,255,0)
thickness=9
newImage=cv2.arrowedLine(image,startPoint,endPoint,color,thickness)
cv2.imwrite('arrow.png',newImage)