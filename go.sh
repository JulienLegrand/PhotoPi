#!/bin/sh

#Wake up screen monitor
sudo chmod 666 /dev/tty1
echo -ne "\033[9;0]" >/dev/tty1

cd "$(/home/pi/PhotoPi "$0")"
DISPLAY=0:0; sudo python main.py