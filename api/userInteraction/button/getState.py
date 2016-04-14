#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
import smbus

address = 0x09

filepath = os.path.join('/tmp', 'BusInUse')

print "Content-type: text/html\n\n"

#arguments = cgi.FieldStorage()
#for i in arguments.keys():
#    buttonNumber = arguments[i].value

while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#get button state  GPIO.input(address, ledNumber,0)
bus = smbus.SMBus(2) #port i2c2
buttonState = bus.read_byte(address)

os.remove('/tmp/BusInUse')

print "%s" % buttonState