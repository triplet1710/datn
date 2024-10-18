import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO model optimized with TensorRT
model = YOLO("yolov8s.pt")  # TensorRT-optimized model (replace with actual .engine file)

# Read input image (replace with video capture if needed)
frame = cv2.imread("20230711103358423_white-prawns_good_jpeg_jpg.rf.00b3b0648f2a5b350d918ce26826ab0d.jpg")  # Replace with your input image file

# Run inference
results = model(frame)

cnt = 0
if results[0].masks is not None:
    # Get mask data from results and process
    masks = (results[0].masks.data.numpy() * 255).astype('uint8')  # Convert masks to uint8 (0-255)
    for i, mask in enumerate(masks):
        x1, y1, x2, y2, c, id = results[0].boxes.data[i].numpy()
        if c < 0.85:
            continue
        original_height, original_width = frame.shape[:2]
        mask_resized = cv2.resize(mask, (original_width, original_height), interpolation=cv2.INTER_NEAREST)

        # Generate a fixed color for shrimp (green color as shown in your example)
        color = (0, 255, 0)  # BGR format: (Blue, Green, Red)

        # Create a colored mask and apply it on the image
        colored_mask = np.zeros_like(frame, dtype=np.uint8)
        colored_mask[mask_resized > 0] = color

        # Overlay the colored mask on the original image
        frame = cv2.addWeighted(frame, 1, colored_mask, 0.5, 0)
        
        # Get bounding box and confidence
        confidence = c * 100  # Convert to percentage

        # Draw the label with confidence on the segmented object
        label = f'shrimp {confidence:.1f}%'
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    # Display total number of objects (shrimp) detected (optional)
    cv2.putText(frame, f'So luong tom: {cnt}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Save the output frame with colored segmentation masks
cv2.imwrite("output_segmented_with_labels.jpg", frame)

# Print processing time for debugging (optional)
print("Processing completed.")
