#!/usr/bin/env python

# Blue Dot Blinkt Colour Picker
# 02/06/2017 
# David Glaude

from bluedot import BlueDot
import colorsys
import time
import blinkt

last_time = time.time()

def setall(r,g,b):
#    for x in range(blinkt.NUM_PIXELS):
#        blinkt.set_pixel(x, r, g, b)
    blinkt.set_all(r, g, b)
    blinkt.show()

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

blinkt.set_brightness(0.1)
blinkt.set_clear_on_exit()

bd = BlueDot()
bd.wait_for_press()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = rmove

while True:
    time.sleep(1)

