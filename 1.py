from ultralytics import YOLO

model = YOLO('yolov5s.pt')

results = model(source=0 , show=True , conf=0.4, save=True)