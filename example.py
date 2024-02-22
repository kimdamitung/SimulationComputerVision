import cv2
import numpy as np

# Đọc ảnh và chuyển đổi thành ảnh xám
image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/input_06.png"
img = cv2.imread(image_path)
height, width = img.shape[:2]
new_height = int(height * 0.9)
new_width = int(width * 0.9)
img = cv2.resize(img, (new_width, new_height))

# code
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholds = cv2.threshold(imgGrey, 0, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresholds, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.025 * cv2.arcLength(cnt, True), True)
    # cv2.drawContours(img, [approx], 0, (128, 128, 128), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(len(approx))
    if len(approx) == 3:
        cv2.drawContours(img, [approx], 0, (128, 69, 128), 5)
        cv2.putText(img, "Shape", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (128, 128, 128))

cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()