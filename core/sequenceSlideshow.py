#!/usr/bin/env python

import core.config as config
from time import sleep
import datetime as dt
import os
import pygame
import os.path
import core.pygameEngine as pygameEngine
import core.camera as camera
import sys
import RPi.GPIO as GPIO

def ShowPhoto(photoFile):
	screen = pygameEngine.GetScreen()
	image = pygame.image.load(photoFile).convert()
	image = pygame.transform.scale(image, (config.WIDTH,config.HEIGHT))
	screen.blit(image, (0,0))
	pygame.display.update()
	sleep(1)
	pygameEngine.ShowNavButtons()

	i = 0
	while True:
		# get one pygame event
		event = pygame.event.poll()

		# handle events
		# Button 1 = Quit
		if (event.type == pygame.MOUSEBUTTONUP and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or GPIO.input(config.GPIO_NUMBER_BUTTON_1):
			return -1
		# Button 2 = Cycle old photos
		if (event.type == pygame.MOUSEBUTTONUP and event.button == 3) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or GPIO.input(config.GPIO_NUMBER_BUTTON_2):
			return 1
		# Button Esc or Q = Quit keys
		if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q) :
			return -1

def CyclePhoto():
	filelist = [ f for f in os.listdir(config.SEQUENCE_PHOTO_COMPOSITES) ]
	filelist.sort()
	filelist = [ f for f in filelist if not ".gitignore" in f]
	for f in reversed(filelist):
		res = ShowPhoto(config.SEQUENCE_PHOTO_COMPOSITES + "/" + f)
		pygameEngine.SoundBip3()
		if res == -1 : break

def Start():
    try:
        print("Slideshow Start")
        CyclePhoto()
    except Exception as e:
        print("ERREUR : Slideshow : " + str(sys.exc_info()[0]) + " : " + str(e))
        pygameEngine.ShowError()
