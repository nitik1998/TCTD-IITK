import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
	_, img = cap.read()

	## convert to hsv
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	## mask of green (36,25,25) ~ (86, 255,255)
	# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
	mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

	## slice the green
	imask = mask>0
	
	green = np.zeros_like(img, np.uint8)
	
	green[imask] = img[imask]
	
	cv2.imshow('green',green)

	
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
	 	

cap.release()
cv2.destroyAllWindows()