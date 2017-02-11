import numpy as np
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera


### https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)


#video = cv2.VideoCapture(0)
video = rawCapture

while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 1)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,1,1),1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(1,255,1),2)

        cv2.imshow('Video', frame)
        key = cv2.waitKey(1) & 0xFF


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break


video.release()
cv2.destroyAllWindows()