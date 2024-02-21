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

def hexagon(img, goto_X, goto_Y, radius = 210, rotate = 90, n = 6):
    original_degree = 360 / n
    color = (255, 0, 0)
    thickness = 2
    points= []
    points_024 = []
    points_135 = []
    for i in range(n):
        x = int(goto_X + radius / 3 * 2 * np.cos(np.radians(i * original_degree - rotate)))
        y = int(goto_Y + radius / 3 * 2 * np.sin(np.radians(i * original_degree - rotate)))
        points.append((x, y))
        if i in [0, 2, 4]:
            cv2.line(img, (goto_X, goto_Y), (x, y), color, thickness)
            points_024.append((x, y))
        if i in [1, 3, 5]:
            points_135.append((x, y))
    for i in range(n):
        cv2.circle(img, points[i], int(radius / 3), color=(255, 255, 255), thickness=2)
    cv2.circle(img, (goto_X, goto_Y), radius, color=(255, 255, 255), thickness=2)
    points = np.array(points, np.int32)
    points_024 = np.array(points_024, np.int32)
    points_135 = np.array(points_135, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color, thickness=thickness)
    cv2.polylines(img, [points_024], isClosed=True, color=(0, 0, 255), thickness=2)
    cv2.polylines(img, [points_135], isClosed=True, color=(0, 0, 255), thickness=2)




image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    hexagon(img, X, Y)
    cv2.imshow("STT 19", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
