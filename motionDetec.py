import os
import cv2
import sys
import time

DELTA_COUNT_THRESHOLD = 1000
color = [0,255,0]
rectangle = False

def delta_images(t0, t1, t2):
    # Return the Absolute difference of t2 and t0
    d1 = cv2.absdiff(t0, t1)
    return d1

for cn in range(0,3):
    cam = cv2.VideoCapture(cn)
    if cam.isOpened():
        break

cam.set(3, 640)
cam.set(4, 480)

winName = "image diff"
cv2.namedWindow(winName)

# Fill the queue.
t_minus = cam.read()[1]
t_now = cam.read()[1]
t_plus = cam.read()[1]
t_now = cv2.resize(t_now, (640, 480))
t_minus = cv2.resize(t_minus, (640, 480))
t_plus = cv2.resize(t_plus, (640, 480))
delta_count_last = 1

try:
    os.mkdir("MOVEMENT_FRAMES")
except:
    pass

start_time = time.time()
record_video_state = False
while True:
    delta_view = delta_images(t_minus, t_now, t_plus)
    retval, delta_view = cv2.threshold(delta_view, 16, 255, 3)
    cv2.normalize(delta_view, delta_view, 0, 255, cv2.NORM_MINMAX)
    img_count_view = cv2.cvtColor(delta_view, cv2.COLOR_RGB2GRAY)
    delta_count = cv2.countNonZero(img_count_view)
    delta_view = cv2.flip(delta_view, 1)
    cv2.putText(delta_view, "DELTA: %d"%(delta_count), (5, 15), cv2.FONT_HERSHEY_PLAIN, 0.8, (255,255,255))
    cv2.imshow(winName, delta_view)
    if (delta_count_last < DELTA_COUNT_THRESHOLD and delta_count >= DELTA_COUNT_THRESHOLD):
        record_video_state = True
        rectangle = True
        sys.stdout.write("MOVEMENT %f\n" % time.time())
        sys.stdout.flush()
    now=time.time()
    if record_video_state == True:
        cv2.imwrite('MOVEMENT_FRAMES/movement-pong-%f.png' % (now-start_time),delta_view)
    delta_count_last = delta_count
    t_minus = t_now
    t_now = t_plus
    t_plus = cam.read()[1]
    t_plus = cv2.blur(t_plus,(8,8))
    t_plus = cv2.resize(t_plus, (640, 480))

    # Wait up to 10ms for a key press.
    # If the key is the ESC or 'q' then quit.
    key = cv2.waitKey(5)
    if key == 0x1b or key == ord('q'):
        cv2.destroyWindow(winName)
        break
