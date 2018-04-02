
# Define paths
DATA_PATH = ROOT_DIR + '/data'
PHOTOS_PATH = DATA_PATH + '/photos'


# Date objects
date = datetime.datetime.now()
today = str(date.year) + '-' + \
        str(date.month) + '-' + \
        str(date.day) + '_' + \
        str(date.hour) + ':' + \
        str(date.minute) + ':' + \
        str(date.second)


# IP of current network. Helpful for laptops
ip = urllib2.urlopen('https://api.ipify.org').read()
