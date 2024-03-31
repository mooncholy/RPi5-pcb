from ultralytics import YOLO
from utils import SimpleFPS, draw_fps, draw_annotation
import argparse
import cv2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Path to the YOLO model file")
    parser.add_argument('--debug', action=argparse.BooleanOptionalAction)
    parser.add_argument('--print_fps', action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    
    # Load the YOLO model
    model = YOLO(args.model)
    src = 'tcp://127.0.0.1:8888'
    cap = cv2.VideoCapture(src)

    fps_util = SimpleFPS()
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break
        fps, is_fps_updated = fps_util.get_fps()

        results = model.predict(frame, stream=True)

        if args.debug is not None and args.debug:
            debug_img = draw_annotation(frame, model.get_label_names(), results)
            draw_fps(debug_img, fps)
            cv2.imshow('frame', debug_img)

            # press 'Q' if you want to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if args.print_fps and is_fps_updated:
            print(f'{fps} fps')  # printing every 1 sec atm, toto

    # clean up
    cap.release()
    cv2.destroyAllWindows()
