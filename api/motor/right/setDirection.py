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
    motorDirection = arguments[i].value



while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#set motor direction
bus = smbus.SMBus(2) #port i2c2
bus.write_byte_data(address, motorDirection)

os.remove('/tmp/BusInUse')

#return null
print ""