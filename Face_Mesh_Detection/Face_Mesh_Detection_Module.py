import cv2
import mediapipe as mp
import time


class FaceMeshDetector():
    def __init__(self, staticMode = False, maxFaces = 2, minDetectionCon = False, TrackCon = False):
        #configration default from mediapipe Face Mesh Detector
        # static_image_mode = False
        # max_num_faces = 1
        # min_detection_confidence = 0.5
        # min_tracking_confidence = 0.5

        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.TrackCon = TrackCon


        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.minDetectionCon, self.TrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 1) 

    def findFaceMesh(self, img, draw = True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.results = self.faceMesh.process(self.imgRGB)
        # print(results)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION, self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                # print(lm)
                    ih, iw, ic = img.shape
                    x, y, = int(lm.x * iw), int(lm.y * ih)
                    # print(id, x, y)
                    # cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 255, 0), 1)
    
                    face.append([x, y])
                faces.append(face)
        return img, faces

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceMeshDetector(maxFaces=2)
    while True:
        succesS,img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces)!=0:
            print(len(faces)) # to count face detection
            # print(len(faces[0])) #to get data position id of point landmark face mesh detection
            # print(faces[0]) #to get all data position point landmark face mesh detection
            
        cTime =time.time()
        fps = 1 / (cTime - pTime)
        pTime =cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):  # use q for exit
            break
        # cv2.waitKey(1) ## always on

if __name__ == "__main__":
    main()