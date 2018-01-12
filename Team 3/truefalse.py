from microbit import *
import radio

GAME_CHANNEL = 49
radio.config(channel=GAME_CHANNEL)
radio.on()


class Button:
    def __init__(self, pin, boolean):
        self.pin = pin
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


# button = Button(pin0, True)
button = button_a

while True:
    msg = radio.receive()
    if msg:
        print(msg)

    if button.was_pressed():
        if True:
            radio.send("tof:true")
        else:
            radio.send("tof:false")
