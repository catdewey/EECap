#!/usr/bin/python
import urlparse
import cgitb
import sys
import time
import os
#import wiringx
cgitb.enable()

address = 0x0F
ledNumber = sys.argv[1]
filepath = os.path.join('/tmp', 'BusInUse')

while (True):
    try:
        file = open(filepath)
    except IOError:
        open(filepath, 'w+')
        break
    time.sleep(0.08)



#state =  GPIO.input(address, ledNumber,0)

print "Content-type: text/html\n\n"
print "<h1>hello, state is: %s </h1>" ledNumber #really state, but ledNumber fot testing 


print os.environ['HOME']
pring os.environ.get('KEY_THAT_might_exist')

os.remove('/tmp/BusInUse')
