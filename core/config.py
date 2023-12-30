#!/usr/bin/env python

# GPIO Setup (optional)
GPIO_NUMBER_BUTTON_1 = 32
GPIO_NUMBER_BUTTON_2 = 36

# PygameEngine
WIDTH = 1280
HEIGHT = 1024
LOGO_SIZE = 500
FONT = "DejaVuSerif-Bold"

# Camera
# Check keywords to find camera status with 'gphoto2 --summary'
# Warning : to avoid encoding problem, i chose words without diacritics (warning of the language parameter, check 'gphoto2 --summary')
DEBUG = False # DEBUG variable is here to avoid using DSLR for testing
KEYWORDS_IN_USE = "Camera is already in use"
KEYWORDS_NO_CAMERA = "*** Error: No camera found. ***"
KEYWORDS_CAMERA_OK = "Access Capability: Read-Write"
CMD_CHECK = "gphoto2 --summary"
CMD_PHOTO = "gphoto2 --capture-image-and-download --filename {filename} --force-overwrite"

# Media
PLAY_SOUND = False
DEBUG_FILE = "media/debug.jpg"
ACTION_SCREEN_FILE1 = "media/action-screen-1.jpg"
ACTION_SCREEN_FILE2 = "media/action-screen-2.jpg"
ACTION_SCREEN_FILE3 = "media/action-screen-3.jpg"
ACTION_SCREEN_FILE4 = "media/action-screen-4.jpg"
WAIT_LOGO_FILE = "media/wait.gif"
WAIT_SOUND_FILE = "media/Waiting.wav"
BEEP01_SOUND_FILE = "media/beep-01.wav"
BEEP02_SOUND_FILE = "media/beep-02.wav"
BEEP03_SOUND_FILE = "media/beep-03.wav"

# Capture folders
SEQUENCE_PHOTO_CAPTURES = "captures/photo-captures"
SEQUENCE_PHOTO_COMPOSITES = "captures/photo-composites"

# Sequence Photo
SEQUENCE_PHOTO_MSG1 = "Smile :)"
SEQUENCE_PHOTO_MSG2 = "~ Party ~"
SEQUENCE_PHOTO_MSG3 = ".: More fun :."
SEQUENCE_PHOTO_MSG4 = "The last one :D"

# Sequence Slideshow
QUIT_BTON_MSG = "Quit"
PREC_BTON_MSG = "Prev."

# Mail
MAIL = True
MAIL_FROM = "foo_foo@foo.com"
MAIL_TO = ["foo_love@foo.com"]
MAIL_SUBJECT = "PhotoPI"
MAIL_TEXT = ""
MAIL_SMTP = "smtp.foo.com"
MAIL_SMTP_USER = "foo"
MAIL_SMTP_PWD = "secret_foo"
