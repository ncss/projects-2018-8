
from microbit import *
import radio
radio.on()
radio.config(channel=43)
upper_th = -200
lower_th = -1600
motion_state = "not_moving"
round_start = False
up_first = 0
down_first = 0
just_jumped = 0
just_ducked = 0

while True:
    message = radio.receive()
    #(start transmitting time)
    if message == "1":
       round_start = True
    #stop transmitting time
    if message == "0":
        round_start = False
    if round_start == True:
        display.clear()
        if just_jumped == 1:
            just_jumped = 0
        if just_ducked == 1:
            just_ducked = 0
        #detecting jump
        if lower_th > accelerometer.get_z() and up_first == 1: #down after up
            radio.send("JUMP")
            display.show(Image.HAPPY)
            sleep(1500)
            up_first = 0
        if upper_th < accelerometer.get_z(): #up
            up_first = 1

        #detecting duck
        if upper_th < accelerometer.get_z() and down_first == 1: #up after down
            radio.send("DUCK")
            display.show(Image.HAPPY)
            sleep(1500)
            down_first = 0
        if lower_th > accelerometer.get_z(): #down
            down_first = 1

        