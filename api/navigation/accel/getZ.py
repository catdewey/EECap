#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
import smbus

address = 0x07

filepath = os.path.join('/tmp', 'BusInUse')

while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)



#get z value  
bus = smbus.SMBus(2) #port i2c2
zValue = bus.read_byte(address)

os.remove('/tmp/BusInUse')


#output zValue .
print "%s" % zValue



