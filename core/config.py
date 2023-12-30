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
KEYWORDS_IN_USE = "Camera is already in use"
KEYWORDS_NO_CAMERA = "*** Error: No camera found. ***"
KEYWORDS_CAMERA_OK = "Access Capability: Read-Write"
DEBUG = True # DEBUG variable is here to avoid using DSLR for testing
CMD_CHECK = "gphoto2 --summary"
CMD_PHOTO = "gphoto2 --capture-image-and-download --filename {filename} --force-overwrite"
CMD_MOVIE = "gphoto2 --capture-movie={duration}s --stdout> {filename}"

# Live preview
LIVE_PREVIEW_MSG = "Find your place"
LIVE_PREVIEW_ENABLE = False
LIVE_MOVIE_FILE = "captures/livepreview-temp/fifo.mjpg"
PREVIEW_DURATION = 10 # seconds
CMD_LIVE_PREVIEW_PLAY = "omxplayer {filename} --live"

# Media
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
SEQUENCE_STOPMOTION_CAPTURES = "captures/stopmotion-captures"
SEQUENCE_STOPMOTION_COMPOSITES = "captures/stopmotion-composites"
SEQUENCE_STOPMOTION_TEMP = "captures/stopmotion-temp"
SEQUENCE_VIDEO_CAPTURES = "captures/videos"

# Sequence Photo
SEQUENCE_PHOTO_MSG1 = "Smile :)"
SEQUENCE_PHOTO_MSG2 = "~ Party ~"
SEQUENCE_PHOTO_MSG3 = ".: More fun :."
SEQUENCE_PHOTO_MSG4 = "The last one :D"

# Sequence Slideshow
QUIT_BTON_MSG = "Quit"
PREC_BTON_MSG = "Prev."

# Sequence Stop-Motion
SEQUENCE_STOPMOTION_NB_PHOTOS = 5
MUSIC_FILE = "media/music.mp3"
CMD_SHRINK = "mogrify -resize 1920x1080 {filename}"
CMD_ADD_MORPH_FRAMES = "sudo convert {filename1} {filename2} -delay 100 -morph 10 {filenamePattern}"
CMD_ENCODE = "sudo mencoder mf://{image_folder}/*.jpg -mf w=1920:h=1080:fps=20:type=jpg -nosound -ovc x264 -x264encopts bitrate=2000 -o {filename}"
CMD_ADD_MUSIC = "sudo avconv -i {filename_in} -i {filename_music} -c copy -map 0:v -map 1:a -shortest {filename_out} -y"
CMD_STOPMOTION_PLAY = "omxplayer {filename} -o local --vol -4000"

# Sequence Video
CMD_VIDEO_PLAY = "omxplayer {filename}"

# Mail
MAIL = True
MAIL_FROM = "foo_foo@foo.com"
MAIL_TO = ["foo_love@foo.com"]
MAIL_SUBJECT = "PhotoPI"
MAIL_TEXT = ""
MAIL_SMTP = "smtp.foo.com"
MAIL_SMTP_USER = "foo"
MAIL_SMTP_PWD = "secret_foo"
