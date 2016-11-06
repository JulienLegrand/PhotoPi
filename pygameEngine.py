#!/usr/bin/env python

import pygame
from time import sleep

# Variables
width = 1280
height = 1024
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)#FULLSCREEN
waitLogoImage = "wait.gif"
logo_size = 500
font = "DejaVuSerif-Bold"

def init(app_name):
	print "pygame init"
	pygame.init()
	pygame.mouse.set_visible(False)
	pygame.display.set_caption(app_name)
	
def GetScreen():
	return screen

def Fill(color):
	screen.fill(color)
	pygame.display.update()
	
def CheckAction(): #Return -1 or 1 or 2 (Sequence 1 or 2)
	# get one event
	event = pygame.event.poll()
	res = -1
	
	# handle MOUSEBUTTONUP
	if event.type == pygame.MOUSEBUTTONUP:
		if(event.button==1):
			res = 1
		if(event.button==3):
			res = 2
	return res

def ClearActionsQueue():
	pygame.event.clear() #Clear events in the queue (typically when button is pressed during the sequence)

def DrawCenterMessage(message,big=False,withSleep=True):
	"""displays notification messages onto the screen"""
	if big:
		fontsize = 160
	else:
		fontsize = 60
	screen.fill(black)
	TextSurf = pygame.font.SysFont(font,fontsize).render(message, True, white)
	TextRect = TextSurf.get_rect()
	TextRect.center = ((width/2),(height/2))
	screen.blit(TextSurf, TextRect)
	pygame.display.update()
	if withSleep:
		sleep(1)
    
def DrawTopMessage(message):
	"""displays notification messages onto the screen"""
	screen.fill(black)
	TextSurf = pygame.font.SysFont(font,40).render(message, True, white)
	TextRect = TextSurf.get_rect()
	TextRect.center = ((width/2),(80))
	screen.blit(TextSurf, TextRect)
	pygame.display.update()
	
def WaitLogo():
	""" Draw title """
	# image
	screen.fill(black)
	image = pygame.image.load(waitLogoImage)

	# crop middle square and resize
	imgsize = image.get_rect().size
	image_square = pygame.Rect((imgsize[0]-imgsize[1])/2, 0, imgsize[1], imgsize[1]) # left, top, width, height
	image_surface = pygame.transform.scale(image.subsurface(image_square),(logo_size,logo_size))
	image_Rect = image_surface.get_rect()
	image_Rect.center = ((width/2),(height/2))
	screen.blit(image_surface, image_Rect)
	pygame.display.update()
	
def Quit():
	pygame.quit()