import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 6: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường tam giác trên ảnh được mở từ camera
"""

def Write_Text_Img(img, X, Y, name):
	"""
	Args:
	img   : link ảnh 
	X     : tọa độ X
	Y     : tọa độ Y
	name  : kí tự tên 
	Returns: function
	"""
	text = 'Ho va ten: ' + name
	position = (X, Y)
	font = cv2.FONT_HERSHEY_SIMPLEX
	scale = 1
	color = (0, 0, 255)
	font_size = 2
	cv2.putText(img, text, position, font, scale, color, font_size)

def Check_size(img):
	"""
	Args:
	img   : link ảnh  
	Returns: 
	height   : chiều cao
	width    : chiều dài
	channels : số kênh màu
	"""
	height = img.shape[0]
	width = img.shape[1]
	channels = img.shape[2] if len(img.shape) > 2 else 1
	return height, width, channels


def Star_func(img, goto_X, goto_Y, radius = 210, rotate = 90, n = 5):
	original_degree = 360 / n
	color = (0, 255, 0)
	thickness = 2
	points = []
	hexagon = []
	for i in range(n):
		x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
		y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
		points.append((x, y))
	size_hexagon = 0.376 * radius
	for i in range(n):
		x = int(goto_X + size_hexagon * np.sin(np.radians(i * original_degree)))
		y = int(goto_Y + size_hexagon * np.cos(np.radians(i * original_degree)))
		hexagon.append((x, y))
	cv2.line(img, points[0], hexagon[0], (0, 0, 255), 2)
	cv2.line(img, points[1], hexagon[4], (0, 0, 255), 2)
	cv2.line(img, points[2], hexagon[3], (0, 0, 255), 2)
	# cv2.line(img, points[3], hexagon[2], (0, 0, 255), 2)
	cv2.line(img, points[4], hexagon[1], (0, 0, 255), 2)
	for i in range(n):
		cv2.line(img, points[i], points[(i + 2) % n], color, thickness)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
	name = 'Nguyen Duy Tung'
	Write_Text_Img(img, 0, 600, name)
	Star_func(img, X, Y)
	cv2.imshow("STT 21", img)
	cv2.waitKey(0);
	cv2.destroyAllWindows()
	Check_size(img)
else:
	print("Lỗi. Không dẫn được ảnh")
