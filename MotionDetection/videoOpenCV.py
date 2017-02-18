import numpy as np
import cv2


# This will return video from the first webcam on your computer.

cap = cv2.VideoCapture(0)
 
# This code initiates an infinite loop (to be broken later by a break statement),
# where we have ret and frame being defined as the cap.read().

while(cap.isOpened()): 
	ret, frame = cap.read()

	# Here, we define a new variable, gray, as the frame, converted to gray. 
	# Notice this says BGR2GRAY.

	if ret: # check ! (some webcam's need a "warmup")
		# our operation on frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Display the resulting frame
		cv2.imshow('frame', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()