#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
import smbus

address = 0x08

filepath = os.path.join('/tmp', 'BusInUse')

print "Content-type: text/html\n\n"

arguments = cgi.FieldStorage()
for i in arguments.keys():
    pinNumber = arguments[i].value


while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)


#set pin to 1  
bus = smbus.SMBus(2) #port i2c2
bus.write_byte_data(address, pinNumber, 1)

os.remove('/tmp/BusInUse')

#returns nothing
print ""



