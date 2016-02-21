#!/bin/bash

i="0"
DATE=$(date +%Y-%m-%d_%H%M)

while [ $i -lt 4 ]
do
mkdir -p /home/pi/SecureCameraServer/webcam
sudo mount -t tmpfs tmpfs /home/pi/SecureCameraServer/webcam
raspistill -o /home/pi/SecureCameraServer/webcam/toSend.jpg
#call sript to send 
python SSLtestWebcam.py
sleep 10
sudo umount /home/pi/SecureCameraServer/webcam
rm -r /home/pi/SecureCameraServer/webcam
echo "script complete"
done
