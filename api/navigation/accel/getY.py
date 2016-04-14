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



#get y value  GPIO.input(address, ledNumber,0)
os.remove('/tmp/BusInUse')

print "Content-type: text/html\n\n"

#output yValue .
print "<h1>This is the y value: %s</h1>" % yValue


