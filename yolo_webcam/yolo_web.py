from ultralytics import YOLO
import cv2
import cvzone
import math

#cap = cv2.VideoCapture(0)#for webc
#cap.set(3, 640)
#cap.set(4, 480)
cap = cv2.VideoCapture("videos/pedestrian.mp4") #for video

model = YOLO('yolov8n.pt')

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "trucK", "boat","traffic light","fire hydrant", "stop sign", "parking meter",
              "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant","bear","zebra","giraffe","backpack","umbrella",
              "handbag","title", "suitcase", "frsbee", "skis", "snowboard", "sports ball", "kite", "baseball bat","baseball glove", "skateboard","surboard","tennis racket",
              "bottle","wine glass","cup","fork","knife","spoon","bowl", "banana","apple","sandwich","orange","broccoli","carrot",
              "hot dog", "pizza","donut", "calke", "chair", "sofa", "pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse","remote",
              "keyboard", "cell phone","microwave", "oven", "toaster", "sink", "refrigator", "book", "clock", "vase","scissors", "teddy bear", "hair drier", "tootbrush"
              ]  # Ensure this matches your model's classes

while True:
    success, img = cap.read()
    if not success:
        break

    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            if box.xyxy.size(0) == 0:  # Skip if no bounding boxes are detected
                continue
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            cvzone.putTextRect(img, f'{conf}', (max(0, x1), max(35, y1)))

            # Class name
            if box.cls.size(0) > 0:  # Ensure there is a class index
                cls = int(box.cls[0])
                if cls < len(classNames):  # Ensure class index is within bounds
                    cvzone.putTextRect(img, f"{classNames[cls]} {conf}", (max(0, x1), max(35, y1)),thickness=1)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
