import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import time

# Load YOLO model optimized with TensorRT
model = YOLO("yolov8s.pt")  # TensorRT-optimized model (replace with actual .engine file)
names = model.model.names

# Open video capture
frame = cv2.imread("1658649633546_jpg.rf.3383d639e6afd74cff0e57e82058d7a6.jpg")  # Replace with your input video file

results = model(frame)

cnt = 0
if results[0].masks is not None:
    masks = (results[0].masks.data.numpy() * 255).astype('uint8')
    for i, mask in enumerate(masks):
        original_height, original_width = frame.shape[:2]
        mask_resized = cv2.resize(mask, (original_width, original_height), interpolation=cv2.INTER_NEAREST)

        x1, y1, x2, y2, c, id = results[0].boxes.data[i].numpy()

             
        M = cv2.moments(mask_resized)
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
        cv2.circle(frame, (center_x, center_y), 4, (255, 0, 0), -1)
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        # cv2.putText(frame, str(area), (int(x1), int(y1)), 1, 1, (0, 0, 255)
        cv2.circle(mask_resized, (center_x, center_y), 4, (0, 0, 255), -1)
        cv2.imwrite(str(i)+".jpg",mask)

       
    cv2.putText(frame, f'So luong tom: {cnt}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

   
cv2.imwrite("out.jpg",frame)

    # Print processing time for debugging


