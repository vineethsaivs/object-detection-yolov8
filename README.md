# **Object Detection Using YOLOv8**

This project demonstrates object detection using the YOLOv8 model. It supports detection on images, videos, and real-time webcam streams. The repository contains sample scripts to run YOLOv8 on various media and displays bounding boxes, confidence scores, and detected class names.

---

## **Features**
- **Image Detection**: Perform object detection on static images.
- **Video Detection**: Detect objects in video files with real-time processing.
- **Webcam Detection**: Detect objects live from a webcam feed.
- **Customizable**: Easily switch between different detection sources.

---

## **Setup and Requirements**

### **1. Clone the Repository**
```bash
git clone https://github.com/vineethsaivs/object-detection-yolov8.git
cd object-detection-yolov8
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Download YOLOv8 Model**
Ensure the `yolov8n.pt` file is present in the project directory. If not, download it from the [Ultralytics YOLOv8 repository](https://github.com/ultralytics/ultralytics).

---

## **Usage**

### **Image Detection**
To run YOLOv8 on a single image (e.g., `car.jpeg` in the `images` folder):
```bash
python running_yolo/yolo.py
```
This will display the image with bounding boxes and detected class names.

---

### **Video Detection**
To perform object detection on a video (e.g., `pedestrian.mp4` in the `videos` folder):

1. Update the video path in `yolo_web.py`:
   ```python
   cap = cv2.VideoCapture("videos/pedestrian.mp4")
   ```
2. Run the script:
   ```bash
   python yolo_webcam/yolo_web.py
   ```

---

### **Webcam Detection**
To detect objects in real-time using your webcam:

1. Update the webcam source in `yolo_web.py`:
   ```python
   cap = cv2.VideoCapture(0)  # Set to 0 for default webcam
   ```
2. Run the script:
   ```bash
   python yolo_webcam/yolo_web.py
   ```

---

## **Folder Structure**
```
object-detection-yolov8/
│
├── images/               # Sample images for testing
│   ├── car.jpeg
│   └── school.jpeg
│
├── videos/               # Sample videos for testing
│   ├── bike.mp4
│   └── pedestrian.mp4
│
├── running_yolo/         # Script for single-image detection
│   └── yolo.py
│
├── yolo_webcam/          # Script for video and webcam detection
│   └── yolo_web.py
│
├── yolov8n.pt            # YOLOv8 model file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (excluded in .gitignore)
```

---

## **Demo**
- **Image Example**: Detect cars and other objects in static images.
- **Video Example**: Process videos and detect moving objects like pedestrians and vehicles.
- **Webcam Example**: Perform real-time object detection through your webcam.

---

## **Requirements**
- **Python 3.11** or higher
- YOLOv8 model weights (`yolov8n.pt`)
- Dependencies listed in `requirements.txt`

---

## **Acknowledgements**
- **YOLOv8**: Ultralytics for creating the powerful YOLOv8 model ([Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)).
- **OpenCV**: For computer vision operations.
- **cvzone**: For drawing bounding boxes and adding text overlays.

---

## **Future Enhancements**
- Add functionality for saving detection outputs as annotated videos/images.
- Fine-tune YOLOv8 for custom datasets.
- Explore deployment as a web application or on embedded systems.

---

Feel free to fork the repository, contribute improvements, or open issues if you encounter problems. 🎉
