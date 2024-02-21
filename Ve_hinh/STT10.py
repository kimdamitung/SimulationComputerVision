import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 10: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường chữ nhật trên ảnh được mở từ camera
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

def regular_pentagon(img, goto_X, goto_Y, radius = 240):
    points = []
    midpoints = []
    color = (255, 0, 0)
    thickness = 2
    for i in range(5):
        angle_rad = math.radians(i * 360 / 5 - 90)  # Góc quay -90 độ để ngũ giác đứng
        x = int(goto_X + radius * math.cos(angle_rad))
        y = int(goto_Y + radius * math.sin(angle_rad))
        points.append((x, y))
        # print(f"Điểm {i+1}: ({x}, {y})")  # In ra tọa độ của mỗi đỉnh
    for i in range(5):
        next_i = (i + 1) % 5
        midpoint_x = (points[i][0] + points[next_i][0]) // 2
        midpoint_y = (points[i][1] + points[next_i][1]) // 2
        midpoints.append((midpoint_x, midpoint_y))
        # print(f"Trung điểm cạnh {i+1}-{next_i+1}: ({midpoint_x}, {midpoint_y})")  # In ra tọa độ của trung điểm
    for i in range(5):
        cv2.line(img, points[i], points[(i + 1) % 5], color, thickness)


def connect_line(img):
    # 2 4 1 3 5
    # star to
    star_big = np.array(
        [
            [125, 142],
            [240, 225],
            [354, 142],
            [311, 276],
            [424, 359],
            [284, 359],
            [239, 494],
            [195, 359],
            [54, 359],
             [168, 276]
        ], np.int32
    )
    cv2.polylines(img, [star_big], isClosed=True, color=(255, 0, 0), thickness=2)
    # star nhỏ
    # # 1 4 3 5 2
    star_small = np.array(
        [
            [240, 225],
            [195, 360],
            [311, 276],
            [168, 276],
            [284, 360]            
        ], np.int32
    )
    cv2.polylines(img, [star_small], isClosed=True, color=(255, 0, 0), thickness=2)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    # print("hình to")
    regular_pentagon(img, X, Y)
    # print("hình nhỏ")
    # regular_pentagon(img, X, Y, radius = 75)
    # cv2.circle(img , (311, 276), 3, (255, 0, 0), 2)
    connect_line(img)
    cv2.imshow("STT 10", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
