#!/usr/bin/env python

import pygame

# GPIO Setup (optional)
GPIO_NUMBER_BUTTON_1 = 36
GPIO_NUMBER_BUTTON_2 = 32

# PygameEngine
WIDTH = 1280
HEIGHT = 1024
LOGO_SIZE = 500
FONT = "DejaVuSerif-Bold"

# Camera check
# keywords to find camera status with 'gphoto2 --summary'
# Warning : to avoid encoding problem, i chose words without diacritics (warning of the language parameter, check 'gphoto2 --summary')
KEYWORDS_IN_USE = "Camera is already in use"
KEYWORDS_NO_CAMERA = "*** Error: No camera found. ***"
KEYWORDS_CAMERA_OK = "Access Capability: Read-Write"
DEBUG = True # DEBUG variable is here to avoid using DSLR for testing

# Live preview
LIVE_PREVIEW_ENABLE = True
LIVE_MOVIE_FILE = "captures/livepreview-temp/fifo.mjpg"
PREVIEW_DURATION = 10 # seconds

# Media
DEBUG_FILE = "media/debug.jpg"
ACTION_SCREEN_FILE = "media/Action-screen.jpg"
WAIT_LOGO_FILE = "media/wait.gif"
WAIT_SOUND_FILE = "media/Waiting.wav"
BEEP01_SOUND_FILE = "media/beep-01.wav"
BEEP02_SOUND_FILE = "media/beep-02.wav"

# Capture folders
SEQUENCE_PHOTO_CAPTURES = "captures/photo-captures"
SEQUENCE_PHOTO_COMPOSITES = "captures/photo-composites"
SEQUENCE_STOPMOTION_CAPTURES = "captures/stopmotion-captures"
SEQUENCE_STOPMOTION_COMPOSITES = "captures/stopmotion-composites"
SEQUENCE_STOPMOTION_TEMP = "captures/stopmotion-temp"
SEQUENCE_VIDEO_CAPTURES = "captures/videos"

# Sequence Photo
SEQUENCE_PHOTO_MSG1 = "Smile :)"
SEQUENCE_PHOTO_MSG2 = "~ Party ~"
SEQUENCE_PHOTO_MSG3 = ".: More fun :."
SEQUENCE_PHOTO_MSG4 = "The last one :D"

# Sequence Stop-Motion
SEQUENCE_STOPMOTION_NB_PHOTOS = 5
