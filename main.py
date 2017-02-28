#!/usr/bin/env python

import pygameEngine
import os
from time import sleep
import sequencePhoto
import sequenceVideo
import sequenceStopMotion
import Camera

# drops other possible connections to the camera on every restart just to be safe
os.system("sudo pkill gvfs")
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

#Init app
app_name = "PhotoPi"
print app_name + " started"
sleep(2)

#Self test
if(Camera.CheckCamera() == -1):
	raise Exception('No camera detected!')

#Start
pygameEngine.init(app_name)

# Boucle principale
print "Waiting events"
try:
	while(1):
		#Default screen between sequences
		pygameEngine.ActionScreen()

		action = pygameEngine.CheckAction()
		if(action == 1):
			sequencePhoto.Start()
			pygameEngine.ClearActionsQueue()
		if(action == 2):
			#sequenceVideo.Start()
			sequenceStopMotion.Start()
			pygameEngine.ClearActionsQueue()
                if(action == 9):
                        break

except:
	raise
finally:
	# Fin
	print "End"
	pygameEngine.Quit()
