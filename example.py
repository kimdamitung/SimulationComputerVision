import cv2
import numpy as np

def Write_Text_Img(img, goto_X, goto_Y, name):
    text = "Ho va ten: " + name
    position = (goto_X, goto_Y)
    font = cv2.FONT_ITALIC
    scale = 1
    color = (0, 0, 255)
    thickness = 2
    cv2.putText(img, text, position, font, scale, color,thickness)

def Check_Size(img):
    height = img.shape[0]
    width = img.shape[1]
    return height, width

def square(img, goto_X, goto_Y, radius=160, rotate=45, n=4):
    original_degree = 360 / n
    color = (0, 0, 255)
    thickness = 2
    points = []
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree - rotate)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree - rotate)))
        points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color, thickness=thickness)

def hexagon_rotate(img, goto_X, goto_Y, radius=60, rotate=30, n=6):
    original_degree = 360 / n
    color = (0, 0, 255)
    thickness = 2
    points = []
    for i in range(n):
        x = int(goto_X + radius * np.cos(np.radians(i * original_degree)))
        y = int(goto_Y + radius * np.sin(np.radians(i * original_degree)))
        points.append((x, y))
    points = np.array(points, np.int32)
    cv2.polylines(img, [points], isClosed=True, color=color, thickness=thickness)


image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"
img = cv2.imread(image_path)
if img is not None:
    Write_Text_Img(img, 0, 600, "Nguyen Duy Tung")
    cv2.imshow("STT01", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Height, width: ", Check_Size(img))
else:
    print("ERROR")