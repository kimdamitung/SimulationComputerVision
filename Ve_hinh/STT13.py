import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 13: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường gấp khúc trên ảnh được mở từ camera
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


def pentagon(img, goto_X, goto_Y, radius = 100, n = 5):
    color = (255, 0, 0)
    thickness = 2
    angle = 360 / n
    points = []
    for i in range(n):
        x = int(goto_X + radius * np.sin(np.radians(i * angle - 90)))
        y = int(goto_Y + radius * np.cos(np.radians(i * angle - 90)))
        points.append((x, y))
    points = np.array(points, np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img, [points], isClosed=True, color=color, thickness= thickness)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    # pentagon_rotate(img, 150, 200, 72, 1.2)
    # pentagon_rotate(img, 203, 122, 140, 1.2)
    # pentagon_rotate(img, 278, 170, 72, 1.2)
    pentagon(img, 200, 250)
    cv2.imshow("STT 13", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
