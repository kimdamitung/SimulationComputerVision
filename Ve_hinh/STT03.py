import cv2
import sys
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 3: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 hình ngũ giác trên ảnh được mở từ camera
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

def pentagon_rotate(img, to_X, to_Y, rotate):
    """
    Args:
    img        : link imread
    to_X       : X coordinate of the center of the pentagon.
    to_Y       : Y coordinate of the center of the pentagon.
    rotate     : Rotation angle in degrees.
    """
    radius = [60, 40, 40, 60, 80]
    angle = 360 / 5
    vertices = []
    for i in range(5):
        x = int(to_X + radius[i] * np.cos(np.radians(i * angle + rotate)))
        y = int(to_Y + radius[i] * np.sin(np.radians(i * angle + rotate)))
        vertices.append((x, y))
    for i in range(5):
        cv2.line(img, vertices[i], vertices[(i + 1) % 5], (0, 0, 255), 2)


image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
# điều chỉnh tọa độ
X = 50
Y = 50

if img is not None:
	name = 'Nguyen Duy Tung'
	Write_Text_Img(img, 0, 600, name)
	# hình trước
	pentagon_rotate(img, X + 150, Y + 150, 105)
	pentagon_rotate(img, X + 285, Y + 150, 219)
	pentagon_rotate(img, X + 218, Y + 275, 342)
	# hình sau
	pentagon_rotate(img, X + 218, Y + 115, 162)
	pentagon_rotate(img, X + 285, Y + 240, 285)
	pentagon_rotate(img, X + 150, Y + 240, 39)
	cv2.imshow("STT 3", img)
	cv2.waitKey(0);
	cv2.destroyAllWindows()
	Check_size(img)
else:
	print("Lỗi. Không dẫn được ảnh")
