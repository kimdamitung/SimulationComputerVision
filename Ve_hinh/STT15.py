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

def hexagon(img, goto_X, goto_Y, radius=150, n=6):
    original_degree = 360 / n
    points = []
    points_mid = []
    points_0_3 = []
    points_1_4 = [] 
    points_2_5 = []  
    color = (211, 85, 486)
    thickness = 2
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree)))
        points.append((x, y))
        # print(f"Tọa độ đỉnh {i+1}: ({x}, {y})")
    for i in range(n):
        for j in range(4):
            segment_x = int((points[i][0] * (3 - j) + points[(i + n//2) % n][0] * (1 + j)) / 4)
            segment_y = int((points[i][1] * (3 - j) + points[(i + n//2) % n][1] * (1 + j)) / 4)
            if j == 0:
                points_mid.append((segment_x, segment_y))
            # print(f"Tọa độ điểm trên đoạn {j+1} của đường chéo {i+1}-{(i + n//2) % n + 1}: ({segment_x}, {segment_y})")
                if i == 0 or i == 3:
                    points_0_3.append((segment_x, segment_y))
                if i == 1 or i == 4:
                    points_1_4.append((segment_x, segment_y))
                if i == 2 or i == 5:
                    points_2_5.append((segment_x, segment_y))
        next_i = (i + 1) % n 
        mid_x = int((points[i][0] + points[next_i][0]) / 2)
        mid_y = int((points[i][1] + points[next_i][1]) / 2)
        points_mid.append((mid_x, mid_y))
        # print(f"Tọa độ trung điểm cạnh {i+1}-{next_i+1}: ({mid_x}, {mid_y})")
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color, thickness=thickness)
    points_mid = np.array(points_mid, np.int32)
    cv2.polylines(img, [points_mid], isClosed=True, color=color, thickness=thickness)
    cv2.line(img, points_0_3[0], points_0_3[1], color, thickness)
    cv2.line(img, points_1_4[0], points_1_4[1], color, thickness)
    cv2.line(img, points_2_5[0], points_2_5[1], color, thickness)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    hexagon(img, X, Y)
    cv2.imshow("STT 15", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
