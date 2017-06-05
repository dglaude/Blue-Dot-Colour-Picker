# Blue-Dot-Colour-Picker
Use Blue Dot library to control the colour off LEDs

Blue Dot Colour Picker rely on [Blue Dot library](https://github.com/martinohanlon/BlueDot) from by [Martin O'Hanlon](http://stuffaboutco.de/) @martinohanlon.

The you need some hardware with RGB LED that is already supported:
* [Pimoroni Blinkt!](https://shop.pimoroni.com/products/blinkt) with it's [library](https://github.com/pimoroni/blinkt) Please use blinktCP.py.
* [Pimoroni Unicorn pHAT](https://shop.pimoroni.com/products/unicorn-phat) with it's [library](https://github.com/pimoroni/unicorn-hat). Please use unicornCP.py
* [Pimoroni Unicorn HAT](https://shop.pimoroni.com/products/unicorn-hat) with it's [library](https://github.com/pimoroni/unicorn-hat). Please use unicornCP.py
* [Raspberry Pi Fondation Sense HAT](https://www.raspberrypi.org/products/sense-hat/) with it's [library](https://www.raspberrypi.org/documentation/hardware/sense-hat/). Please use senseCP.py

## Usage

Click the Blue Dot to turn LEDs on.
Swipe to select your prefered colour for the mood.
Double click turn off your LEDs.

## New version

blinkt and unicorn version are now available in a version that use when_double_pressed from version 1.0 of Blue Dot library.

Changes between *CP.py version and *_rainbow.py version:
* When a client connect, it display a rainbow.
* A simple touch without move does not change the colour.
* To change the colour you have to move your finger after the click.
* Double click turn the LEDs off

