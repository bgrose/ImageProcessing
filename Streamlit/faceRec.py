import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

camera = cv2.VideoCapture(0)
BUTTON_CALCULATE = st.sidebar.button('Calculate')

WEIGHT = st.sidebar.number_input('Weight', value=0)
last_frame = None
last_frame_count = 0

i = 0
calcWait = True

while (run):
    _, img = camera.read()

        # Processing of frames are done in gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # We blur it to minimize reaction to small details
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Need to check if we have a last_frame, if not get it
    if last_frame is None:
        last_frame = gray
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.putText(img, "Objects Detected " + str(i), (10,50), font, 1, (0,0, 0), 2, cv2.LINE_AA) 
    FRAME_WINDOW.image(img)
    i =11234
    last_frame_count = i
    if (BUTTON_CALCULATE):
        COUNT = st.sidebar.metric('Count', value=last_frame_count)
        st.write('Stopped')
        img = cv2.putText(img, "Objects Detected " + str(i), (10,50), font, 1, (0,0, 0), 2, cv2.LINE_AA) 
        FRAME_WINDOW.image(img)
        st.sidebar.metric('Weight', i)
        run = False
        break
   