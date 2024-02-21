import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 11: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 hình chữ nhật trên ảnh được mở từ camera
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

def regular_hexagon(img, goto_X, goto_Y, radius = 150, n = 6):
    points = [] 
    midpoints = []
    color = (0, 255, 255)
    thickness = 2
    for i in range(n):
        angle_rad = math.radians(i * 360 / n - 90)  # Góc quay -90 độ để ngũ giác đứng
        x = int(goto_X + radius * math.cos(angle_rad))
        y = int(goto_Y + radius * math.sin(angle_rad))
        points.append((x, y))
        # print(f"Điểm {i+1}: ({x}, {y})")  # In ra tọa độ của mỗi đỉnh
    for i in range(n):
        next_i = (i + 1) % n
        midpoint_x = (points[i][0] + points[next_i][0]) // 2
        midpoint_y = (points[i][1] + points[next_i][1]) // 2
        midpoints.append((midpoint_x, midpoint_y))
        # print(f"Trung điểm cạnh {i+1}-{next_i+1}: ({midpoint_x}, {midpoint_y})")  # In ra tọa độ của trung điểm
    for i in range(n):
        cv2.line(img, points[i], points[(i + 1) % n], color, thickness)
    for i in range(int(n / 2)):
        cv2.line(img, points[i], points[i + int(n / 2)], color, thickness)


image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    regular_hexagon(img, X, Y)
    cv2.imshow("STT 11", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
