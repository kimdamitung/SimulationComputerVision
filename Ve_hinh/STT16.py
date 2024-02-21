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


def pentagon_rotate(img, goto_X, goto_Y, radius=45, rotate=90, n=5):
    original_degree = 360 / n
    color_blue = (255, 0, 0)
    thickness = 2
    points = []
    mid_points = []
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
        points.append((x, y))
    #     if i in [1, 3]:
    #         print(f"({x},{y})")
    #         cv2.circle(img, (x, y), 3, color_blue, thickness)
    # print("None", end="\n")
    for i in range(n):
        next_i = (i + 1) % n 
        mid_x = int((points[i][0] + points[next_i][0]) / 2)
        mid_y = int((points[i][1] + points[next_i][1]) / 2)
        # print(f"Trung điểm {i}: {mid_x}, {mid_y}")
        # cv2.circle(img, (mid_x, mid_y), 3, (0, 255, 0), 2)
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color_blue, thickness=thickness)


def pentagon(img, goto_X, goto_Y, radius=120, rotate=270, n=5):
    original_degree = 360 / n
    color_blue = (255, 0, 0)
    thickness = 2
    points = []
    mid_points = []
    mid = np.array([
            [210, 397], 
            [266, 397],
            [154, 356],
            [136, 301],
            [158, 235],
            [204, 203],
            [273, 203],
            [319, 235],
            [340, 301],
            [322, 356]
        ], np.int32
    )
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
        points.append((x, y))
        match i:
            case 0:
                cv2.line(img, (x, y), mid[0], color_blue, thickness)
                cv2.line(img, (x, y), mid[1], color_blue, thickness)
            case 1:
                cv2.line(img, (x, y), mid[2], color_blue, thickness)
                cv2.line(img, (x, y), mid[3], color_blue, thickness)
            case 2:
                cv2.line(img, (x, y), mid[4], color_blue, thickness)
                cv2.line(img, (x, y), mid[5], color_blue, thickness)
            case 3:
                cv2.line(img, (x, y), mid[6], color_blue, thickness)
                cv2.line(img, (x, y), mid[7], color_blue, thickness)
            case 4:
                cv2.line(img, (x, y), mid[8], color_blue, thickness)
                cv2.line(img, (x, y), mid[9], color_blue, thickness)
    for i in range(n):
        next_i = (i + 1) % n 
        mid_x = int((points[i][0] + points[next_i][0]) / 2)
        mid_y = int((points[i][1] + points[next_i][1]) / 2)
        # pentagon_rotate(img, mid_x, mid_y)
        mid_points.append((mid_x, mid_y))
        match i:
            case 0:
                Ox = int(mid_x + 10 * np.sin(np.radians(- 36)))
                Oy = int(mid_y + 10 * np.cos(np.radians(- 36)))
                pentagon_rotate(img, Ox, Oy)
            case 1:
                Ox = int(mid_x + 10 * np.sin(np.radians(- original_degree - 36)))
                Oy = int(mid_y + 10 * np.cos(np.radians(- original_degree - 36)))
                pentagon_rotate(img, Ox, Oy)
            case 2:
                Ox = int(mid_x + 10 * np.sin(np.radians(- original_degree * 2 - 36)))
                Oy = int(mid_y + 10 * np.cos(np.radians(- original_degree * 2 - 36)))
                pentagon_rotate(img, Ox, Oy)
            case 3:
                Ox = int(mid_x + 10 * np.sin(np.radians(- original_degree * 3 - 36)))
                Oy = int(mid_y + 10 * np.cos(np.radians(- original_degree * 3 - 36)))
                pentagon_rotate(img, Ox, Oy)
            case 4:
                Ox = int(mid_x + 10 * np.sin(np.radians(- original_degree * 4 - 36)))
                Oy = int(mid_y + 10 * np.cos(np.radians(- original_degree * 4 - 36)))
                pentagon_rotate(img, Ox, Oy)



def Connect_lines(img):
    color_blue = (255, 0, 0)
    thickness = 2
    cv2.line(img, (265,228), (298,251), color_blue, thickness)
    cv2.line(img, (314,301), (301,341), color_blue, thickness)
    cv2.line(img, (258,372), (218,372), color_blue, thickness)
    cv2.line(img, (176,341), (163,301), color_blue, thickness)
    cv2.line(img, (179,251), (212,228), color_blue, thickness)

        
image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 240
Y = 300

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    pentagon(img, X, Y)
    Connect_lines(img)
    cv2.imshow("STT 16", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
