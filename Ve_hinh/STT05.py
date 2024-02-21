import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 5: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường tròn trên ảnh được mở từ camera
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

def Star_rotate(img, goto_X, goto_Y, rotate):
	radius = 150
	number_wing = 5
	color = (0, 255, 0)
	recipe = 2 * np.pi / number_wing
	if rotate > 0 and rotate <= 360:
		rotate = 180 / rotate
	elif rotate == 0:
		rotate = 1
	else:
		raise ValueError("Hãy nhập gốc quay rotate từ 0 đến 360!!!")
	star_array = []
	for i in range(number_wing):
		vertex_star = i * recipe + np.pi / 4
		x = goto_X + int(radius * np.cos(vertex_star))
		y = goto_Y + int(radius * np.sin(vertex_star))
		star_array.append((x, y))
	for i in range(number_wing):
		cv2.line(img, star_array[i], star_array[(i + 2) % number_wing], color, 2)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
# điều chỉnh tọa độ
X = 0
Y = 0

if img is not None:
	name = 'Nguyen Duy Tung'
	Write_Text_Img(img, 0, 600, name)
	Star_rotate(img, X + 225, Y + 335, 360)
	cv2.imshow("STT 5", img)
	cv2.waitKey(0);
	cv2.destroyAllWindows()
	Check_size(img)
else:
	print("Lỗi. Không dẫn được ảnh")
