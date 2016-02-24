#!/bin/bash

i="0"
DATE=$(date +%Y-%m-%d_%H%M)

#while [ $i -lt 1 ]
#do
#mount a folder into RAM to store the picture
mkdir -p /home/pi/SecureCameraServer/webcam
sudo mount -t tmpfs tmpfs /home/pi/SecureCameraServer/webcam

#take the picture
raspistill -vf -o /home/pi/SecureCameraServer/webcam/toSend.jpg

#call sript to send 
/usr/bin/python /home/pi/SecureCameraServer/SSLtestWebcam.py

#remove the picture from RAM
sudo umount /home/pi/SecureCameraServer/webcam
rm -r /home/pi/SecureCameraServer/webcam

echo "script complete"
#sleep 10
#done
