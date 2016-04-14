#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
#import wiringx

address = 0x07

filepath = os.path.join('/tmp', 'BusInUse')


while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#get lat  GPIO.input(address, ledNumber,0)

os.remove('/tmp/BusInUse')

#return lat
print "Content-type: text/html\n\n"
print "<h1>This is the state of the breadboard pin you are inquiring about: %s</h1>" % lat

