import cv2
import cvzone
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
	success, img = cap.read()
	imgText = np.zeros_like(img)
	img, faces = detector.findFaceMesh(img, draw=False)
	if faces:
		face = faces[0]
		pointLeft = face[145]
		pointRight = face[374]
		cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
		cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
		w, _ = detector.findDistance(pointLeft, pointRight)
		# focal lenght
		W = 6.3
		# d = 50
		# f = (w * d) / W
		f = 840
		d = (W * f) / w
		print(d)
		cvzone.putTextRect(img, f'Khoang cach: {int(d)}cm', (face[10][0] - 100, face[10][1] - 50), scale=2)
	imgStacked = cvzone.stackImages([img, imgText], 2, 1)
	cv2.imshow("img", imgStacked)
	k = cv2.waitKey(1) & 0xFF
	if(k == 27):
		break
cv2.destroyAllWindows()