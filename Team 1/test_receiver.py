# README!
# scrolls stuff on the microbit when recieved on channel 51

from microbit import *
import radio

radio.on()
radio.config(channel=51)
while True:
    msg = radio.receive()
    if msg:
        display.scroll(msg)