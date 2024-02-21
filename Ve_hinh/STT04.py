import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 4: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 hình tròn trên ảnh được mở từ camera
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

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)

goto_X_Y = (235, 300)
radius = 75
color = (0, 0, 255)
font_size = 1
number_circle = 6

if img is not None:
	name = 'Nguyen Duy Tung'
	Write_Text_Img(img, 0, 600, name)
	for i in range(number_circle):
		recipe = 2 * math.pi * i / number_circle 
		x = int(goto_X_Y[0] + radius * math.cos(recipe))
		y = int(goto_X_Y[1] + radius * math.sin(recipe))
		gotoXY= (x, y)
		cv2.circle(img, gotoXY, radius, color, font_size)
	cv2.imshow("STT 4", img)
	cv2.waitKey(0);
	cv2.destroyAllWindows()
	Check_size(img)
else:
	print("Lỗi. Không dẫn được ảnh")
