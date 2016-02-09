#!/bin/bash

DATE=$(date +%Y-%m-%d_%H%M)

mkdir webcam

sudo mount -t tmpfs tmpfs webcam

fswebcam -r 640x480 --no-banner /home/pi/webcam/$DATE.jpg

sudo umount webcam

rm -r webcam
