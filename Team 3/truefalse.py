# pls dont edit this

from microbit import *
import radio

GAME_CHANNEL = 49
radio.config(channel=GAME_CHANNEL)
radio.on()


class Button:
    def __init__(self, pin, boolean):
        self.pin = pin
        self.pin.set_pull(self.pin.NO_PULL)
        self.boolean = boolean
        self.push = True

    def was_pressed(self):
        if self.pin.read_digital():
            if self.push:
                self.push = False
                return True
        else:
            self.push = True
        
        return False


button = Button(pin0, True)

while True:
    msg = radio.receive()
    if msg:
        print(msg)

    if button.was_pressed():
        if button.boolean:
            radio.send("true")
        else:
            radio.send("false")