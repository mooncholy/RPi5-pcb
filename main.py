from ultralytics import YOLO
import argparse
import math, serial, time

temp_arr = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, default='./models/best.pt')
    args = parser.parse_args()
    classNames = ['mouse_bite', 'spur', 'missing_hole', 'short', 'open_circuit', 'spurious_copper']
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    model = YOLO(args.model)
    results = model.predict('tcp://localhost:8080', stream=True, imgsz=416)
    while True:
        for result in results:
            boxes = result.boxes
            # probs = result.probs
            for box in boxes:
                probs = math.ceil((box.conf[0]*100))/100
                print(f"Class = {int(box.cls[0])}, Confidence = {probs}")
                # class name
                cls = int(box.cls[0])
                cls = str(cls) + "\n"
                if len(temp_arr) < 1:
                    temp_arr.append(cls)
                    #byte_index = bytes(temp_arr[-1])
                    #tx = byte_index + b'\n'
                    #print(f"tx = {tx}")
                    x = str.encode(temp_arr[-1])
                    print(x)
                    ser.write(x)
                    temp_arr = []
                elif cls != temp_arr[-1]:
                    temp_arr.append(cls)
                    #bytes_index = bytes(temp_arr[-1])
                    #tx = byte_index + b'\n'
                    #print(f"tx = {tx}")
                    x = str.encode(temp_arr[-1])
                    print(x)
                    ser.write(x)
                    temp_arr = []
