#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
import smbus

address = 0x0B

filepath = os.path.join('/tmp', 'BusInUse')

print "Content-type: text/html\n\n"

arguments = cgi.FieldStorage()
for i in arguments.keys():
    motorSpeed = arguments[i].value



while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#set motorSpeed  GPIO.input(address, ledNumber,0)
bus = smbus.SMBus(2) #port i2c2
bus.write_byte(address, motorSpeed)


os.remove('/tmp/BusInUse')

#null
print ""