import numpy as np
import cv2
import time


cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')


img = cv2.imread('pictures/garagepic/pos/pos12.jpg')
cars = cars_cascade.detectMultiScale(img, scaleFactor = 1.03,
                                   minNeighbors = 0, minSize=(400,400), maxSize=(800,700))
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,1,1),3)


    resized_image = cv2.resize(img, (960, 540))

    cv2.imshow('cars?', resized_image)
    print w
    print h

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()