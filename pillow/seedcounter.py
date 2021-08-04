from PIL import Image, ImageFilter
import cv2

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
im = Image.open("black-organic-sesame-seeds-isolated-260nw-664802284.jpg")
im.show()


#Import all the enhancement filter from pillow
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
#Create image object
#Applying the blur filter
img1 = im.filter(CONTOUR)
img1.save('ImageFilter_blur.jpg')
img1.show()

image =cv2.imread("R.jfif")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200)
contrours, heirachy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
number = len(contrours)

image = cv2.putText(image, str(number), (10,50), font, 1, (0,255, 255), 2, cv2.LINE_AA) 

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
