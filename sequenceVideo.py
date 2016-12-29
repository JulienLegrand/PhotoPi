#!/usr/bin/env python

from time import sleep
import datetime as dt
import os
import os.path
import pygameEngine
import livePreview
import Camera

def RecordVideo():
	pygameEngine.DrawCenterMessage("3", True)
	pygameEngine.DrawCenterMessage("2", True)
	pygameEngine.DrawCenterMessage("1", True)
	
	movieFile = "videos/" + dt.datetime.now().strftime("%Y%m%d-%Hh%Mm%S") + ".mpeg"
	if not os.path.isdir("videos") :
		os.makedirs("videos")
		
	Camera.RecordMovie(movieFile, 20)

def Start():
	try:
		livePreview.Start()
		RecordVideo()
	except:
		print "ERREUR : Stop-Motion : " + sys.stderr
		pygameEngine.ShowError()