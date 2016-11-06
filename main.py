#!/usr/bin/env python

import pygameEngine
import os
from time import sleep
import sequencePhoto

# drops other possible connections to the camera on every restart just to be safe
os.system("sudo pkill gvfs")
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

#Init app
app_name = "PhotoPi"
print app_name + " started"
sleep(2)

#Start
pygameEngine.init(app_name)

# Boucle principale
print "Waiting events"
while(1):
	#Clear screen between sequences
	pygameEngine.Fill(pygameEngine.black)

	action = pygameEngine.CheckAction()
	if(action==1):
		#import sequencePhoto
		sequencePhoto.Start()
		pygameEngine.ClearActionsQueue()
	if(action==2):
		print "Right click" #TODO : sequenceVideo

# Fin
print "End"
pygameEngine.quit()