from cv2 import *
import datetime
import os
import urllib2

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

execfile(ROOT_DIR + '/inc/definitions.py')
execfile(ROOT_DIR + '/inc/helpers.py')
execfile(ROOT_DIR + '/inc/env.py')


if not os.path.exists(PHOTOS_PATH):
    os.makedirs(PHOTOS_PATH)

# Save photo if enabled
if SAVE_PHOTO:
        take_photo()

# Write in logs if enabled
if LOG_ENABLED:
        write_in_log()

# Send email if enabled
if EMAIL_ENABLED:
        send_email()