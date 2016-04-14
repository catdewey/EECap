#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
#import wiringx

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


#get pin state  GPIO.input(address, ledNumber,0)
os.remove('/tmp/BusInUse')

#change pinNumber to pinState once we can get that.
print "<h1>This is the state of the breadboard pin you are inquiring about: %s</h1>" % pinNumber