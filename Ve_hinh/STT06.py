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



"""
(456, 256)
(317, 446)
(94, 373)
(94, 138)
(317, 65)
(181, 256)
(232, 184)
(316, 211)
(316, 300)
(232, 327)
"""
# cv2.circle(img, (456, 256), 3,(255, 0, 0), 1) 
# cv2.circle(img, (316, 300), 3,(255, 0, 0), 1) 
# cv2.circle(img, (317, 446), 3,(255, 0, 0), 1) 
# cv2.circle(img, (232, 327), 3,(255, 0, 0), 1)
# cv2.circle(img, (94, 373), 3,(255, 0, 0), 1)
# cv2.circle(img, (181, 256), 3,(255, 0, 0), 1)
# cv2.circle(img, (94, 138), 3,(255, 0, 0), 1)
# cv2.circle(img, (232, 184), 3,(255, 0, 0), 1)
# cv2.circle(img, (316, 211), 3,(255, 0, 0), 1)
# cv2.circle(img, (317, 65), 3,(255, 0, 0), 1)
def Star_rotate(img, X, y, rotate, size):
    center = (X, y)
    points = np.array(
        [[456, 256],
         [317, 300],
         [317, 446],
         [231, 327],
         [92, 375],
         [181, 256],
         [94, 138],
         [232, 184],
         [317, 65],
         [317, 211]], np.int32
    )
    rotated_points = []
    for point in points:
        x = center[0] + int((point[0] - center[0]) * size)
        y = center[1] + int((point[1] - center[1]) * size)
        x_rotated = center[0] + int((x - center[0]) * np.cos(rotate) - (y - center[1]) * np.sin(rotate))
        y_rotated = center[1] + int((x - center[0]) * np.sin(rotate) + (y - center[1]) * np.cos(rotate))
        rotated_points.append([x_rotated, y_rotated])
    cv2.polylines(img, [np.array(rotated_points, np.int32)], isClosed=True, color=(0, 0, 255), thickness=2)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 0
Y = 0

if img is not None:
	name = 'Nguyen Duy Tung'
	Write_Text_Img(img, 0, 600, name)
	Star_rotate(img, X + 256, Y + 256, np.pi / 1, size=0.75)
	cv2.imshow("STT 6", img)
	cv2.waitKey(0);
	cv2.destroyAllWindows()
	Check_size(img)
else:
	print("Lỗi. Không dẫn được ảnh")
