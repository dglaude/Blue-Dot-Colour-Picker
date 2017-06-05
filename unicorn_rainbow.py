#!/usr/bin/env python

# Blue Dot Unicorn [p]HAT Colour Picker
# 05/06/2017 
# David Glaude

# Adapted to use when_double_pressed from version 1.0 of Blue Dot

from bluedot import BlueDot
from signal import pause
import colorsys
import unicornhat

unicornhat.set_layout(unicornhat.AUTO)
unicornhat.rotation(0)
unicornhat.brightness(0.5)
width,height=unicornhat.get_shape()

def when_client_connects():
    maxi=height+width
    for y in range(height):
        for x in range(width):
            hue = (((((x+y)/float(maxi)) * 360)) % 360) / 360.0
            r,g,b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
            unicornhat.set_pixel(x, y, r, g, b)
    unicornhat.show()

def setall(r,g,b):
    for y in range(height):
        for x in range(width):
            unicornhat.set_pixel(x,y,r,g,b)
    unicornhat.show()

def when_moved(pos):
    h=((pos.angle) % 360) / 360
    s=pos.distance
    v=1.0
    r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, s, v)]
    setall(r,g,b)

def double_pressed():
    setall(0,0,0)

bd = BlueDot()

bd.when_client_connects = when_client_connects
bd.when_moved = when_moved
bd.when_double_pressed = double_pressed

pause()

