import numpy as np
import cv2
import time


cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')


img = cv2.imread('pictures/garagepic/pos/pos7.jpg')
spot = img[954:276, 1689:1000]
cv2.rectangle(img,(954,276),(1689,999),(255,1,1),3)
cars = cars_cascade.detectMultiScale(img)
for (x,y,w,h) in cars:
    if x >= 954 and x+w <= 1689:
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,1),2)

    resized_image = cv2.resize(img, (960, 680))

    cv2.imshow('cars?', resized_image)
    print w
    print h

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()