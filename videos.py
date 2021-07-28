import cv2
import datetime

cap = cv2.VideoCapture(0);

while(True):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255, 255), 2, cv2.LINE_AA) 
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

