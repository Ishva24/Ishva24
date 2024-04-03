import torch
from PIL import Image
from PIL import ImageDraw


# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5l-seg.pt')  # Replace 'yolov5l-seg.pt' with the path to your custom YOLOv5 model

def detect_objects(image):
    results = model(image)
    detections = results.xyxy[0]  # Extract bounding boxes and class labels
    return detections

# Read image using PIL
image_path = 'C:/Users/rajaprasanna/Documents/neuralintents-master/neuralintents-master/neuralintents/examples/2.png'  # Replace with the path to your input image
image = Image.open(image_path)

# Perform object detection
detections = detect_objects(image)

# Process and display detected objects (example code)
for det in detections:
    bbox = det[:4]
    label = det[5]
    confidence = det[4]

    # Draw bounding box on the image
    draw = ImageDraw.Draw(image)
    draw.rectangle(bbox, outline='red', width=3)
    draw.text((bbox[0], bbox[1]), f'{label}: {confidence:.2f}', fill='red')

# Display the image with detected objects
image.show()
