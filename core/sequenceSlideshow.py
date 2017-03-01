#!/usr/bin/env python

import config
from time import sleep
import datetime as dt
import os
import pygame
import os.path
import pygameEngine
import livePreview
import camera
import sys
import RPi.GPIO as GPIO

def ShowPhoto(photoFile):
	screen = pygameEngine.GetScreen()
	image = pygame.image.load(photoFile)
	screen.blit(image, (0,0))
	pygame.display.update()

	i = 0
	while i < 60: # 6 seconds
		# get one pygame event
		event = pygame.event.poll()

		# handle events
		# Button 1 = no action (too many risks to start photobooth)
		# if (event.type == pygame.MOUSEBUTTONUP and event.button == 1) or (event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_KP1)) or (GPIO.input(config.GPIO_NUMBER_BUTTON_1)):
		#	return 0
		if (event.type == pygame.MOUSEBUTTONUP and event.button == 3) or (event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2)) or (GPIO.input(config.GPIO_NUMBER_BUTTON_2)):
			return 1
		if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q) :
			return -1
			
		i += 1
		sleep(.1)

	# No action ends slideshow
	return -1

def CyclePhoto():
	filelist = [ f for f in os.listdir(config.SEQUENCE_PHOTO_COMPOSITES) ]
	filelist.sort()
	for f in reversed(filelist):
		res = ShowPhoto(config.SEQUENCE_PHOTO_COMPOSITES + "/" + f)
		if res == -1 : break

def Start():
    try:
        print "Slideshow Start"
        CyclePhoto()
    except Exception, e:
        print "ERREUR : Slideshow : " + str(sys.exc_info()[0]) + " : " + str(e)
        pygameEngine.ShowError()
