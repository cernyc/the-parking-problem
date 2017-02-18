import numpy as np
import cv2

# Show the video in cap
cap = cv2.VideoCapture(0)

# Load our cascade classifier from cars3.xml
car_cascade = cv2.CascadeClassifier(r'cars3.xml')

# Reduce frame number of tests.
number_of_frames_to_load = 30
for frame_id in xrange(number_of_frames_to_load):
    ret, image = cap.read()
    
    # Crop so that only the roads remain, eliminatives the distraction.
    image = image[120:,:-20]
    
    # Use Cascade Classifier to detect cars, may have to tune the
    # parameters for less false positives.
    cars = car_cascade.detectMultiScale(image, 1.008, 5)
    for (x,y,w,h) in cars:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    
    print 'Processing %d : cars detected : [%s]' % (frame_id, len(cars))

    cv2.imshow('frame', image)
    cv2.waitKey(300)

cap.release()
cv2.destroyAllWindows()
