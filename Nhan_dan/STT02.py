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
	circles = np.uint32(np.around(circles))
	for i in circles[0, :]:
		cv2.circle(img, (i[0], i[1]), i[2], (0, 69, 255), 2)
		cv2.putText(img, "circles", (i[0], i[1]), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 69, 255), 2)


def identified_quadrilateral(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	edges = cv2.Canny(blur, 0, 255)
	contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		epsilon = 0.0165555 * cv2.arcLength(cnt, False)
		approx = cv2.approxPolyDP(cnt, epsilon, True)
		x, y = approx[0][0]
		if len(approx) == 4:
			cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
			cv2.putText(img, "Quadrilateral", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 69, 255), 2)

identified_Circle(img)

cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
