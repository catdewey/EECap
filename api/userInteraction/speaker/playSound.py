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

while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#send play signal
bus = smbus.SMBus(2) #port i2c2
bus.write_byte(address, 1)


os.remove('/tmp/BusInUse')

#return nothing
print ""