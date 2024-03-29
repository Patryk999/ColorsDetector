#
#to run type  >python colorsdetector.py --image lines.jpg
#
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print(image)

#white boundries
boundaries = [
	([180, 180, 180], [255, 255, 255]),
]

#test boundries
for x in range(0,180,10):
    boundaries.append(([x,x,x],[255,255,255]))

for (lower, upper) in boundaries:
    lower = np.array(lower)
    upper = np.array(upper)
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("images", np.hstack([image, output]))
    print (np.hstack([image,output]))
    cv2.waitKey(0)