# Capture video from camera or load a video, OpenCV provides a very simple interface for this.
# To capture a video, a VideoCapture object must be created. Its argument can be either the device index
# or the name of a video file. A device index is a number to specify which camera to use. The main camera
# would be a webcam and can be passed as a 0 (or -1). You can select a second camera by passing 1 and so on.
# From there, the camera captures frame-by-frame and displays it on the screen.

import cv2
import numpy as np

# Create VideoCapture object from input video.
# Replace with 0 for webcam
cap = cv2.VideoCapture('test_video/testvideo2.mp4')

# Check if video opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream on file")

# Read until video is completed
while(cap.isOpened()):

    # Capture every readable frame
    ret, frame = cap.read()
    # cv2.imshow("Original Scene Size", frame)

    if ret == True:

        # Display frame
        cv2.imshow('Scene', cv2.resize(frame, (700, 400)))

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything is done, release VideoCapture and VideoWriter objects
cap.release()

# Close all the frames
cv2.destroyAllWindows()