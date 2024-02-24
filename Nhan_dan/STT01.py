import cv2
import numpy as np

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/input_06.png"
img = cv2.imread(image_path)
height, width = img.shape[:2]
new_height = int(height * 0.9)
new_width = int(width * 0.9)
img = cv2.resize(img, (new_width, new_height))

def identified_Circle(img):
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
	median_img = cv2.medianBlur(gray, 5)
	circles = cv2.HoughCircles(median_img, cv2.HOUGH_GRADIENT, 1.011, 20, param1=100, param2=28, minRadius=0, maxRadius=55)
	circles = np.uint16(np.around(circles))
	for i in circles[0, :]:
		cv2.circle(img, (i[0], i[1]), i[2], (0, 69, 255), 5)
		cv2.putText(img, "circles", (i[0], i[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)


def identified_Triangle(img):
	# code
	imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresholds = cv2.threshold(imgGrey, 0, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresholds, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
	    approx = cv2.approxPolyDP(cnt, 0.025 * cv2.arcLength(cnt, True), True)
	    x = approx.ravel()[0]
	    y = approx.ravel()[1]
	    if len(approx) == 3:
	        cv2.drawContours(img, [approx], 0, (0, 69, 255), 5)
	        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)

identified_Circle(img)
identified_Triangle(img)
cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
