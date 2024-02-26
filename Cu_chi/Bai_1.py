import cv2
import time 
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
hands_videos = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def detectHandsLandmarks(image, hands, draw=True):
	output_image = image.copy()
	imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)
	if results.multi_hand_landmarks and draw:
		for hand_landmarks in results.multi_hand_landmarks:
			mp_drawing.draw_landmarks(image=output_image,
						landmark_list=hand_landmarks,
						connections=mp_hands.HAND_CONNECTIONS,
						landmark_drawing_spec=mp_drawing.DrawingSpec(
												color=(255, 255, 255),
												thickness=2,
												circle_radius=2
											),
						connection_drawing_spec=mp_drawing.DrawingSpec(
												color=(0, 255, 0),
												thickness=2,
												circle_radius=2
											)		
			)
	return output_image, results

def countFinger(image, results, draw=True):
	height, width, _ = image.shape
	output_image = image.copy()
	count = {'RIGHT': 0, 'LEFT': 0}
	finger_tip_ids = [
				mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
				mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP
	]

	"""
	thumb: cái
	index: trỏ
	middle: giữa
	ring: áp út
	pinky: út
	"""
	fingers_statuses = {
					'RIGHT_THUMB': False,
					'RIGHT_INDEX': False,
					'RIGHT_MIDDLE': False,
					'RIGHT_RING': False,
					'RIGHT_PINKY': False,
					'LEFT_THUMB': False,
					'LEFT_INDEX': False,
					'LEFT_MIDDLE': False,
					'LEFT_RING': False,
					'LEFT_PINKY': False
	}
	for hand_index, hand_info in enumerate(results.multi_handedness):
		hand_label = hand_info.classification[0].label
		hand_landmarks = results.multi_hand_landmarks[hand_index]
		for tip_index in finger_tip_ids:
			finger_name = tip_index.name.split("_")[0]
			if(hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y):
				fingers_statuses[hand_label.upper() + "_" + finger_name] = True
				count[hand_label.upper()] += 1
		thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
		thumb_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x
		if(hand_label == 'Right' and (thumb_tip_x < thumb_mcp_x)) or (hand_label == 'Left' and (thumb_tip_x > thumb_mcp_x)):
			fingers_statuses[hand_label.upper() + "_THUMB"] = True
			count[hand_label.upper()] += 1
	if draw:
		cv2.putText(output_image, "Counter finger: ", (20, 30),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
		cv2.putText(output_image, str(sum(count.values())), (width // 3 - 100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
	return output_image, fingers_statuses, count

def annotate(image, results, fingers_statuses, count):
	height, width, _ = image.shape
	output_image = image.copy()
	HANDS_IMGS_PATHS = {
		'LEFT': ['media/left_hand_not_detected.png'],
		'RIGHT': ['media/right_hand_not_detected.png']
	}
	if results.multi_hand_landmarks:
		for hand_index, hand_info in enumerate(results.multi_handedness):
			hand_label = hand_info.classification[0].label
			HANDS_IMGS_PATHS[hand_label.upper()] = ['media/' + hand_label.lower() + '_hand_detected.png']
			if count[hand_label.upper()] == 5:
				HANDS_IMGS_PATHS[hand_label.upper()] = ['media/' + hand_label.lower() + '_all_fingers.png']
			else:
				for finger, status in fingers_statuses.items():
					if status == True and finger.split("_")[0] == hand_label.upper():
						HANDS_IMGS_PATHS[hand_label.upper()].append('media/' + finger.lower() + '.png')
	for hand_index, hand_imgs_paths in enumerate(HANDS_IMGS_PATHS.values()):
		for img_path in hand_imgs_paths:
			hand_imageBGRA = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
			alpha_channel = hand_imageBGRA[:, :, -1]
			hand_imageBGR = hand_imageBGRA[:, :, :-1]
			hand_height, hand_width, _ = hand_imageBGR.shape
			ROI = output_image[30 : 30 + hand_height, (hand_index * width // 2) + width // 12 : ((hand_index * width // 2) + width // 12 + hand_width)]
			ROI[alpha_channel == 255] = hand_imageBGR[alpha_channel == 255]
			output_image[30 : 30 + hand_height, (hand_index * width // 2) + width // 12 : ((hand_index * width // 2) + width // 12 + hand_width)] = ROI
	return output_image


camera_video = cv2.VideoCapture(0)
camera_video.set(3, 1980)
camera_video.set(4, 960)
# cv2.namedWindow('Duy Tung Counter Fingers', cv2.WINDOW_NORMAL)
fingers_statuses = None
while camera_video.isOpened():
	ok, frame = camera_video.read()
	if not ok:
		continue
	frame = cv2.flip(frame, 1)
	frame, results = detectHandsLandmarks(frame, hands_videos)
	if results.multi_hand_landmarks:
		frame, fingers_statuses, count = countFinger(frame, results)
	# if fingers_statuses is not None:
	# 	frame = annotate(frame, results, fingers_statuses, count)
	cv2.imshow("Fingers Counter", frame)
	k = cv2.waitKey(1) & 0xFF
	if(k == 27):
		break
camera_video.release()
cv2.destroyAllWindows()