import cv2
import easyocr

reader = easyocr.Reader(['en'])
output = reader.readtext('TextExtraction\\1199637-0516-pomogoofysigns-1w.jpg')
print(output)

iterator = len(output)
print(iterator)
for x in range(iterator):
    
    cord = output[x][0]

    x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
    x_max, y_max = [int(max(idx)) for idx in zip(*cord)]

    image = cv2.imread('TextExtraction\\1199637-0516-pomogoofysigns-1w.jpg')
    image = cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
