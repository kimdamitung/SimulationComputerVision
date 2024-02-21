import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 8: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 hình elip trên ảnh được mở từ camera
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

def draw_parallelogram(img, goto_X, goto_Y):
    square_base_edge = 60
    hypotenuse = 30
    points = np.array(
        [
            [goto_X - square_base_edge - hypotenuse, goto_Y + hypotenuse],
            [goto_X - hypotenuse, goto_Y + hypotenuse], # chéo
            [goto_X - hypotenuse, goto_Y + square_base_edge + hypotenuse],
            [goto_X, goto_Y + square_base_edge], #thẳng
            [goto_X + hypotenuse, goto_Y + square_base_edge + hypotenuse],
            [goto_X + hypotenuse, goto_Y + hypotenuse], #chéo
            [goto_X + square_base_edge + hypotenuse, goto_Y + hypotenuse],
            [goto_X + square_base_edge, goto_Y], #thẳng
            [goto_X + square_base_edge + hypotenuse, goto_Y - hypotenuse],
            [goto_X + hypotenuse, goto_Y - hypotenuse], #chéo
            [goto_X + hypotenuse, goto_Y - square_base_edge - hypotenuse],
            [goto_X, goto_Y - square_base_edge], #thẳng
            [goto_X - hypotenuse, goto_Y - square_base_edge - hypotenuse],
            [goto_X - hypotenuse, goto_Y - hypotenuse], #chéo
            [goto_X - square_base_edge - hypotenuse, goto_Y - hypotenuse],
            [goto_X - square_base_edge, goto_Y] #thẳng
        ],
        np.int32
    )
    cv2.polylines(img, [points], isClosed= True, color=(255, 255, 255), thickness=2)
    # connect line chéo tới tâm Oxy
    cv2.line(img, (goto_X, goto_Y), (goto_X - hypotenuse, goto_Y + hypotenuse), (255, 255, 255), thickness=2)
    cv2.line(img, (goto_X, goto_Y), (goto_X + hypotenuse, goto_Y + hypotenuse), (255, 255, 255), thickness=2)
    cv2.line(img, (goto_X, goto_Y), (goto_X + hypotenuse, goto_Y - hypotenuse), (255, 255, 255), thickness=2)
    cv2.line(img, (goto_X, goto_Y), (goto_X - hypotenuse, goto_Y - hypotenuse), (255, 255, 255), thickness=2)
    # connect line thẳng tới tâm Oxy
    cv2.line(img, (goto_X, goto_Y), (goto_X, goto_Y + square_base_edge), (255, 255, 255), thickness=2)
    cv2.line(img, (goto_X, goto_Y), (goto_X + square_base_edge, goto_Y), (255, 255, 255), thickness=2)
    cv2.line(img, (goto_X, goto_Y), (goto_X, goto_Y - square_base_edge), (255, 255, 255), thickness=2)
    cv2.line(img, (goto_X, goto_Y), (goto_X - square_base_edge, goto_Y), (255, 255, 255), thickness=2)

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
#đều chỉnh tọa độ
X = 200
Y = 250

if img is not None:
    name = 'Nguyen Duy Tung'
    Write_Text_Img(img, 0, 600, name)
    draw_parallelogram(img, X, Y)
    cv2.imshow("STT 8", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    Check_size(img)
else:
    print("Lỗi. Không dẫn được ảnh")
