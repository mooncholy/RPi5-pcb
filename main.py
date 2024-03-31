from ultralytics import YOLO
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, default='./models/best.pt')
    args = parser.parse_args()
    model = YOLO(args.model)
    results = model.predict('tcp://192.168.137.36:8080', stream=True, imgsz=416)
    while True:
        for result in results:
            boxes = result.boxes
            probs = result.probs
