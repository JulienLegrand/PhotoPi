#!/usr/bin/env python

import os
import subprocess as sub
from time import sleep

#keywords to find camera status in Gphoto2 --summary
#Warning : to avoid encoding problem, i chose words without diacritics
keywordsInUse = "*** Erreur ***"
keywordsNoCamera = "*** Erreur : aucun appareil trouv"
keywordsCameraOk = " sur l'appareil"

def CheckCamera():
	res = -1
	#Test Camera status by reading Gphoto2 summary : -1 No camera / 0 in use / 1 ok
	p = sub.Popen('gphoto2 --summary',stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
	summary = str(p.communicate())
	if(summary.find(keywordsNoCamera) != -1): res = -1
	if(summary.find(keywordsInUse) != -1): res = 0
	if(summary.find(keywordsCameraOk) != -1): res = 1
	return res

def WaitCamera():
	while(CheckCamera() == 0):
		sleep(.1)
		if(CheckCamera() == -1) : raise Exception('No camera detected!')
		
def TakePhoto(photoFile):
	os.popen("gphoto2 --capture-image-and-download --filename " + photoFile + " --force-overwrite &")
	
def RecordMovie(liveMovie, previewDuration):
	os.popen("gphoto2 --capture-movie=" + str(previewDuration) + "s --stdout> " + liveMovie + " &")