#!/usr/bin/env python

import core.config as config
import os
import os.path
import core.pygameEngine as pygameEngine
import core.camera as camera
from time import sleep

def Start():
    if(config.DEBUG or not config.LIVE_PREVIEW_ENABLE):
        return

    # Start recording live preview
    pygameEngine.DrawCenterMessage(config.LIVE_PREVIEW_MSG, True)
    print("Start recording live preview")
    if os.path.exists(config.LIVE_MOVIE_FILE):
        os.remove(config.LIVE_MOVIE_FILE)
    os.mkfifo(config.LIVE_MOVIE_FILE)

    # To avoid problem, wait
    while not os.path.exists(config.LIVE_MOVIE_FILE):
        time.sleep(.1)
    camera.RecordPreview(config.LIVE_MOVIE_FILE, config.PREVIEW_DURATION)

    # Playing live preview
    pygameEngine.DrawCenterMessage("") #Clean screen before preview
    print("Playing live preview")
    os.popen(config.CMD_LIVE_PREVIEW_PLAY.format(filename = config.LIVE_MOVIE_FILE))
