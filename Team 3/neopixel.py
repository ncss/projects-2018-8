from microbit import *
from random import randint
import neopixel
import radio
import math

# Setup the Neopixel strip on pin0 with a length of 10 pixels
np = neopixel.NeoPixel(pin0, 10)

max_no_lights = 8
lights_on = max_no_lights
max_value = 60000
radio.on()
radio.config(channel = 49)
can_i_loop = True
msg = ""

while True:
    if msg and msg.startswith("score:"):
        new_msg = msg[6:]
        new_no = int(new_msg)
        lights_on = math.ceil(new_no/max_value*max_no_lights)
        lights_off = max_no_lights - lights_on
        for pixel_id in range(lights_on, max_no_lights):
            np[pixel_id] = (0, 0, 0)
        can_i_loop = True

    if can_i_loop:
        for thisloop in range(0,100):
            for pixel_id in range(0, lights_on):
                red = randint(0, 50)
                green = randint(0, 50)
                blue = randint(0, 50)
                np[pixel_id] = (red, green, blue)
            np.show()
            msg = radio.receive()
            if msg and msg.startswith("score:"):
                can_i_loop = False
                break
            sleep(randint(10,100))
    if can_i_loop:
        for colour in range (0,128):
            for pixel_id in range(0, lights_on):
                np[pixel_id] = (colour, 0, 0)
            np.show()
            msg = radio.receive()
            if msg and msg.startswith("score:"):
                can_i_loop = False
                break
            sleep(10)
    if can_i_loop:
        for colour in range (0,128):
            for pixel_id in range(0, lights_on):
                np[pixel_id] = (128 - colour, colour, 0)
            np.show()
            msg = radio.receive()
            if msg and msg.startswith("score:"):
                can_i_loop = False
                break
            sleep(10)    
    if can_i_loop:
        for colour in range (0,128):
            for pixel_id in range(0, lights_on):
                np[pixel_id] = (0, 128-colour, colour)
            np.show()
            msg = radio.receive()
            if msg and msg.startswith("score:"):
                can_i_loop = False
                break
            sleep(10)
