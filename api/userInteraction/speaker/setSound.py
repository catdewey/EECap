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

arguments = cgi.FieldStorage()
for i in arguments.keys():
    soundNumber = arguments[i].value


while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#setsound number
bus = smbus.SMBus(2) #port i2c2
bus.write_byte(address, soundNumber)

os.remove('/tmp/BusInUse')

#return nothing
print ""