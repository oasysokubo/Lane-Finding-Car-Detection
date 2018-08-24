import cv2
import numpy as np

# Create VideoCapture object from input video.
# Replace with 0 for webcam
cap = cv2.VideoCapture('testvideo2.mp4')

# Check if video opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream on file")

# Set default frame resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object
# Output is stored as 'out.avi' file
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))


# Read until video is completed
while(cap.isOpened()):

    # Capture every readable frame
    ret, frame = cap.read()
    # cv2.imshow("Original Scene Size", frame)

    if ret == True:

        # Write the frame into the file 'output.avi'
        # out.write(frame)

        # Display frame
        cv2.imshow('Scene', cv2.resize(frame, (700, 400)))

        # Press Q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything is done, release VideoCapture and VideoWriter objects
cap.release()
out.release()

# Close all the frames
cv2.destroyAllWindows()