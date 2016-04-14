#!/usr/bin/python
import cgi
import cgitb
import sys
import time
import os
import urlparse
#import wiringx

address = 0x07
ledNumber = sys.argv[1]
filepath = os.path.join('/tmp', 'BusInUse')

while (True):
    try:
        file = open(filepath)
    
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)



#get z value  GPIO.input(address, ledNumber,0)
os.remove('/tmp/BusInUse')

print "Content-type: text/html\n\n"

#output xValue .
print "<h1>This is the z value: %s</h1>" % zValue



