from ultralytics import YOLO
import cv2

model= YOLO('yolov8n.pt')
results=model('images/car.jpeg', show=True)
cv2.waitKey(0)