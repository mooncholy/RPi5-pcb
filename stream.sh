#!/bin/bash
libcamera-vid -t 0 --inline --width 1920 --height 1080 --framerate 15 -o - | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264
