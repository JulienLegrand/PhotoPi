#!/usr/bin/env python

import config
import pygame
from time import sleep
import RPi.GPIO as GPIO

# GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(config.GPIO_NUMBER_BUTTON_1, GPIO.IN)
GPIO.setup(config.GPIO_NUMBER_BUTTON_2, GPIO.IN)

# Variables
BLACK_COLOR = pygame.Color(0, 0, 0)
WHITE_COLOR = pygame.Color(255, 255, 255)
BLUE_COLOR = pygame.Color(40, 87, 255)
SCREEN = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.FULLSCREEN)

def init(app_name):
	print "pygame init"
	pygame.init()
	pygame.mouse.set_visible(False)
	pygame.display.set_caption(app_name)
	
def GetScreen():
	return SCREEN

def Fill(color):
	SCREEN.fill(color)
	pygame.display.update()
	
def CheckAction(): #Return -1 (idle) or 1 or 2 (Sequence 1 or 2) or 9 (exit)
    # get one pygame event
    event = pygame.event.poll()

    # handle physical buttons (connected to GPIO)
    if (event.type == pygame.MOUSEBUTTONUP and event.button == 1) or (event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_KP1)) or (GPIO.input(config.GPIO_NUMBER_BUTTON_1)):
    	return 1
    if (event.type == pygame.MOUSEBUTTONUP and event.button == 3) or (event.type == pygame.KEYDOWN and (event.key == pygame.K_2 or event.key == pygame.K_KP2)) or (GPIO.input(config.GPIO_NUMBER_BUTTON_2)):
        return 2

    # handle keyboard keys
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q) :
        return 9

    return -1

def ClearActionsQueue():
	pygame.event.clear() #Clear events in the queue (typically when button is pressed during the sequence)

def DrawCenterMessage(message, big = False, withSleep = True):
	"""displays notification messages onto the SCREEN"""
	FONTsize = 160 if big else 60
		
	SCREEN.fill(BLACK_COLOR)
	TextSurf = pygame.font.SysFont(config.FONT, FONTsize).render(message, True, WHITE_COLOR)
	TextRect = TextSurf.get_rect()
	TextRect.center = ((config.WIDTH / 2), (config.HEIGHT / 2))
	SCREEN.blit(TextSurf, TextRect)
	pygame.display.update()
	if withSleep:
		sleep(1)

def DrawTopMessage(message):
	"""displays notification messages onto the SCREEN"""
	SCREEN.fill(BLACK_COLOR)
	TextSurf = pygame.font.SysFont(config.FONT, 40).render(message, True, WHITE_COLOR)
	TextRect = TextSurf.get_rect()
	TextRect.center = ((config.WIDTH / 2), (80))
	SCREEN.blit(TextSurf, TextRect)
	pygame.display.update()
	
def ActionScreen():
	image = pygame.image.load(config.ACTION_SCREEN_FILE)
	SCREEN.blit(image, (0,0))
	pygame.display.update()
	sleep(.6)

def WaitLogo():
	""" Draw title """
	# image
	SCREEN.fill(BLACK_COLOR)
	image = pygame.image.load(config.WAIT_LOGO_FILE)

	# crop middle square and resize
	imgsize = image.get_rect().size
	image_square = pygame.Rect((imgsize[0] - imgsize[1]) / 2, 0, imgsize[1], imgsize[1]) # left, top, WIDTH, HEIGHT
	image_surface = pygame.transform.scale(image.subsurface(image_square), (config.LOGO_SIZE, config.LOGO_SIZE))
	image_Rect = image_surface.get_rect()
	image_Rect.center = ((config.WIDTH / 2), (config.HEIGHT / 2))
	SCREEN.blit(image_surface, image_Rect)
	pygame.display.update()

def Bip1():
	soundBeep1 = pygame.mixer.Sound(config.BEEP01_SOUND_FILE)
	soundBeep1.play()

def Bip2():
	soundBeep2 = pygame.mixer.Sound(config.BEEP02_SOUND_FILE)
	soundBeep2.play()
	
def ShowError():
	SCREEN.fill(BLUE_COLOR)
	DrawCenterMessage("Erreur", True, True)
	
def Quit():
	pygame.quit()
