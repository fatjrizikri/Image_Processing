# if ubuntu can't play video maybe you must to install
# sudo apt-get install ubuntu-restricted-extras
# this code same like code Hands Tarcking
import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose #this code to call solutions of body pose from mediapipe lib 
pose = mpPose.Pose() #this code to call code parameter to get landmarks of body from mediapipe lib

cap = cv2.VideoCapture('Video/2.mp4')
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results) #to know mediapipe work to get possition landmarks of pose full body
    # print(results.pose_landmarks) #to get possition landmarks of pose full body
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            # cx, xy (possition id landmark), 10 (diameter of circle), 255,0,0 (Value color RGB Red, Grean, Blue)
            cv2.circle(img, (cx,cy), 10, (255, 0 , 0), cv2.FILLED)



    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime =cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0,), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord("q"):  # use q for exit
        break
    # cv2.waitKey(1) ## always on