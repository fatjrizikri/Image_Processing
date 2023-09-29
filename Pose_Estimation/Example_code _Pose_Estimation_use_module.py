import cv2
import time
import Pose_Estimation_module as mp

cap = cv2.VideoCapture('Video/2.mp4')
pTime = 0
detector = mp.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.getPosition(img)
    # print(lmList) # to print all data point position of pose all point is 33 point of landmarks pose full body
    if len(lmList) !=0: # check the points of body landmarks whether they exist or not to prevent errors
        print(lmList[14]) # to print data point number 14 position of landmark pose body
        # to make diffrent circle point of position landmark body
        # (lmList[14][1], lmList[14][2]) value of (x ,y) posistion 2 dimension 
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime =cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0,), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord("q"):  # use q for exit
        break
    # cv2.waitKey(1) ## always on
