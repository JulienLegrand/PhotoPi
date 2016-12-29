#!/usr/bin/env python

import os
import os.path
import pygameEngine
import Camera
from time import sleep

# Variables
LIVE_MOVIE_FILE = "fifo.mjpg"
PREVIEW_DURATION = 10 #secondes

def Start():
    if(Camera.DEBUG):
        return

    # Start recording live preview
    pygameEngine.DrawCenterMessage("Prepare for fun", True)
    print "Start recording live preview"
    if os.path.exists(LIVE_MOVIE_FILE):
        os.remove(LIVE_MOVIE_FILE)
    os.mkfifo(LIVE_MOVIE_FILE)

    # To avoid problem, wait
    while not os.path.exists(LIVE_MOVIE_FILE):
        time.sleep(.1)
    Camera.RecordPreview(LIVE_MOVIE_FILE, PREVIEW_DURATION)

    # Playing live preview
    pygameEngine.DrawCenterMessage("") #Clean screen before preview
    print "Playing live preview"
    os.popen("omxplayer " + LIVE_MOVIE_FILE + " --live")