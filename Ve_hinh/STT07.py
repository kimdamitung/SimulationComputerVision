import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 7: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường hình vuông trên ảnh được mở từ camera
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
(429, 356)
(281, 299)
(256, 456)
(231, 299)
(82, 356)
(206, 256)
(82, 156)
(230, 212)
(255, 56)
(281, 212)
(429, 156)
(306, 256)
"""
def Star_6_points(img, goto_X, goto_Y, rotation, size):
    color = (128, 0, 128)
    thickness = 2
    points = []
    for i in range(6):
        x = int(goto_X + size * np.cos(i * np.pi / 3 + rotation))
        y = int(goto_Y + size * np.sin(i * np.pi / 3 + rotation))
        points.append((x, y))
        x = int(goto_X + size/4 * np.cos((i + 0.5) * np.pi / 3 + rotation))
        y = int(goto_Y + size/4 * np.sin((i + 0.5) * np.pi / 3 + rotation))
        points.append((x, y))
    cv2.polylines(img, [np.array(points)], isClosed=True, color=color, thickness=thickness)
    for point in points:
        print("Point:", point)

def Connect_lines(img, X, Y):
    Star_6_points(img, X, Y, np.pi / 6, size=200)
    # cv2.circle(img, (230, 212), 3, (255, 0, 0), thickness=1) #1
    # cv2.circle(img, (281, 212), 3, (255, 0, 0), thickness=1) #2
    # cv2.circle(img, (306, 256), 3, (255, 0, 0), thickness=1) #3
    cv2.line(img, (230, 212), (281, 299) ,(128, 0, 128), 2)
    cv2.line(img, (281, 212), (230, 299) ,(128, 0, 128), 2)
    cv2.line(img, (306, 256), (206, 256) ,(128, 0, 128), 2)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 0
Y = 0



if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    Connect_lines(img, X + 256, Y + 256)
    cv2.imshow("STT 7", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
