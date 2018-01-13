from microbit import *
from random import randint
import neopixel
np = neopixel.NeoPixel(pin13, 30)
for i in range(30)
    np[i] = (0, 0, 0)
np_editing = 0
while True:
    if button_a.was_pressed():
        np_editing += 1
    if button_b.was_pressed():
        np_editing -= 1
    np[np_editing] = (250, 250, 250)