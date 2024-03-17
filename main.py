from ultralytics import YOLO
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Path to the YOLO model file")
    args = parser.parse_args()
    
    # Load the YOLO model
    model = YOLO(args.model)
    results = model('tcp://127.0.0.1:8888', stream=True)
    
    while True:
        for result in results:
            boxes = result.boxes
            probs = result.probs