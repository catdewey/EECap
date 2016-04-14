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


#get longitude  GPIO.input(address, ledNumber,0)

os.remove('/tmp/BusInUse')

#return longitude
print "Content-type: text/html\n\n"
print "<h1>This is the Longitude: %s</h1>" % longitude