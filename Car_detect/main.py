import cv2

cascade_src = 'Car_detect/cars.xml'
video_src = 'Car_detect/video1.avi'
#video_src = 'Car_detect/video2.avi'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while(True):
    ret, img = cap.read()
    if (type(img) == type(None)):
        break

    img = cv2.resize(img, (640, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.2, 1)

    numOfCars= str(len(cars)) + " cars found"
    img = cv2.putText(img, numOfCars, (10,50), font, 1, (0,255, 255), 2, cv2.LINE_AA) 

    for(x, y, w, h) in cars:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,225), 2)

    
    out.write(img)
    cv2.imshow('Detecting Cars', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(33) == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()