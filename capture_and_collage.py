import cv2
from datetime import datetime
import sys
import numpy as np

# create the VideoCapture inst
cam = cv2.VideoCapture(0)
input('Press Enter to capture')
ret, img = cam.read()
capture_image1_name = "test1_" + str(datetime.now()) + ".png"
cv2.imwrite(capture_image1_name, img)
cam.release()

# Let me click one more pic
cam = cv2.VideoCapture(0)
input('Press Enter to capture another one')
ret, img = cam.read()
capture_image2_name = "test2_" + str(datetime.now()) + ".png"
cv2.imwrite(capture_image2_name, img)
cam.release()

# Now we have captured the image let's create the collage out of it
# with color 
img_read1_0 = cv2.imread(capture_image1_name, cv2.IMREAD_COLOR)
img_read2_0 = cv2.imread(capture_image2_name, cv2.IMREAD_COLOR)

# resize
img_read1 = cv2.resize(img_read1_0, (250, 250))
img_read2 = cv2.resize(img_read2_0, (250, 250))

# Vertically stack up two images of first capture
col1 = np.vstack([img_read1, img_read1])

# Vertically stack up two images of secodn capture
col2 = np.vstack([img_read2, img_read2])

# Now horizontally put them side-by-side
collage = np.hstack([col1, col2])

# Create the collage
k = cv2.waitKey(0)
cv2.imwrite("collage.png", collage)
