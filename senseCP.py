#!/usr/bin/env python

# Blue Dot Sense HAT Colour Picker
# 02/06/2017 
# David Glaude

from bluedot import BlueDot
import colorsys
import time

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

last_time = time.time()

def setall(r,g,b):
    for x in range(8):
        for y in range(8):
            sense.set_pixel(x, y, r, g, b)
# Should use sense.clear() if r=g=b=0

def move(pos):
    h=((pos.angle+180) % 360) / 360
    s=pos.distance
    v=1.0
    r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, s, v)]
    setall(r,g,b)

def rmove(pos):
    global last_time
    current_time=time.time()
    delta = current_time-last_time
    last_time = current_time
    if (delta<0.3) :
        setall(0,0,0)

bd = BlueDot()
bd.wait_for_press()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = rmove

while True:
    time.sleep(1)

