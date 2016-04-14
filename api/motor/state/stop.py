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

while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)



#send stop signal 
bus = smbus.SMBus(2) #port i2c2
bus.write_byte(address, 0)

os.remove('/tmp/BusInUse')


#return nothing
print ""