#!/usr/bin/env python

# Blue Dot Mote Colour Picker
# 05/06/2017 
# David Glaude

# First version, use when_double_pressed from version 1.0 of Blue Dot

from bluedot import BlueDot
from signal import pause
import colorsys
from mote import Mote

MAX_CHANNEL=1

mote = Mote()

for channel in range(MAX_CHANNEL):
    mote.configure_channel(channel+1, 16, False)

maxi=MAX_CHANNEL*16

def when_client_connects():
    for channel in range(MAX_CHANNEL):
        for pixel in range(16):
            hue = (((((pixel+(channel*16))/(float(MAX_CHANNEL)*16)) * 360)) % 360) / 360.0
            r,g,b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
            mote.set_pixel(channel + 1, pixel, r, g, b)
    mote.show()

def setall(r,g,b):
    for channel in range(MAX_CHANNEL):
        for pixel in range(16):
            mote.set_pixel(channel + 1, pixel, r, g, b)
    mote.show()

def when_moved(pos):
    h=(pos.angle % 360) / 360
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

