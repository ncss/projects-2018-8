from microbit import *
import radio

GAME_CHANNEL = 49
radio.config(channel=GAME_CHANNEL)
radio.on()

TICK = Image("00000:00009:00090:90900:09000")
CROSS = Image("90009:09090:00900:09090:90009")
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

button = Button(pin0, True)
CELEBRATE_TIME = 3000
celebrate_timer = CELEBRATE_TIME
previous_time = running_time()

while True:
    msg = radio.receive()
    if msg and msg.startswith("tof:"):
        if (button.boolean and msg == "tof:true") or (not button.boolean and msg == "tof:false"):
            display.show(TICK)
            music.play(music.POWER_UP)
            celebrate_timer = CELEBRATE_TIME
        else:
            display.show(CROSS)
            music.play(music.WAWAWAWAA)
            celebrate_timer = CELEBRATE_TIME

    if button.was_pressed():
        if button.boolean:
            radio.send("tof:true")
        else:
            radio.send("tof:false")
    
    current_time = running_time()
    time_elapsed = current_time - previous_time
    previous_time = current_time
    celebrate_timer -= time_elapsed
    if celebrate_timer <= 0:
        celebrate_timer = 0
        display.clear()