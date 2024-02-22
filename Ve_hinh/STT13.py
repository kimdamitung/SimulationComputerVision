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


def pentagonNotWeight_0(img, goto_X, goto_Y, radius = 80, rotate=0, n = 5):
    color_blue = (255, 0, 0)
    thickness = 2
    original_degree = 360 / n
    points = []
    for i in range(n):
        if i in [0, 1, 4]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
            points.append((x, y))
        if i in [2]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 10)
            points.append((x, y))
        if i in [3]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) + 10)
            points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color_blue, thickness= thickness)


def pentagonNotWeight_1(img, goto_X, goto_Y, radius = 80, rotate=0, n = 5):
    color_blue = (255, 0, 0)
    thickness = 2
    original_degree = 360 / n
    points = []
    for i in range(n):
        if i in [0, 1]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
            points.append((x, y))
        if i in [2]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 10)
            points.append((x, y))
        if i in [4]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 15)
            points.append((x, y))
        if i in [3]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 13)
            points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color_blue, thickness= thickness)


def pentagonNotWeight_2(img, goto_X, goto_Y, radius = 80, rotate=0, n = 5):
    color_blue = (255, 0, 0)
    thickness = 2
    original_degree = 360 / n
    points = []
    for i in range(n):
        if i in [1]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) + 10)
            points.append((x, y))
        if i in [0, 4]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
            points.append((x, y))
        if i in [2]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) + 7)
            points.append((x, y))
        if i in [3]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) + 10)
            points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color_blue, thickness= thickness)


def pentagonNotWeight_3(img, goto_X, goto_Y, radius = 80, rotate=0, n = 5):
    color_blue = (255, 0, 0)
    thickness = 2
    original_degree = 360 / n
    points = []
    for i in range(n):
        if i in [0, 1, 2]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
            points.append((x, y))
        if i in [3]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 15)
            points.append((x, y))
        if i in [4]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)) - 5)
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 12)
            points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color_blue, thickness= thickness)


def pentagonNotWeight_4(img, goto_X, goto_Y, radius = 80, rotate=0, n = 5):
    color_blue = (255, 0, 0)
    thickness = 2
    original_degree = 360 / n
    points = []
    for i in range(n):
        if i in [0]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 15)
            points.append((x, y))
        if i in [1, 2]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
            points.append((x, y))
        if i in [3]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 15)
            points.append((x, y))
        if i in [4]:
            x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)) - 5)
            y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)) - 12)
            points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color_blue, thickness= thickness)



image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    pentagonNotWeight_0(img, 200, 250)
    pentagonNotWeight_1(img, 345, 215)
    pentagonNotWeight_2(img, 345, 290)
    pentagonNotWeight_3(img, 260, 175)
    pentagonNotWeight_4(img, 260, 343)
    cv2.imshow("STT 13", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
