# PhotoPi
A Raspberry Pi Photobooth made with Python

This is another python/Raspberry Pi photobooth :)

My hardware :
- Raspberry pi 2 or 3 (not tested on another version, but everything should be fine)
- Canon Rebel T2i Camera (550d in Europe), with AC adapter (or any other DSLR recognize by Gphoto2)
- an old 17' vga monitor

Software :
- Raspbian Jessie 8.0
- Python 2.7.9 (Raspbian default)
- Gphoto2 2.5.10 to 2.5.11.1
- OmxPlayer
- ImageMagick 6.8.9-9 Q16 arm

How to use :
- just launch ./go.sh (with local or distant terminal)
- use key 1, left mouse button or GPIO switch (default pin #36) for action 1
- use key 2, right mouse button or GPIO switch (default pin #32) for action 2
- type Escape or Q to quit

Credits :
Made with code from : (non exhaustive)

https://hackaday.io/project/6380-pibooth
https://github.com/contractorwolf/RaspberryPiPhotobooth/blob/master/photobooth.py
https://github.com/ErikBorra/lightbooth/blob/master/lightbooth.py

Made with sounds from :
https://www.soundjay.com
