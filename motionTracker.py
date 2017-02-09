import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
r, h, c, w = 260, 100, 410, 225  # simply hardcoded the values
track_window1 = (c, r, w, h)
r, h, c, w = 220, 80, 300, 200
track_window2  = (c, r, w, h)

# set up the ROI for tracking
roi = frame[r:r + h, c:c + w]
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleas1t 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while (1):
    rect, frame = cap.read()
    if rect:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location

        rect, track_window1 = cv2.meanShift(dst, track_window1, term_crit)
        rect, track_window2 = cv2.meanShift(dst, track_window2, term_crit)

        # Draw it on image
        x, y, w, h = track_window1
        x, y, w, h = track_window2
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        dst = np.zeros_like(frame)
        dst[y:y + h, x:x + w] = frame[y:y + h, x:x + w]
        cv2.imshow('dst', dst)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
    else:
        break
cv2.destroyAllWindows()
cap.release()

#############################################################################
