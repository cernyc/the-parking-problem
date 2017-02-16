# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
#http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

cars_cascade = cv2.CascadeClassifier('cars.xml')
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    cars = cars_cascade.detectMultiScale(format, scaleFactor = 1.1,
                                   minNeighbors = 10, minSize=(200,200),
                                   flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 1, 1), 1)


    cv2.imshow('Video', frame)


    # show the frame
    #cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break