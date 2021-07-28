import cv2

img = cv2.imread('lena.jfif', 0)

img = cv2.line(img, (0,0), (255,255), (147,96, 44), 10)
img = cv2.arrowedLine(img, (255,0), (0,255), (147,96, 44), 10)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()