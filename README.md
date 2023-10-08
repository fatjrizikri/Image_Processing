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
#### Features:
- Input image processing - Processing includes image rotation, resizing, normalization, and color space conversion.
- Score threshold - Filter results based on prediction scores.

#### Configurations options
This task has the following configuration options:
![image](https://github.com/fatjrizikri/Image_Processing/assets/66940604/966ec868-1674-4492-b528-75bc5c69f75b)
 
#### Pose landmarker model
The pose landmarker model tracks 33 body landmark locations, representing the approximate location of the following body parts:
![image](https://github.com/fatjrizikri/Image_Processing/assets/66940604/81fb5023-bc27-4130-b071-00d3070e5519)

0 - nose
1 - left eye (inner)
2 - left eye
3 - left eye (outer)
4 - right eye (inner)
5 - right eye
6 - right eye (outer)
7 - left ear
8 - right ear
9 - mouth (left)
10 - mouth (right)
11 - left shoulder
12 - right shoulder
13 - left elbow
14 - right elbow
15 - left wrist
16 - right wrist
17 - left pinky
18 - right pinky
19 - left index
20 - right index
21 - left thumb
22 - right thumb
23 - left hip
24 - right hip
25 - left knee
26 - right knee
27 - left ankle
28 - right ankle
29 - left heel
30 - right heel
31 - left foot index
32 - right foot index

## Information
- if code use lib module you must save code module and your project to same file
- some project not have detection object to process. you must input your object to get process with this code
- This code may be the same as the one on the internet. because I'm still learning this machine learning, which I think can be used in the project I want to make.
