#!/usr/bin/env python

import os
import subprocess as sub
from time import sleep
from shutil import copyfile

#keywords to find camera status in Gphoto2 --summary
#Warning : to avoid encoding problem, i chose words without diacritics
KEYWORDS_IN_USE = "Camera is already in use"
KEYWORDS_NO_CAMERA = "*** Error: No camera found. ***"
KEYWORDS_CAMERA_OK = "Access Capability: Read-Write"

#DEBUG variable is here to avoid using DSLR for testing
DEBUG=False

def CheckCamera():
	if(DEBUG):
		return 1
	#Test Camera status by reading Gphoto2 summary : -1 No camera / 0 in use / 1 ok
	p = sub.Popen('gphoto2 --summary', stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
	summary = str(p.communicate())
	if(summary.find(KEYWORDS_NO_CAMERA) != -1): res = -1
	if(summary.find(KEYWORDS_IN_USE) != -1): res = 0
	if(summary.find(KEYWORDS_CAMERA_OK) != -1): res = 1
	return res

def WaitCamera():
	if(DEBUG):
		return
	while(CheckCamera() == 0):
		sleep(.1)
		if(CheckCamera() == -1) : raise Exception('No camera detected!')
		
def TakePhoto(photoFile):
	if(not DEBUG):
		os.popen("gphoto2 --capture-image-and-download --filename " + photoFile + " --force-overwrite &")
	else:
		sleep(3) #Simulate shoot time
		copyfile("debug.jpg", photoFile)
	
def RecordPreview(liveMovie, previewDuration):
	if(DEBUG):
		return
	os.popen("gphoto2 --capture-movie=" + str(previewDuration) + "s --stdout> " + liveMovie + " &")
		
def RecordMovie(movieFile, previewDuration):
	if(DEBUG):
		return
	os.popen("gphoto2 --capture-movie=" + str(previewDuration) + "s --stdout> " + movieFile + " &")