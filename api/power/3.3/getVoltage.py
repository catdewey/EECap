#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
import smbus

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
bus = smbus.SMBus(2) #port i2c2
voltage = bus.read_byte(address)

os.remove('/tmp/BusInUse')

#return voltage
print "%s" % voltage



