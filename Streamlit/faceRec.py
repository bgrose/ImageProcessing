import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

camera = cv2.VideoCapture(0)
BUTTON_CALCULATE = st.sidebar.button('Calculate')
WEIGHT = st.sidebar.number_input('Weight', value=0)

i = 0
calcWait = True

while (run):
    _, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.putText(img, "Objects Detected " + str(i), (10,50), font, 1, (0,0, 0), 2, cv2.LINE_AA) 
    FRAME_WINDOW.image(img)
    i += 1
    if (BUTTON_CALCULATE):
        calcWait = False
    

else:
    st.write('Stopped')
    _, img = camera.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.putText(img, "Objects Detected " + str(i), (10,50), font, 1, (0,0, 0), 2, cv2.LINE_AA) 
    FRAME_WINDOW.image(img)
    st.sidebar.metric('Weight', i)