import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 18: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ một hình lục giác trên ảnh được mở từ camera
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


def square_rotate(img, goto_X, goto_Y, radius = 200, color = (0, 0, 255), n = 4, rotate = 45):
    original_degree = 360 / n
    thickness = 2
    points = []
    mid_points = []
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree + rotate)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree + rotate)))
        points.append((x, y))
    for i in range(n):
        next_i = (i + 1) % n 
        mid_points.append(points[i])
        for j in range(1, 8):
            mid_x = int((points[i][0] * (8 - j) + points[next_i][0] * j) / 8)
            mid_y = int((points[i][1] * (8 - j) + points[next_i][1] * j) / 8)
            mid_points.append((mid_x, mid_y))
            # cv2.circle(img, (mid_x, mid_y), 3, color, thickness)
        mid_points.append(points[next_i])
    # for i, point in enumerate(mid_points):
    #     print(f"Điểm trung gian {i + 1}: {point}")
    mid_points = np.array(mid_points, np.int32)
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color, thickness=thickness)


def connect_lines(img):
    points = np.array(
        [
            [310, 441],
            [271, 392],
            [239, 441],
            [207, 392],
            [168, 441],
            [98, 370],
            [147, 331],
            [98, 299],
            [147, 267],
            [98, 228],
            [168, 158],
            [207, 207],
            [239, 158],
            [271, 207],
            [310, 158],
            [381, 228],
            [332, 267],
            [381, 299],
            [332, 331],
            [381, 370]
        ], np.int32
    )
    cv2.polylines(img, [points], isClosed=True, color=(0, 0, 255), thickness=2)


image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    square_rotate(img, X, Y)
    square_rotate(img, X, Y, radius = 60, color=(211, 85, 486))
    cv2.circle(img, (X, Y), 40, (255, 255, 0), -1)
    connect_lines(img)
    cv2.imshow("STT 24", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
