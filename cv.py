import cv2
import numpy as np
import sys

def plot(ver):
	cv2.imshow('image',ver)
	cv2.waitKey(0)

def cv(image):
	img = cv2.imread(image[1],0)
	#print(img.shape) 
	#print(img)
	img = cv2.medianBlur(img,1)
	#plot(img)
	kernel = np.ones((2,2),np.uint8)
	#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(4,4))
	#print(kernel)
	th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,17,2) #2値変換
	#plot(th)
	img =255-th
	#plot(img)
	#erosion = cv2.erode(img,kernel,iterations = 1)
	#erosion = cv2.dilate(img,kernel,iterations = 1)
	erosion = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #モルフォジー変換
	nonoise = cv2.fastNlMeansDenoising(erosion,None,10,7,21)
	#plot(erosion)
	cv2.imwrite("test.png",nonoise)
	
if __name__ =='__main__':
	image = sys.argv
	cv(image)
