#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
#import wiringx

address = 0x0B

filepath = os.path.join('/tmp', 'BusInUse')

while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#get motorDirection  GPIO.input(address, ledNumber,0)
os.remove('/tmp/BusInUse')

#change pinNumber to pinState once we can get that.
print "<h1>This is the direction of the left motor: %s</h1>" % motorDirection



