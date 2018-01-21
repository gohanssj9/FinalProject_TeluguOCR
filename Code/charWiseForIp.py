import cv2
import numpy as np
import glob
c = 0
# Load the image
for i in range(1,2):
	#filen = "q/q"+str(i)+".png"
	filen = "img.jpg"
	img = cv2.imread(filen)
	#print img.shape
	img = cv2.resize(img,(1280,768))
	# convert to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# smooth the image to avoid noises
	gray = cv2.medianBlur(gray,5)

	# Apply adaptive threshold
	#thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
	thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

	# apply some dilation and erosion to join the gaps
	thresh = cv2.dilate(thresh,None,iterations = 1)
	#cv2.imshow('now_img',thresh)
	#cv2.waitKey(0)

	thresh = cv2.erode(thresh,None,iterations = 2)

	# Find the contours
	_,contours,hierarchy= cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
	threshold_area = 150

	'''
	Remember these values:
		dilate:5, erode:2 for word segmentation -- threshold_area:1000
		dilate:1, erode:2 for character segmentation -- threshold_area:15
		While dataset creation: dilate : 5, erode : 6 , threshold_area:15
	'''

	#cv2.drawContours(img,contours,-1,(0,255,0),-1)
	# For each contour, find the bounding rectangle and draw it
	
	for cnt in contours:
		area = cv2.contourArea(cnt)
		#print area,i+1
		if area > threshold_area:
		    x,y,w,h = cv2.boundingRect(cnt)
		    #cv2.drawContours(img [cnt], -1, (255, 255, 255), -1)
		    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
		    cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(255,255,255),2)

		    letter = img[y:y+h,x:x+w]
		    font = cv2.FONT_HERSHEY_SIMPLEX
		    #cv2.putText(img,str(i+1),(x+(w/2),y), font, 0.4,(0,0,255),1,cv2.LINE_AA)
		    cv2.imwrite(str(c+1)+".jpg",letter)
		c+=1

	# Finally show the image
	cv2.imshow('img',img)
	cv2.waitKey(0)
	#cv2.imshow('res',thresh_color)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
