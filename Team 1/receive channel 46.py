from microbit import *
import radio
radio.on()
radio.config(channel=47)
print("Start!")
while True:
    msg = radio.receive()
    if msg:
        print(msg)