# README!
# scrolls stuff on the microbit when recieved on channel 51
try:
    from microbit import *
    import radio
except:
    from quokka import *

radio.on()
radio.config(channel=51)
while True:
    msg = radio.receive()
    if msg:
        display.scroll(msg)