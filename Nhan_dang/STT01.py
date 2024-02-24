import cv2
import numpy as np

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/input_06_2.png"
img = cv2.imread(image_path)

height, width = img.shape[:2]
new_height = int(height * 1)
new_width = int(width * 1)
img = cv2.resize(img, (new_width, new_height))

def put_text_center(img, text, contour):
    # Tìm bounding box của contour
    x, y, w, h = cv2.boundingRect(contour)
    # Tính toán vị trí để đặt text chính giữa
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)
    text_x = x + (w - text_size[0]) // 2
    text_y = y + (h + text_size[1]) // 2
    # Đặt text lên ảnh
    cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)

def detected_Shape(img):
	# code
	imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresholds = cv2.threshold(imgGrey, 0, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresholds, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
	    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
	    x = approx.ravel()[0]
	    y = approx.ravel()[1]
	    print(len(approx))
	    if len(approx) == 3:
	        cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	        put_text_center(img, "Triangle", cnt)
	    elif len(approx) == 4:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Quad", cnt)
	    elif len(approx) == 5:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Pentagon", cnt)
	    elif len(approx) == 6:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Hexagon", cnt)
	    elif len(approx) == 7:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Arrow", cnt)
	    elif len(approx) == 8:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Star four", cnt)
	    elif len(approx) == 10:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Star five", cnt)
	    elif len(approx) == 11:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Thunder", cnt)
	    elif len(approx) == 12:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Star six", cnt)
	    elif 12 < len(approx) < 14:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Heart", cnt)
	    else:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Circle", cnt)
detected_Shape(img)

cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
