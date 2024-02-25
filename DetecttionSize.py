import cv2
import numpy as np

def getContours(img, cThr=[100, 100], showCanny=False, minArea=1000, filter=0, draw=False):
	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
	imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])
	kernel = np.ones((5, 5))
	imgDial = cv2.dilate(imgCanny, kernel, iterations=3)
	imgThre = cv2.erode(imgDial, kernel, iterations=2)
	if showCanny:
		cv2.imshow("Canny", imgThre)
	contours, hierchy = cv2.findContours(imgThre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	finalContour = []
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area > minArea:
			peri = cv2.arcLength(cnt, True)
			approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
			bbox = cv2.boundingRect(approx)
			if filter > 0:
				if len(approx) == filter:
					finalContour.append([len(approx), area, approx, bbox, cnt])
			else:
				finalContour.append([len(approx), area, bbox, cnt])
	finalContour = sorted(finalContour, key= lambda x:x[1], reverse=True)
	if draw:
		for cnt in finalContour:
			cv2.drawContours(img, cnt[4], -1, (0, 0, 255), 3)
	return img, finalContour


webcam = False
path = 'img/checksize.jpg'
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)
while True:
	if webcam:
		success, img = cap.read()
	else:
		img = cv2.imread(path)
	img, conts = getContours(img, minArea=50000, filter=4)
	if len(conts) != 0:
		biggest = conts[0][2]
		print(biggest)
	cv2.imshow("Check Size", img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()