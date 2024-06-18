#!/bin/bash

# enter venv and project dir
current_dir=$(pwd)

if [[ "$current_dir" != "/home/pi/RPi5-pcb" ]]; then
  # Change directory to "RPi5-pcb"
  cd RPi5-pcb || {
    echo "Directory 'RPi5-pcb' not found." >&2
    exit 1
  }

  # Print a message indicating the directory change
  echo "Changed directory to RPi5-pcb"
else
  echo "RPi5-pcb is the current directory"
fi

# start camera stream
nohup rpicam-vid --nopreview --width 640 --height 640  --framerate 25 --codec mjpeg  -t 0 --inline --listen -o tcp://0.0.0.0:8080 &

# receive and view stream using cv2
nohup python camera.py &

# run detection on stream
python main.py --model=./models/best.onnx &
