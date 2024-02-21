import cv2
import sys
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 2: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 hình tam giác trên ảnh được mở từ camera
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

def cubes_rotate(img, X, Y, width, height, rotate):
	"""
	Args:
	img   : link imread cv2 
	X     : go to X
	Y     : go to Y
	width : chiều dài
	height: chiều rộng
	rotate: gốc quay
	Returns: function
	"""
	rot = ((X, Y), (width, height), rotate)
	color = (255, 255, 255)
	box = cv2.boxPoints(rot) 
	box = np.int0(box)
	font_size = 2
	cv2.drawContours(img, [box], 0, color, font_size)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
# điều chỉnh tọa độ cho hình ảnh
X = 50
Y = 0

if img is not None:
	name = 'Nguyen Duy Tung'
	Write_Text_Img(img, 0, 600, name)
	# draw square 100x100
	cubes_rotate(img, X + 150, Y + 350, 100, 100, 0)
	cubes_rotate(img, X + 250, Y + 250, 100, 100, 0)
	# draw rectanle 100x115
	cubes_rotate(img, X + 125, Y + 285, 100, 115, 60)
	cubes_rotate(img, X + 275, Y + 315, 100, 115, 60)
	# draw square 115x115
	cubes_rotate(img, X + 175, Y + 220, 115, 115, 60 * 2)
	cubes_rotate(img, X + 220, Y + 380, 115, 115, 60 * 2)
	cv2.imshow("STT 2", img)
	cv2.waitKey(0);
	cv2.destroyAllWindows()
	Check_size(img)
else:
	print("Lỗi. Không dẫn được ảnh")
