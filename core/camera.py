#!/usr/bin/env python

import config
import os
import subprocess as sub
from time import sleep
from shutil import copyfile

def CheckCamera():
	if(config.DEBUG):
		return 1
	#Test Camera status by reading Gphoto2 summary : -1 No camera / 0 in use / 1 ok
	p = sub.Popen('gphoto2 --summary', stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
	summary = str(p.communicate())
	if(summary.find(config.KEYWORDS_NO_CAMERA) != -1): res = -1
	if(summary.find(config.KEYWORDS_IN_USE) != -1): res = 0
	if(summary.find(config.KEYWORDS_CAMERA_OK) != -1): res = 1
	return res

def WaitCamera():
	if(config.DEBUG):
		return
	while(CheckCamera() == 0):
		sleep(.1)
		if(CheckCamera() == -1) : raise Exception('No camera detected!')
		
def TakePhoto(photoFile):
	if(not config.DEBUG):
		os.popen("gphoto2 --capture-image-and-download --filename " + photoFile + " --force-overwrite &")
	else:
		sleep(3) #Simulate shoot time
		copyfile(config.DEBUG_FILE, photoFile)
	
def RecordPreview(liveMovie, previewDuration):
	if(config.DEBUG):
		return
	os.popen("gphoto2 --capture-movie=" + str(previewDuration) + "s --stdout> " + liveMovie + " &")
		
def RecordMovie(movieFile, previewDuration):
	if(config.DEBUG):
		return
	os.popen("gphoto2 --capture-movie=" + str(previewDuration) + "s --stdout> " + movieFile)
