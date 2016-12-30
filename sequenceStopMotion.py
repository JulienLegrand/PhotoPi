#!/usr/bin/env python

from time import sleep
import datetime as dt
import os
from shutil import copyfile
import subprocess as sub
import pygame
import os.path
import pygameEngine
import livePreview
import Camera
import sys

# Variables
NB_PHOTOS = 5

def Init():
	#Create folders needed
	if not os.path.isdir("stopmotion-photos") :
		os.makedirs("stopmotion-photos")
	if not os.path.isdir("stopmotion-temp") :
		os.makedirs("stopmotion-temp")
	if not os.path.isdir("stopmotion-composites") :
		os.makedirs("stopmotion-composites")
	Clear()

def TakePictures():
    pygameEngine.Fill(pygameEngine.BLACK_COLOR)
    pygameEngine.DrawCenterMessage("Go for %d pics!" % NB_PHOTOS, True, False)
    pygameEngine.DrawCenterMessage("3", True)
    pygameEngine.DrawCenterMessage("2", True)
    pygameEngine.DrawCenterMessage("1", True)

    photoFile = dt.datetime.now().strftime("%Y%m%d-%Hh%Mm%S")
    i=1
    while(i<=NB_PHOTOS):
        Camera.WaitCamera()
        pygameEngine.DrawCenterMessage("[ Pose " + str(i) + " ]", True)
        photoFilePath = "stopmotion-photos/" + photoFile + "-" + str(i).zfill(2) + ".jpg"
        pygameEngine.Fill(pygameEngine.WHITE_COLOR)
        Camera.TakePhoto(photoFilePath)

        #Don't wait to shrink the picture to reduce global time and don't wasting the time waiting the camera
        photoFilePathDest = "stopmotion-temp/" + photoFile + "-" + str(i).zfill(2) + ".jpg"
        while os.path.exists(photoFilePath) == False: # Wait for creation
            sleep(.1)
        copyfile(photoFilePath, photoFilePathDest)
        p = sub.Popen('mogrify -resize 1920x1080 ' + photoFilePathDest, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)

        i+=1
    pygameEngine.WaitLogo()
    p.wait()
    return photoFile

def Composite(photoFile):
    print "Prepare images"

    i=1
    while(i<=NB_PHOTOS):
        photoFilePathDest = "stopmotion-temp/" + photoFile + "-" + str(i).zfill(2) + ".jpg"

        #Create additionnal images with imagemagick morph
        if(i>1):
            p = sub.Popen("sudo convert stopmotion-temp/" + photoFile + "-" + str(i-1).zfill(2) + ".jpg stopmotion-temp/" + photoFile + "-" + str(i).zfill(2) + ".jpg -delay 100 -morph 10 stopmotion-temp/" + photoFile + "-" + str(i-1).zfill(2) + "-99-%03d.jpg", stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            p.wait()

        #Duplicate the photo for the final video
        j=1
        while(j<=20):
            copyfile(photoFilePathDest, "stopmotion-temp/" + photoFile + "-" + str(i).zfill(2) + "-" + str(j).zfill(2) + ".jpg")
            j+=1

        i+=1

    #Realign numbers
    i=1
    filelist = [ f for f in os.listdir("stopmotion-temp") ]
    filelist.sort()
    for f in filelist:
        os.rename("stopmotion-temp/" + f, "stopmotion-temp/" + photoFile + "-" + str(i).zfill(3) + ".jpg")
        i+=1

    print "Encode video"
    #os.popen don't work for this, don't know why
    p = sub.Popen("sudo mencoder mf://stopmotion-temp/*.jpg -mf w=1920:h=1080:fps=20:type=jpg -nosound -ovc x264 -x264encopts bitrate=2000 -o stopmotion-temp/" + photoFile + ".mp4", stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    p.wait()

    print "Add music"
    #Add music
    p = sub.Popen("sudo avconv -i stopmotion-temp/" + photoFile + ".mp4 -i music.mp3 -c copy -map 0:v -map 1:a -shortest stopmotion-composites/" + photoFile + ".mp4 -y", stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    p.wait()

    print "Play"
    #Play
    pygameEngine.Fill(pygameEngine.BLACK_COLOR)
    os.popen("omxplayer stopmotion-composites/" + photoFile + ".mp4 -o local --vol -4000")

def Clear():
	#Clear temp folder
	filelist = [ f for f in os.listdir("stopmotion-temp") ]
	for f in filelist:
		os.remove("stopmotion-temp/" + f)
	
def Start():
    try:
        print "Stop-Motion Start"
        livePreview.Start()
        Init()
        photoFile = TakePictures()
        Composite(photoFile)

        #Clear()
        print "Stop-Motion End"
    except Exception, e:
        print "ERREUR : Stop-Motion : " + e.message
        pygameEngine.ShowError()