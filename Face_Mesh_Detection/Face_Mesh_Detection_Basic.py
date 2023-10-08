import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 1) #to add face to process face mesh detection
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1) 

while True:
    succesS,img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = faceMesh.process(imgRGB)
    # print(results)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)

            for id, lm in enumerate(faceLms.landmark):
                # print(lm)
                ih, iw, ic = img.shape
                x, y, = int(lm.x * iw), int(lm.y * ih)
                print(id, x, y)

    cTime =time.time()
    fps = 1 / (cTime - pTime)
    pTime =cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # use q for exit
        break
    # cv2.waitKey(1) ## always on
