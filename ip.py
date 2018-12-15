import cv2
import numpy as np
import matplotlib.pyplot as plt
# img=cv2.imread('8.jpg',0)
cap=cv2.VideoCapture(0)
while(True):
	ret, img=cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# img1=cv2.imread('2.jpg')
	# plt.figure()
	# hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
	# plt.imshow(img)
	ret,img_b = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)
	# plt.show()
	kernel = np.ones((5,5),np.uint8)
	opening = cv2.morphologyEx(img_b, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
	# blur = cv2.blur(img_b,(5,5))
	erosion = cv2.erode(closing,kernel,iterations = 1)
	edges = cv2.Canny(erosion,100,200)
	# im2, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# cv2.drawContours(img, contours, -1, (0,255,0), 3)
	cv2.namedWindow('rgb_img', cv2.WINDOW_NORMAL)
	cv2.imshow('rgb_img',img)
	cv2.namedWindow('bw_img', cv2.WINDOW_NORMAL)
	cv2.imshow('bw_img',erosion)
	cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
	cv2.imshow('gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()