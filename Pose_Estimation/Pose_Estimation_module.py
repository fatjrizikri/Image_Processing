# if ubuntu can't play video maybe you must to install
# sudo apt-get install ubuntu-restricted-extras
# this code same like code Hands Tarcking
import cv2
import mediapipe as mp
import time

class poseDetector():
    #this code basic code of object oriented programming
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=False, trackCon=False):
    #  in this parameter only boolean value you can set (False or True)
    # this default prameter from lib mediapipe pose object
    # static_image_mode = False,
    # upper_body_only = False,
    # smooth_landmark = True,
    # min_tracking_confidence = 0.5,
    # min_detection_confidence = 0.5

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose #this code to call solutions of body pose from mediapipe lib 
        
        #this code to call code parameter to get landmarks of body from mediapipe lib
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)
        
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    
    def getPosition(self, img, draw = True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)    
                # cx, xy (possition id landmark), 10 (diameter of circle), 255,0,0 (Value color RGB Red, Grean, Blue)                
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 10, (255, 0 , 0), cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture('Video/2.mp4')
    pTime = 0
    detector = poseDetector()
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

if __name__ == "__main__":
    main()