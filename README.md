# Fine-Tuned YOLOv8-Pose for Lower-body Keypoint Detection

In clinical research on Parkinson’s disease (PD) and other gait disorders, video recordings are often restricted to the lower body only to protect patient privacy.
However, pre-trained YOLO-pose models—originally trained on COCO-style full-body datasets—perform poorly on such lower-limb-only videos, failing to detect or localize keypoints accurately.
To address this limitation, I fine-tuned the YOLOv8-pose model on a custom dataset containing manually annotated lower-body keypoints, achieving significantly improved detection and tracking performance for gait analysis tasks.
In total, I manually annotated over 2,000 frames and validated the model on 30+ two-minute videos (≈100,000 frames).
For future applications, users can easily prepare their own datasets using CVAT
, export the annotations in YOLO format, and perform similar fine-tuning for other domain-specific tasks.

This repository provides a **fine-tuned YOLOv8-pose model** specialized for **lower-body (legs) keypoint detection** in gait videos.  
The model was trained on manually annotated lower-body data using **CVAT**(https://www.cvat.ai/), focusing on 10 keypoints:
> L & R Hip, L & R Knee, L & R Ankle, L & R Heel, L & R Foot.

---

## 1. Project Overview

The model was fine-tuned using **videos containing only the lower body of walking subjects**.  
Each frame was manually labeled in **CVAT** with 10 anatomical keypoints.  
Fine-tuning significantly improved YOLOv8's accuracy for lower-body pose estimation and tracking in gait analysis videos.

---

## 2. Installation

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
## 3. Run Inference on a Video
You can run YOLO directly from command line or Python

### Option1: Python script
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

### Option2: Command line
```bash
yolo pose predict model="best.pt" source="videos/example.mp4" conf=0.25 save=True
```

After completion, results (including annotated videos) will be saved under:
runs/pose/predict/

# 3. Model Information

Base model: YOLOv8n-pose (yolov8n-pose.pt)

Fine-tuned dataset: custom lower-body dataset (manually labeled via CVAT)

Keypoints per instance: 10
Training epochs: 200
Image size: 640
Optimizer: AdamW

# 4. Contact
If you have questions or want to collaborate:

Author: Yankai Zhao

Email: yaz624@lghigh.edu

Institution: Lehigh University, Department of Electrical and Computer Engineering
