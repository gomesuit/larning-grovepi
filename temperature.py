#!/usr/bin/env python

import time
import grovepi
#import math

# Connect the Grove 4 Digit Display to digital port D5
# CLK,DIO,VCC,GND
display = 5
grovepi.pinMode(display,"OUTPUT")

# If you have an analog sensor connect it to A0 so you can monitor it below
sensor = 0
grovepi.pinMode(sensor,"INPUT")

time.sleep(.5)

while True:
    try:
        grovepi.fourDigit_brightness(display,2)

        #seconds = 10
        #grovepi.fourDigit_monitor(display,sensor,seconds)
        temp = round(grovepi.temp(sensor,'1.2'), 2)
        grovepi.fourDigit_init(display)
        grovepi.fourDigit_number(display,int(temp * 100),0)
        #print(temp.__class__)
        print("temp =", temp)
        time.sleep(.5)

    except KeyboardInterrupt:
        grovepi.fourDigit_off(display)
        break
    except IOError:
        print ("Error")
