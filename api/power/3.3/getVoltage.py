#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
#import wiringx

address = 0x0A

filepath = os.path.join('/tmp', 'BusInUse')




while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#get voltage  GPIO.input(address, ledNumber,0)

os.remove('/tmp/BusInUse')

#return voltage
print "Content-type: text/html\n\n"
print "<h1>This is the voltage should be 3.3: %s</h1>" % voltage



