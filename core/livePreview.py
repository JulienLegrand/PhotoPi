#!/usr/bin/env python

import config
import os
import os.path
import pygameEngine
import camera
from time import sleep

def Start():
    if(config.DEBUG or not config.LIVE_PREVIEW_ENABLE):
        return

    # Start recording live preview
    pygameEngine.DrawCenterMessage("Prepare for fun", True)
    print "Start recording live preview"
    if os.path.exists(config.LIVE_MOVIE_FILE):
        os.remove(config.LIVE_MOVIE_FILE)
    os.mkfifo(config.LIVE_MOVIE_FILE)

    # To avoid problem, wait
    while not os.path.exists(config.LIVE_MOVIE_FILE):
        time.sleep(.1)
    camera.RecordPreview(config.LIVE_MOVIE_FILE, config.PREVIEW_DURATION)

    # Playing live preview
    pygameEngine.DrawCenterMessage("") #Clean screen before preview
    print "Playing live preview"
    os.popen("omxplayer " + config.LIVE_MOVIE_FILE + " --live")
