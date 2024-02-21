import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 9: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường elip trên ảnh được mở từ camera
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

def four_propellers(img, goto_X, goto_Y):
    lenght = 400
    width = 350
    color = (255, 255, 255) #màu trắng
    thickness = 2
    # vẽ hình chữ nhật test hình stt9
    # cv2.rectangle(img, (int(goto_X - (lenght / 2)), int(goto_Y + (width / 2))), (int(goto_X + (lenght / 2)), int(goto_Y - (width / 2))), color, thickness)
    lenght_k = lenght / 100 * 60
    width_k = width / 100 * 70
    # vẽ hình tam giác đầu tên
    triangle_1 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X + lenght_k - lenght, goto_Y + width / 2],
            [goto_X - lenght_k + lenght, goto_Y + width / 2]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_1], isClosed=True, color=(255, 255, 255), thickness = 2)
    # vẽ hình tam giác thứ hai
    triangle_2 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X + lenght_k - lenght, goto_Y - width / 2],
            [goto_X - lenght_k + lenght, goto_Y - width / 2]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_2], isClosed=True, color=(255, 255, 255), thickness = 2)
    # vẽ hình tam giác thứ ba
    triangle_3 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X + lenght / 2, goto_Y + width - width_k],
            [goto_X + lenght / 2, goto_Y - width + width_k]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_3], isClosed=True, color=(255, 255, 255), thickness = 2)
    # vẽ hình tam giác thứ tư
    triangle_4 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X - lenght / 2, goto_Y + width - width_k],
            [goto_X - lenght / 2, goto_Y - width + width_k]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_4], isClosed=True, color=(255, 255, 255), thickness = 2)


image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 250
Y = 250
# Tọa độ của 4 đỉnh của hình bình hành


if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    four_propellers(img, X, Y)
    cv2.imshow("STT 9", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
