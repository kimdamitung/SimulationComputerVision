import cv2

image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/input_06.png"
img = cv2.imread(image_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_gray)
print("Giá trị ngưỡng nhỏ nhất:", min_val)
print("Giá trị ngưỡng lớn nhất:", max_val)

points_approx = []
points = []
ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for idx, cnt in enumerate( contours):
    epsilon = 0.015 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)
    text = str(idx)
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)
    text_x = x + (w - text_size[0]) // 2
    text_y = y + (h + text_size[1]) // 2
    if len(approx) == 4:
        print(f"{idx}: {len(approx)}")
        cv2.drawContours(img, [approx], -1, (0, 69, 255), 2)
        cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)


cv2.imshow("Gray Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
