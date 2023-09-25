# ===== handtracking =====
import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)  # default camera (0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = hands.process(imgRGB)
    # print(results)  # to check results from lib mediapipe to use data hands
    # print(results.multi_hand_landmarks)  # to detect hand and get landmarks x,y,z

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(
                handLms.landmark
            ):  # get data from lib mediapipe to get x, y point of landmarks hands you should read doc mediapipe
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 0: #use if for to know number of point of landmarks hands
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # use q for exit
        break
    # cv2.waitKey(1) ## always on
