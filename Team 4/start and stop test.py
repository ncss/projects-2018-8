from microbit import *
import radio

radio.on()
radio.config(channel = 41)

race_going = 0
while True:
    
    msg = radio.receive()
    if msg:
        if msg == "start":
            display.scroll("started")
            race_going = 1

    
    if button_a.is_pressed() == 1 and race_going == 1:
        radio.send("time")
        race_going = 0


