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
import core.mail as mail

def TakePictures():
	#Attribute a name with current time for all photos and composite
	photoFile = dt.datetime.now().strftime("%Y%m%d-%Hh%Mm%S")
	pic1 = TakeOnePicture(config.SEQUENCE_PHOTO_MSG1, photoFile + "-1")
	pic2 = TakeOnePicture(config.SEQUENCE_PHOTO_MSG2, photoFile + "-2")
	pic3 = TakeOnePicture(config.SEQUENCE_PHOTO_MSG3, photoFile + "-3")
	pic4 = TakeOnePicture(config.SEQUENCE_PHOTO_MSG4, photoFile + "-4")
	return Composite(pic1, pic2, pic3, pic4, photoFile)

def TakeOnePicture(message, photoFile):
	pygameEngine.DrawCenterMessage("3", True)
	pygameEngine.DrawCenterMessage("2", True)
	pygameEngine.DrawCenterMessage("1", True)
	pygameEngine.SoundBip2()
	pygameEngine.DrawCenterMessage(message, True)
	sleep(1)

	photoFile = config.SEQUENCE_PHOTO_CAPTURES + "/" + photoFile + ".jpg"
	if not os.path.isdir(config.SEQUENCE_PHOTO_CAPTURES) :
		os.makedirs(config.SEQUENCE_PHOTO_CAPTURES)

	camera.WaitCamera()
	pygameEngine.Fill(pygameEngine.WHITE_COLOR)
	camera.TakePhoto(photoFile)

	sleep(3)
	return photoFile

def photoLoad(file):
	dtStart = dt.datetime.now()
	while os.path.exists(file) == False: # Wait for creation
		if (dt.datetime.now() - dtStart).seconds / 60 > 1 : raise Exception('No image taken')  # special way out if no image appears
		sleep(.1)
	return pygame.image.load(file).convert()

def Composite(pic1, pic2, pic3, pic4, photoFile):
	screen = pygameEngine.GetScreen()

	#Play sound
	pygameEngine.SoundWait()

	#Create composite image
	pygameEngine.WaitLogo()
	borderWidth = 20
	imageWidth = (config.WIDTH - 3 * borderWidth) // 2
	imageHeight = imageWidth * 2 // 3 #only work in landscape mode with 3/2 ratio
	borderHeight = (config.HEIGHT - 2 * imageHeight) // 3

	#Photos loading
	pbimage1Raw = photoLoad(pic1)
	pbimage1 = pygame.transform.scale(pbimage1Raw, (imageWidth, imageHeight))
	pbimage2Raw = photoLoad(pic2)
	pbimage2 = pygame.transform.scale(pbimage2Raw, (imageWidth, imageHeight))
	pbimage3Raw = photoLoad(pic3)
	pbimage3 = pygame.transform.scale(pbimage3Raw, (imageWidth, imageHeight))
	pbimage4Raw = photoLoad(pic4)
	pbimage4 = pygame.transform.scale(pbimage4Raw, (imageWidth, imageHeight))

	#Fade in
	i = 50
	while(i<=255):
		screen.fill(pygameEngine.WHITE_COLOR)
		pbimage1.set_alpha(i)
		pbimage2.set_alpha(i)
		pbimage3.set_alpha(i)
		pbimage4.set_alpha(i)
		screen.blit(pbimage1, (borderWidth, borderHeight))
		screen.blit(pbimage2, (2 * borderWidth + imageWidth, borderHeight))
		screen.blit(pbimage3, (borderWidth, 2 * borderHeight + imageHeight))
		screen.blit(pbimage4, (2 * borderWidth + imageWidth, 2 * borderHeight + imageHeight))
		pygame.display.flip()
		#pygame.time.delay(5) #To slow down animation
		i += 5 #To speed up animation

	#Composition only for saving photo file
	ratio = 3
	photoSurface = pygame.Surface((config.WIDTH * ratio, config.HEIGHT * ratio))
	photoSurface.fill(pygameEngine.WHITE_COLOR)
	imageWidth = imageWidth * ratio
	imageHeight = imageHeight * ratio
	borderWidth = borderWidth * ratio
	borderHeight = borderHeight * ratio
	pbimage1 = pygame.transform.scale(pbimage1Raw, (imageWidth, imageHeight))
	pbimage2 = pygame.transform.scale(pbimage2Raw, (imageWidth, imageHeight))
	pbimage3 = pygame.transform.scale(pbimage3Raw, (imageWidth, imageHeight))
	pbimage4 = pygame.transform.scale(pbimage4Raw, (imageWidth, imageHeight))
	photoSurface.blit(pbimage1, (borderWidth, borderHeight))
	photoSurface.blit(pbimage2, (2 * borderWidth + imageWidth, borderHeight))
	photoSurface.blit(pbimage3, (borderWidth, 2 * borderHeight + imageHeight))
	photoSurface.blit(pbimage4, (2 * borderWidth + imageWidth, 2 * borderHeight + imageHeight))

	#Save
	if not os.path.isdir(config.SEQUENCE_PHOTO_COMPOSITES) :
		os.makedirs(config.SEQUENCE_PHOTO_COMPOSITES)

	compositePhoto = config.SEQUENCE_PHOTO_COMPOSITES + "/" + photoFile + ".jpg"
	pygame.image.save(photoSurface, compositePhoto)
	sleep(4)
	return compositePhoto

def SendMail(compositePhoto):
	if not config.MAIL :
		return
	print("Send mail")
	mail.send_mail(config.MAIL_FROM, config.MAIL_TO, config.MAIL_SUBJECT, config.MAIL_TEXT, [compositePhoto], config.MAIL_SMTP, config.MAIL_SMTP_USER, config.MAIL_SMTP_PWD)

def Start():
	try:
		print("Photo Start")
		compositePhoto = TakePictures()
		SendMail(compositePhoto)
		pygameEngine.SoundBip3()
	except Exception as e:
		print("ERREUR : Photo : " + str(sys.exc_info()[0]) + " : " + str(e))
		pygameEngine.ShowError()
