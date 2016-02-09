#!/bin/bash

DATE=$(date +%Y-%m-%d_%H%M)

mkdir webcam

sudo mount -t tmpfs tmpfs webcam

fswebcam -r 640x480 --no-banner /home/pi/SecureCameraServer/webcam/toSend.jpg
#call sript to send 
python SSLtestWebcam.py

sudo umount webcam

rm -r webcam
