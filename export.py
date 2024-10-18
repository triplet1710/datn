from ultralytics import YOLO

model = YOLO("best.pt")
model.export(format="engine")  # creates 'yolov8n.engine'