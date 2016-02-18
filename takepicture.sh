#!/bin/bash

COUNTER=0
DATE=$(date +%Y-%m-%d_%H%M)

while [ $COUNTER -le 5 ]
do
	mkdir webcam
	sudo mount -t tmpfs tmpfs webcam
	fswebcam -r 640x480 /home/pi/SecureCameraServer/webcam/toSend.jpg
	#call sript to send 
	python SSLtestWebcam.py
	sudo umount webcam
	rm -r webcam
	sleep 60
done
