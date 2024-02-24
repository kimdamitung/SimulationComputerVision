import cv2
import numpy as np

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/input_06_2.png"
img = cv2.imread(image_path)

def identified_Circle(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = cv2.blur(gray, (3, 3))
	detected_circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=60, param2=25, minRadius=20, maxRadius=60)
	if detected_circles is not None:
		detected_circles = np.uint16(np.around(detected_circles))
		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]
			cv2.circle(img, (a, b), r, (0, 69, 255), 2)
			cv2.putText(img, "Circle", (a, b), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)

def identified_Quad(img):
	# code
	imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresholds = cv2.threshold(imgGrey, 0, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresholds, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
	    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
	    x = approx.ravel()[0]
	    y = approx.ravel()[1]
	    if len(approx) == 4:
	        cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	        cv2.putText(img, "Quad", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)

# identified_Circle(img)
identified_Quad(img)

cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
