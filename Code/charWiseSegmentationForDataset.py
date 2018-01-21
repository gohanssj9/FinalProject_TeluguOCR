import cv2
import numpy as np
import glob
c = 0
# Load the image
for i in range(1,37):
	filen = "q/q"+str(i)+".png"
	#filen = "img.jpg"
	img = cv2.imread(filen)
	print img.shape
	#img = cv2.resize(img,(1074,300))
	# convert to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# smooth the image to avoid noises
	gray = cv2.medianBlur(gray,5)

	# Apply adaptive threshold
	thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
	thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

	# apply some dilation and erosion to join the gaps
	thresh = cv2.dilate(thresh,None,iterations = 5)
	#cv2.imshow('now_img',thresh)
	#cv2.waitKey(0)

	thresh = cv2.erode(thresh,None,iterations = 6)

	# Find the contours
	_,contours,hierarchy= cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
	threshold_area = 15

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
		    if x-5 >= 0 or y-10 >= 0:
		    	cv2.rectangle(img,(x-5,y-10),(x+w+5,y+h+10),(0,255,0),2)
		    	cv2.rectangle(thresh_color,(x-5,y-10),(x+w+5,y+h+10),(0,255,0),2)
		    else:
		    	cv2.rectangle(img,(x,y),(x+w+5,y+h+10),(0,255,0),2)
		    	cv2.rectangle(thresh_color,(x,y),(x+w+5,y+h+10),(0,255,0),2)

		    if y -10 <= 0 or x-5 <= 0:
		    	letter = img[y:y+h+10,x:x+w+5]
		    else:
		    	letter = img[y-10:y+h+10,x-5:x+w+5]

		    if c == 160:
		    	print c,x,y,x-5,y-10
		    font = cv2.FONT_HERSHEY_SIMPLEX
		    #cv2.putText(img,str(c+1),(x+(w/2),y), font, 0.4,(0,0,255),1,cv2.LINE_AA)
		    #cv2.imwrite("FinalProject_TeluguOCR/TeluguDataset/"+str(c+1)+"/"+str(c+1)+".JPEG",letter)
		    #cv2.imwrite("W22"+str(c+1)+".JPEG",letter)
		c+=1

	# Finally show the image
	cv2.imshow('img',img)
	cv2.waitKey(0)
	#cv2.imshow('res',thresh_color)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
