#sequencePhoto
import pygame
import os
from time import sleep
import sequencePhoto

# Variables
width = 1280
height = 1024

# Start
# drops other possible connections to the camera on every restart just to be safe
os.system("sudo pkill gvfs")
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
app_name = "PhotoPi"
print app_name + " started"
sleep(2)

# Pygame init
print "pygame init"
pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption(app_name)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)#FULLSCREEN

# Boucle principale
print "Waiting events"
while(1):
	#Clear screen between sequences
	screen.fill(black)
	pygame.display.update()

	# get all events
	ev = pygame.event.get()

	# proceed events
	for event in ev:

		# handle MOUSEBUTTONUP
		if event.type == pygame.MOUSEBUTTONUP:
			if(event.button==1):
				#import sequencePhoto
				sequencePhoto.Start()
			if(event.button==3):
				print "Right click" #TODO : sequenceVideo

# Fin
print "End"
pygame.quit()