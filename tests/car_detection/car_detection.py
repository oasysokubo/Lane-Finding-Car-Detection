# The objective of this program is to detect object of interest, in this case cars, in video
# frames and keep tracking the same object in each frame. The trained XML classifier 'cars.xml'
# contains many possible features of a car that can be detected in the frame. To exit out of the
# display window before the video ends, press 'ESC'.

import cv2
import numpy as np

# Create VideoCapture object to capture frames from video.
# Replace with integers to corresponding camera.
cap = cv2.VideoCapture('test_pics/raw/test1.jpg')

# Load trained XML classifier to detect cars
car_cascade = cv2.CascadeClassifier('resources/cars.xml')

# Check if video opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream")

# Loop runs until video is over or key is pressed
while(cap.isOpened()):
    # Capture every readable frame
    ret, frame = cap.read()

    if ret == True:

        # Convert each frame to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect cars of different size in the frame
        detect_car = car_cascade.detectMultiScale(gray, 1.1, 1)

        # Draw rectangle on each detected car in frame
        for(x, y, w, h) in detect_car:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Display frame in window
        cv2.imshow('Car Detection', cv2.resize(frame, (700, 400)))

        # Break out of while loop if 'ESC' is pressed
        if cv2.waitKey(1) == 27:
            break

    # Break the loop
    else:
        break

# Releases VideoCapture object memory when program is finished
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()