import cv2 
import numpy as np

image_path = "img/input_06_2.png"
img = cv2.imread(image_path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
edges = cv2.Canny(imgBlur, 0, 50)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    cv2.drawContours(img, [approx], -1, (0, 69, 255), 2)

cv2.imshow("Testing", img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()