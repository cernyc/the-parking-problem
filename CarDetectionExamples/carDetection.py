import numpy as np
import cv2
import time


cars_cascade = cv2.CascadeClassifier('lbp_cars.xml')


img = cv2.imread('pictures/image3.jpg',0)
cars = cars_cascade.detectMultiScale(img, scaleFactor = 1.2,
                                   minNeighbors = 5, minSize=(150,150),flags = cv2.CASCADE_SCALE_IMAGE)
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,1,1),3)

    resized_image = cv2.resize(img, (960, 540))

    cv2.imshow('cars?', resized_image)


    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()