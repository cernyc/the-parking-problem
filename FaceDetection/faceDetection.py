import numpy as np
import cv2
import time
# https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
x = 290
y = 190
w = 300
h = 300

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


video = cv2.VideoCapture(0)


while(video.isOpened()):
    ret, frame = video.read()


    ROI = cv2.rectangle(frame, (x,y),(x+w,y+h),(200, 60, 60), 5)

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 1)
        for (x,y,w,h) in faces:
            if (x == 290 and y==190  and w==300 and h==300):
                cv2.rectangle(frame,(x, y),(x + w, y + h),(255,1,1),1)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(1,255,1),2)

        cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()