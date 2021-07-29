import cv2


from tkinter import *
CAPTURE_INDEX = 0;

capture = cv2.VideoCapture(CAPTURE_INDEX)
eye_cascade = cv2.CascadeClassifier('projects\haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('projects\haarcascade_frontalface_default.xml')

while(capture.isOpened()):
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in eyes:
        cv2.rectangle(img, (x,y), (x+w, y+h),(255, 255, 255) , 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h),(255, 0, 0) , 3)

    cv2.imshow('Detecting Eyes& Face', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
