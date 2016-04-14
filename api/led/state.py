#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
import smbus

address = 0x0F

filepath = os.path.join('/tmp', 'BusInUse')

print "Content-type: text/html\n\n"

arguments = cgi.FieldStorage()
for i in arguments.keys():
    ledNumber = arguments[i].value


while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#get led state  GPIO.input(address, ledNumber,0)
bus = smbus.SMBus(2) #port i2c2
ledState = bus.read_byte(address, ledNumber)
os.remove('/tmp/BusInUse')

#prints ledState once we can get that.
print "%s" % ledState