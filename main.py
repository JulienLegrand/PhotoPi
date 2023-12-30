#!/usr/bin/env python

import core
from core import camera
from core import sequencePhoto
from core import sequenceVideo
from core import sequenceStopMotion
from core import sequenceSlideshow
from time import sleep
from core import pygameEngine
import os
import datetime as dt

# Variables
LAST_WALLPAPER_DATE = dt.datetime.now()
LAST_WALLPAPER_NUMBER = 1

# drops other possible connections to the camera on every restart just to be safe
os.system("sudo pkill gvfs")
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

#Init app
app_name = "PhotoPi"
print(app_name + " started")
sleep(2)

#Self test
if(camera.CheckCamera() == -1):
	raise Exception('No camera detected!')

#Start
pygameEngine.init(app_name)

# Boucle principale
print("Waiting events")
try:
	#Default screen between sequences
	pygameEngine.ActionScreen(LAST_WALLPAPER_NUMBER)
	while True:

		action = pygameEngine.CheckAction()
		if(action == 1):
			pygameEngine.SoundBip1()
			sequencePhoto.Start()
			#Default screen between sequences
			pygameEngine.ActionScreen(LAST_WALLPAPER_NUMBER)
			pygameEngine.ClearActionsQueue()
		if(action == 2):
			pygameEngine.SoundBip1()
			#sequenceVideo.Start()
			#sequenceStopMotion.Start()
			sequenceSlideshow.Start()
			#Default screen between sequences
			pygameEngine.ActionScreen(LAST_WALLPAPER_NUMBER)
			pygameEngine.ClearActionsQueue()
		if(action == 9):
			break
		if(dt.datetime.now() > LAST_WALLPAPER_DATE + dt.timedelta(minutes=1)):
			LAST_WALLPAPER_DATE = dt.datetime.now()
			LAST_WALLPAPER_NUMBER = LAST_WALLPAPER_NUMBER + 1
			if(LAST_WALLPAPER_NUMBER > 4) : LAST_WALLPAPER_NUMBER = 1
			pygameEngine.ActionScreen(LAST_WALLPAPER_NUMBER)
			print("########################## change")

except:
	raise
finally:
	# Fin
	print("End")
	pygameEngine.Quit()
