# Fine-Tuned YOLOv8-Pose for Lower-Limb Keypoint Detection

This repository provides a **fine-tuned YOLOv8-pose model** specialized for **lower-body (legs) keypoint detection** in gait videos.  
The model was trained on manually annotated lower-limb data using **CVAT**, focusing on 10 keypoints:
> L & R Hip, L & R Knee, L & R Ankle, L & R Heel, L & R Foot.

---

## Project Overview

The model was fine-tuned using **videos containing only the lower body of walking subjects**.  
Each frame was manually labeled in **CVAT** with 10 anatomical keypoints.  
Fine-tuning significantly improved YOLOv8's accuracy for lower-limb pose estimation and tracking in gait analysis videos.

---

## Installation

```bash
# 1. Clone this repository
git clone https://github.com/yankaizhao322/Fine-Tuned-YOLOv8-Pose-Lower-body-Keypoints-Motion-Tracking/tree/main

cd Fine-Tuned-YOLOv8-Pose-Lower-body-Keypoints-Motion-Tracking

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate     # on macOS/Linux
venv\Scripts\activate        # on Windows

# 3. Install dependencies
pip install ultralytics opencv-python

# Folder Structure
```bash
├── best.pt                          # Fine-tuned YOLOv8-pose weights
├── videos/                          # Folder containing test videos
│   └── example.mp4                  # Your video file
├── README.md                        # This file
└── frame_extraction_from_video.py                 # Video Frame Extraction(30HZ)
```
# Run Inference on a Video
You can run YOLO directly from command line or Python

## Option1: Python script
```python
from ultralytics import YOLO

# Load fine-tuned model
model = YOLO("best.pt")

# Run on your video
results = model.predict(
    source="videos/example.mp4",  # your input video
    conf=0.25,                    # confidence threshold
    save=True                     # save output video with keypoints
)

print("Inference complete! Check the 'runs/pose/predict' folder.")
```

## Option2: Command line
```bash
yolo pose predict model="best.pt" source="videos/example.mp4" conf=0.25 save=True
```

After completion, results (including annotated videos) will be saved under:
runs/pose/predict/

# Model Information

Base model: YOLOv8n-pose (yolov8n-pose.pt)

Fine-tuned dataset: custom lower-limb dataset (manually labeled via CVAT)

Keypoints per instance: 10
Training epochs: 200
Image size: 640
Optimizer: AdamW

# Contact
If you have questions or want to collaborate:

Author: Yankai Zhao

Email: yaz624@lghigh.edu

Institution: Lehigh University, Department of Electrical and Computer Engineering
