from ultralytics import YOLO
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Path to the YOLO model file")
    parser.add_argument("--image", required=True, help="Path to the input image file")
    args = parser.parse_args()

    # Load the YOLO model
    model = YOLO(args.model)

    # Detect objects in the input image
    results = model(args.image, save=True, show=True, show_boxes=True)

    # Print the detected objects
    print(results)
