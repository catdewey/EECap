#!/usr/bin/python
import cgi
import sys
import time
import os.path
#import wiringx

address = 0x0F
ledNumber = sys.argv[1]
filepath = os.path.join('/tmp', 'BusInUse')

while (True):
    try:
        file = open(filepath)
        print "no exit"
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)



#setInputto0  GPIO.input(address, ledNumber,0)
os.remove('/tmp/BusInUse')


