import numpy as np
import cv2
import time


cars_cascade = cv2.CascadeClassifier('cars.xml')


img = cv2.imread('pictures/image3.jpg',0)
cars = cars_cascade.detectMultiScale(img, scaleFactor = 1.1,
                                   minNeighbors = 10, minSize=(200,200),
                                   flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,1,1),1)

    cv2.imshow('cars?', img)


    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()