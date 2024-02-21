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
    color = (0, 0, 255)
    box = cv2.boxPoints(rot) 
    box = np.int0(box)
    font_size = 2
    cv2.drawContours(img, [box], 0, color, font_size)


def decagon(img, goto_X, goto_Y, radius=120, n=10):
    original_degree = 360 / n
    angle = original_degree / 2
    points = []  
    list_points = []
    color = (211, 85, 486)
    thickness = 2
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree - 90)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - 90)))
        points.append((x, y))
        print(f"Tọa độ đỉnh {i+1}: ({x}, {y})")
        edge_length = 2 * radius * np.sin(np.pi / n)
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color, thickness=thickness)

def circleX10(img, goto_X, goto_Y, radius=90, n=10):
    original_degree = 360 / n
    points = []  
    color = (211, 85, 486)
    thickness = 2
    r = 25
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree - 90)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - 90)))
        cv2.circle(img, (x, y), 25, color, thickness)



        
image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    # decagon(img, X, Y)
    cubes_rotate(img, 287, 155, 74, 74, 18)
    cubes_rotate(img, 362, 212, 74, 74, 53)
    cubes_rotate(img, 391, 299, 74, 74, 90)
    cubes_rotate(img, 363, 388, 74, 74, 127)
    cubes_rotate(img, 288, 443, 74, 74, 162)
    cubes_rotate(img, 193, 443, 74, 74, 17)
    cubes_rotate(img, 119, 390, 74, 74, 53)
    cubes_rotate(img, 88, 299, 74, 74, 90)
    cubes_rotate(img, 118, 209, 74, 74, 127)
    cubes_rotate(img, 194, 155, 74, 74, 163)
    circleX10(img, X, Y)
    cv2.imshow("STT 17", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
