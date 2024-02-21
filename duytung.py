import cv2
import numpy as np

# Đường dẫn tới hình ảnh
image_path = "D:/Thuc_Hanh/Ky_6_2024/BaiTapThiGiacMayTinh/BaiTapMoPhongNhom/img/kimdami.jpg"

# Đọc hình ảnh từ đường dẫn
img = cv2.imread(image_path)

# Kích thước hình ảnh
height, width, _ = img.shape

# Tạo ma trận quay
angle = 30
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

# Tính toán các đỉnh của hình vuông
side_length = 200
half_side = side_length // 2
square = np.array([[-half_side, -half_side],
                   [half_side, -half_side],
                   [half_side, half_side],
                   [-half_side, half_side]])

# Áp dụng ma trận quay vào hình vuông
rotated_square = cv2.transform(np.array([square]), rotation_matrix)

# Dịch chuyển hình vuông về trung tâm của hình ảnh
# translated_square = rotated_square + np.array([[center[0], center[1]]])

# Vẽ hình vuông lên hình ảnh
color = (255, 0, 0)  # Màu xanh lá cây
thickness = 2
cv2.polylines(img, [np.int32(rotated_square)], isClosed=True, color=color, thickness=thickness)

# Hiển thị hình ảnh với hình vuông đã vẽ
cv2.imshow('Rotated Square', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
