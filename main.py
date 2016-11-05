#!/usr/bin/env python

from time import sleep
import datetime as dt
import os
import pygame
import os.path
import subprocess as sub

# Variables
liveMovie = "fifo.mjpg"
previewDuration = 10 #secondes
width = 1280
height = 1024
font = "DejaVuSerif-Bold"
waitLogoImage = "wait.gif"
logo_size = 500

# Functions
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
	#logo = pygame.transform.scale(pygame.image.load("anomaly_transparent_white.png"),(logosize[0],logosize[1]))
	# image
	screen.fill(black)
	image = pygame.image.load(waitLogoImage)

	# crop middle square and resize
	imgsize = image.get_rect().size
	image_square = pygame.Rect((imgsize[0]-imgsize[1])/2, 0, imgsize[1], imgsize[1]) # left, top, width, height
	image_surface = pygame.transform.scale(image.subsurface(image_square),(logo_size,logo_size))
	image_Rect = image_surface.get_rect()
	image_Rect.center = ((width/2),(height/2))
	#screen.blit(image_surface,(width-logo_size-20,height-logo_size-20))
	#screen.blit(image_surface, ((0.5 * width) - (0.5 *width-logo_size), (0.5 * height) - (0.5 *height-logo_size)))
	screen.blit(image_surface, image_Rect)
	pygame.display.update()
	
def LivePreview():
	# Start recording live preview
	DrawCenterMessage("Prepare for fun",True)
	print "Start recording live preview"
	if os.path.exists(liveMovie):
		os.remove(liveMovie)
	os.mkfifo(liveMovie)
	os.popen("gphoto2 --capture-movie=" + str(previewDuration) + "s --stdout> " + liveMovie + " &")

	# Playing live preview
	DrawCenterMessage("") #Clean screen before preview
	print "Playing live preview"
	os.popen("omxplayer " + liveMovie + " --live")
	
	#Deleting live preview
	os.remove(liveMovie)
	
def TakePictures():
	#Attribute a name with current time for all photos and composite
	photoFile = dt.datetime.now().strftime("%Y%m%d-%Hh%Mm%S")
	pic1 = TakeOnePicture("Smile :)", photoFile + "-1")
	pic2 = TakeOnePicture("~ Party ~", photoFile + "-2")
	pic3 = TakeOnePicture(".: More fun :.", photoFile + "-3")
	pic4 = TakeOnePicture("The last one :D", photoFile + "-4")
	Composite(pic1,pic2,pic3,pic4, photoFile)
	
def TakeOnePicture(message, photoFile):
	DrawCenterMessage("3",True)
	DrawCenterMessage("2",True)
	DrawCenterMessage("1",True)
	DrawCenterMessage(message,True,False)
	
	photoFile = "photos/" + photoFile + ".jpg"
	if not os.path.isdir("photos") :
		os.makedirs("photos")
	
	# Test if DSLR is ready by reading Gphoto2 summary and finding or not the french word "Erreur" (Error)
	p = sub.Popen('gphoto2 --summary',stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
	while(str(p.communicate()).find("Erreur") != -1):
		sleep(.1)
		p = sub.Popen('gphoto2 --summary',stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
	
	os.popen("gphoto2 --capture-image-and-download --filename " + photoFile + " --force-overwrite &")
	sleep(4)
	return photoFile
	
def Composite(pic1,pic2,pic3,pic4, photoFile):
	#Create composite image 
	WaitLogo()
	borderWidth = 20
	imageWidth = (width-3*borderWidth)/2
	imageHeight = imageWidth*2/3 #only work in landscape mode with 3/2 ratio
	borderHeight = (height-2*imageHeight)/3
	
	while os.path.exists(pic1) == False: # Wait for creation
		sleep(.1)
	pbimage1 = pygame.image.load(pic1)
	pbimage1 = pygame.transform.scale(pbimage1, (imageWidth,imageHeight))
	
	while os.path.exists(pic2) == False: # Wait for creation
		sleep(.1)
	pbimage2 = pygame.image.load(pic2)
	pbimage2 = pygame.transform.scale(pbimage2, (imageWidth,imageHeight))
	
	while os.path.exists(pic3) == False: # Wait for creation
		sleep(.1)
	pbimage3 = pygame.image.load(pic3)
	pbimage3 = pygame.transform.scale(pbimage3, (imageWidth,imageHeight))
	
	while os.path.exists(pic4) == False: # Wait for creation
		sleep(.1)
	pbimage4 = pygame.image.load(pic4)
	pbimage4 = pygame.transform.scale(pbimage4, (imageWidth,imageHeight))
	
	screen.fill(white)	
	screen.blit(pbimage1, (borderWidth, borderHeight))
	screen.blit(pbimage2, (2*borderWidth+imageWidth, borderHeight))
	screen.blit(pbimage3, (borderWidth, 2*borderHeight+imageHeight))
	screen.blit(pbimage4, (2*borderWidth+imageWidth, 2*borderHeight+imageHeight))
	pygame.display.flip()
	
	if not os.path.isdir("composites") :
		os.makedirs("composites")
	pygame.image.save(screen, "composites/" + photoFile + ".jpg")
	sleep(10)
	#pygame.display.flip()
# End Functions

# Demarrage
# drops other possible connections to the camera on every restart just to be safe
os.system("sudo pkill gvfs")
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
app_name = "PhotoPi"
print app_name + " started"
sleep(2)

# Boucle principale
# Pygame init
print "pygame init"
pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption(app_name)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)#FULLSCREEN

LivePreview()
TakePictures()

# Fin
print "End"
pygame.quit()