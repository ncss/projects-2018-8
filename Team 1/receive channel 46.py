from microbit import *
import radio
radio.on()
radio.config(channel=46)

while True:
    msg = radio.receive()
    if msg:
        print(msg)