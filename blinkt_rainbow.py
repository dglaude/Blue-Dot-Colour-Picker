#!/usr/bin/env python

# Blue Dot Blinkt Colour Picker
# 05/06/2017 
# David Glaude

# Adapted to use when_double_pressed from version 1.0 of Blue Dot

from bluedot import BlueDot
from signal import pause
import colorsys
import blinkt
#import time

def when_client_connects():
    for x in range(blinkt.NUM_PIXELS):
        hue = ((((x/float(blinkt.NUM_PIXELS)) * 360)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        blinkt.set_pixel(x, r, g, b)
    blinkt.show()

def setall(r,g,b):
    blinkt.set_all(r, g, b)
    blinkt.show()

def when_moved(pos):
    h=((pos.angle+180) % 360) / 360
    s=pos.distance
    v=1.0
    r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, s, v)]
    setall(r,g,b)

def double_pressed():
    setall(0,0,0)

blinkt.set_brightness(0.1)
blinkt.set_clear_on_exit()

bd = BlueDot()
#bd.wait_for_press()

bd.when_client_connects = when_client_connects
bd.when_moved = when_moved
bd.when_double_pressed = double_pressed

pause()

