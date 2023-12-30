#!/usr/bin/env python

import core.config as config
from time import sleep
import datetime as dt
import os
from shutil import copyfile
import subprocess as sub
import pygame
import os.path
import core.pygameEngine as pygameEngine
import core.livePreview as livePreview
import core.camera as camera
import sys

def Init():
	#Create folders needed
	if not os.path.isdir(config.SEQUENCE_STOPMOTION_CAPTURES) :
		os.makedirs(config.SEQUENCE_STOPMOTION_CAPTURES)
	if not os.path.isdir(config.SEQUENCE_STOPMOTION_TEMP) :
		os.makedirs(config.SEQUENCE_STOPMOTION_TEMP)
	if not os.path.isdir(config.SEQUENCE_STOPMOTION_COMPOSITES) :
		os.makedirs(config.SEQUENCE_STOPMOTION_COMPOSITES)
	Clear()

def TakePictures():
    pygameEngine.Fill(pygameEngine.BLACK_COLOR)
    pygameEngine.DrawCenterMessage("Go for %d pics!" % config.SEQUENCE_STOPMOTION_NB_PHOTOS, True, False)
    pygameEngine.DrawCenterMessage("3", True)
    pygameEngine.DrawCenterMessage("2", True)
    pygameEngine.DrawCenterMessage("1", True)

    photoFile = dt.datetime.now().strftime("%Y%m%d-%Hh%Mm%S")
    i=1
    while(i <= config.SEQUENCE_STOPMOTION_NB_PHOTOS):
        camera.WaitCamera()
        pygameEngine.SoundBip2()
        pygameEngine.DrawCenterMessage("[ Pose " + str(i) + " ]", True)
        photoFilePath = config.SEQUENCE_STOPMOTION_CAPTURES + "/" + photoFile + "-" + str(i).zfill(2) + ".jpg"
        pygameEngine.Fill(pygameEngine.WHITE_COLOR)
        camera.TakePhoto(photoFilePath)

        #Don't wait to shrink the picture to reduce global time and don't wasting the time waiting the camera
        photoFilePathDest = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i).zfill(2) + ".jpg"
        while os.path.exists(photoFilePath) == False: # Wait for creation
            sleep(.1)
        copyfile(photoFilePath, photoFilePathDest)
        p = sub.Popen(config.CMD_SHRINK.format(filename = photoFilePathDest), stdout=sub.PIPE, stderr=sub.PIPE, shell=True)

        i+=1
    pygameEngine.WaitLogo()
    p.wait()
    return photoFile

def Composite(photoFile):
    print("Prepare images")

    #Play sound
    waitSound = pygame.mixer.Sound(config.WAIT_SOUND_FILE)
    waitSound.play()

    i=1
    while(i <= config.SEQUENCE_STOPMOTION_NB_PHOTOS):
        photoFilePathDest = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i).zfill(2) + ".jpg"

        #Create additionnal images with imagemagick morph
        if(i>1):
            p = sub.Popen(config.CMD_ADD_MORPH_FRAMES.format(filename1 = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i-1).zfill(2) + ".jpg", filename2 = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i).zfill(2) + ".jpg", filenamePattern = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i-1).zfill(2) + "-99-%03d.jpg"), stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            p.wait()

        #Duplicate the photo for the final video
        j=1
        while(j<=20):
            copyfile(photoFilePathDest, config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i).zfill(2) + "-" + str(j).zfill(2) + ".jpg")
            j+=1

        i+=1

    #Realign numbers
    i=1
    filelist = [ f for f in os.listdir(config.SEQUENCE_STOPMOTION_TEMP) ]
    filelist.sort()
    for f in filelist:
        os.rename(config.SEQUENCE_STOPMOTION_TEMP + "/" + f, config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + "-" + str(i).zfill(3) + ".jpg")
        i+=1

    print("Encode video")
    #os.popen don't work for this, don't know why
    p = sub.Popen(config.CMD_ENCODE.format(image_folder = config.SEQUENCE_STOPMOTION_TEMP, filename = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + ".mp4"), stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    p.wait()

    print("Add music")
    #Add music
    p = sub.Popen(config.CMD_ADD_MUSIC.format(filename_in = config.SEQUENCE_STOPMOTION_TEMP + "/" + photoFile + ".mp4", filename_music = config.MUSIC_FILE, filename_out = config.SEQUENCE_STOPMOTION_COMPOSITES + "/" + photoFile + ".mp4"), stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
    p.wait()

    print("Play")
    #Play
    pygameEngine.Fill(pygameEngine.BLACK_COLOR)
    os.popen(config.CMD_STOPMOTION_PLAY.format(filename = config.SEQUENCE_STOPMOTION_COMPOSITES + "/" + photoFile + ".mp4"))

def Clear():
	#Clear temp folder
	filelist = [ f for f in os.listdir(config.SEQUENCE_STOPMOTION_TEMP) ]
	for f in filelist:
		os.remove(config.SEQUENCE_STOPMOTION_TEMP + "/" + f)

def Start():
    try:
        print("Stop-Motion Start")
        livePreview.Start()
        Init()
        photoFile = TakePictures()
        Composite(photoFile)

        #Clear()
        print("Stop-Motion End")
    except Exception as e:
        print("ERREUR : Stop-Motion : " + str(sys.exc_info()[0]) + " : " + str(e))
        pygameEngine.ShowError()
