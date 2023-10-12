# Image_Processing
```
pip install mediapipe
```
```
pip install opencv-python
```
```
pip install numpy
```
```
pip install math
```
## mediapipe
### Pose Landmarks
 Information from https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
 
#### Pose landmarker model
The pose landmarker model tracks 33 body landmark locations, representing the approximate location of the following body parts:
- 0 - nose
- 1 - left eye (inner)
- 2 - left eye
- 3 - left eye (outer)
- 4 - right eye (inner)
- 5 - right eye
- 6 - right eye (outer)
- 7 - left ear
- 8 - right ear
- 9 - mouth (left)
- 10 - mouth (right)
- 11 - left shoulder
- 12 - right shoulder
- 13 - left elbow
- 14 - right elbow
- 15 - left wrist
- 16 - right wrist
- 17 - left pinky
- 18 - right pinky
- 19 - left index
- 20 - right index
- 21 - left thumb
- 22 - right thumb
- 23 - left hip
- 24 - right hip
- 25 - left knee
- 26 - right knee
- 27 - left ankle
- 28 - right ankle
- 29 - left heel
- 30 - right heel
- 31 - left foot index
- 32 - right foot index
  The model output contains both normalized coordinates (Landmarks) and world coordinates (WorldLandmarks) for each landmark.

### Hand landmarks detection
information from https://developers.google.com/mediapipe/solutions/vision/hand_landmarker

#### Models
The Hand Landmarker uses a model bundle with two packaged models: a palm detection model and a hand landmarks detection model. You need a model bundle that contains both these models to run this task.
![image](https://github.com/fatjrizikri/Image_Processing/assets/66940604/ac11f25c-1feb-4f4f-bd07-48f6632a3ebf)

### Face landmark detection
information from https://developers.google.com/mediapipe/solutions/vision/face_landmarker
#### Features
- Input image processing - Processing includes image rotation, resizing, normalization, and color space conversion.
- Score threshold - Filter results based on prediction scores.
#### Configurations options
![image](https://github.com/fatjrizikri/Image_Processing/assets/66940604/20dcefff-a98f-48f7-bf6a-b0f6233bf4dc)
#### Models
The Face Landmarker uses a series of models to predict face landmarks. The first model detects faces, a second model locates landmarks on the detected faces, and a third model uses those landmarks to identify facial features and expressions.

The following models are packaged together into a downloadable model bundle:

- Face detection model: detects the presence of faces with a few key facial landmarks.
- Face mesh model: adds a complete mapping of the face. The model outputs an estimate of 478 3-dimensional face landmarks.
- Blendshape prediction model: receives output from the face mesh model predicts 52 blendshape scores, which are coefficients representing facial different expressions.

![image](https://github.com/fatjrizikri/Image_Processing/assets/66940604/134d2318-423d-41e5-b2b8-0dffa6511ea0)


## Information
- if code use lib module you must save code module and your project to same file
- some project not have detection object to process. you must input your object to get process with this code
- This code may be the same as the one on the internet. because I'm still learning this machine learning, which I think can be used in the project I want to make.
  
