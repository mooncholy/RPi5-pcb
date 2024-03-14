# RPi5-pcb
## Prerequisite
1. Setting raspberry pi camera using libcam-hello
    ```
    sudo apt update && sudo apt full upgrade    // check for system updates
    sudo apt install -y python3-picamera2       // installing picamera2 for the 1st time
    rpicam-hello --list-camera                  // checking connected cams
    rpicam-hello --qt -preview                  // testing camera preview
    ```
2. Installing MiniConda on Raspberry pi 
    ```
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    ~/miniconda3/bin/conda init bash
    //optional clean up
    rm -rf ~/miniconda3/miniconda.sh
    ```
3. Installing CMake in raspberrypi is needed for tflite format
    `sudo apt-get install cmake`  
## Create envirnoment
```
conda create -n pcb_defect python=3.10.12
conda activate pcb_defect
pip install ultralytics
pip install tensorflow==2.13.1
pip install onnx==1.15.0 onnxruntime==1.16.3 onnxsim==0.4.33
pip install -U --force-reinstall flatbuffers==23.5.26
```

## Export yolov8 model to tflite and onnx format
```
python export_models.py
python export_models.py --format onnx
```

## Run
set utf8 format for python if you are getting strange error with latin1 encoding
```
export PYTHONUTF8=1 
```
### Run models
1. Detecting from local images
    ```
    python detect.py --model=./models/best.onnx --image=./test/<filename.jpg>
    ```
2. Running pt models
    ```
    python main.py --debug
    python main.py --print_fps
    ```
3. Running exported models
    ```
    python main.py --model=./models/best.onnx  -debug
    python main.py --model=./models/best_saved_model/best_integer_quant.tflite --debug
    ```