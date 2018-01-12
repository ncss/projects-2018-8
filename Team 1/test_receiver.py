# Write your code here :-)
from microbit import *
import radio

radio.on()
radio.config(channel=51)
while True:
    msg = radio.receive()
    if msg:
        display.scroll(msg)