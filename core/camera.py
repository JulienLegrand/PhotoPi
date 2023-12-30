#!/usr/bin/env python

import core.config as config
import os
import subprocess as sub
from time import sleep
from shutil import copyfile

def CheckCamera():
	if(config.DEBUG):
		return 1
	#Test Camera status by reading Gphoto2 summary : -1 No camera / 0 in use / 1 ok
	p = sub.Popen(config.CMD_CHECK, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
	summary = str(p.communicate())
	if(summary.find(config.KEYWORDS_NO_CAMERA) != -1): return -1
	if(summary.find(config.KEYWORDS_IN_USE) != -1): return 0
	if(summary.find(config.KEYWORDS_CAMERA_OK) != -1): return 1

def WaitCamera():
	if(config.DEBUG):
		return
	while(CheckCamera() == 0):
		sleep(.1)
		if(CheckCamera() == -1) : raise Exception('No camera detected!')

def TakePhoto(photoFile):
	if(not config.DEBUG):
		os.popen(config.CMD_PHOTO.format(filename = photoFile))
	else:
		sleep(3) #Simulate shoot time
		copyfile(config.DEBUG_FILE, photoFile)

def RecordPreview(liveMovie, previewDuration):
	if(config.DEBUG):
		return
	os.popen(config.CMD_MOVIE.format(filename = liveMovie, duration = str(previewDuration)) + " &")

def RecordMovie(movieFile, previewDuration):
	if(config.DEBUG):
		return
	os.popen(config.CMD_MOVIE.format(filename = movieFile, duration = str(previewDuration)))
