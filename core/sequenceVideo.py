#!/usr/bin/env python

import config
from time import sleep
import datetime as dt
import os
import os.path
import pygameEngine
import livePreview
import camera
import sys

def RecordVideo():
	print "Record video"
	pygameEngine.DrawCenterMessage("3", True)
	pygameEngine.DrawCenterMessage("2", True)
	pygameEngine.DrawCenterMessage("1", True)
	pygameEngine.Fill(pygameEngine.WHITE_COLOR)
	
	movieFile = config.SEQUENCE_VIDEO_CAPTURES + "/" + dt.datetime.now().strftime("%Y%m%d-%Hh%Mm%S") + ".mpeg"
	if not os.path.isdir(config.SEQUENCE_VIDEO_CAPTURES) :
		os.makedirs(config.SEQUENCE_VIDEO_CAPTURES)
		
	camera.RecordMovie(movieFile, 20)
	PlayVideo(movieFile)

def PlayVideo(movieFile):
	print "Play video"
	while not os.path.exists(movieFile):
		sleep(.1)
	os.popen(config.CMD_VIDEO_PLAY.format(filename = movieFile))

def Start():
	try:
		livePreview.Start()
		RecordVideo()
	except:
		print "ERREUR : Video : " + str(sys.exc_info()[0]) + " : " + str(e)
		pygameEngine.ShowError()
