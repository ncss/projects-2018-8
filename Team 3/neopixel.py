from microbit import *
from random import randint
import neopixel
import radio


# Setup the Neopixel strip on pin0 with a length of 10 pixels
np = neopixel.NeoPixel(pin0, 10)

lights_on = 10
radio.on()
radio.config(channel = 49)

while True:
    msg = radio.receive()
    if msg and msg.startswith("score:"):
        new_msg = msg[6:]
        new_no = int(new_msg)
        print(new_
    
    for thisloop in range(0,100):
        for pixel_id in range(0, lights_on):
            red = randint(0, 50)
            green = randint(0, 50)
            blue = randint(0, 50)
            np[pixel_id] = (red, green, blue)
        np.show()
        sleep(randint(10,100))
    for colour in range (0,128):
        for pixel_id in range(0, lights_on):
            np[pixel_id] = (colour, 0, 0)
        np.show()
        sleep(10)
    for colour in range (0,128):
        for pixel_id in range(0, lights_on):
            np[pixel_id] = (128 - colour, colour, 0)
        np.show()
        sleep(10)    
    for colour in range (0,128):
        for pixel_id in range(0, lights_on):
            np[pixel_id] = (0, 128-colour, colour)
        np.show()
        sleep(10)
