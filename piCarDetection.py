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
	display_window = cv2.namedWindow("piCarDetection")
	

	cars_cascade = cv2.CascadeClassifier('cars.xml')
	
	
	time.sleep(1)
	

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	

	    image = frame.array
	
	    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	    cars = cars_cascade.detectMultiScale(gray, 1.1, 5)
	    for (x,y,w,h) in cars:
	        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 1, 1), 1)


	    #DISPLAY TO WINDOW
	    cv2.imshow("piCarDetection", image)
	    key = cv2.waitKey(1)
	

	    # clear the stream in preparation for the next frame
	    rawCapture.truncate(0)
	

	    # if the `q` key was pressed, break from the loop
	    if key == ord("q"):
	        break

