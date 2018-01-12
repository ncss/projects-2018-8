from microbit import *
import radio
radio.on()
radio.config(channel=43)
upper_th = -200
lower_th = -1600
motion_state = "not_moving"
round_start = False
while True:
    message = radio.receive()
    #(start transmitting time)
    if message == "1":
       round_start = True
    #stop transmitting time
    if message == "0":
        round_start = False
    #detecting jump
    if round_start == True:
        display.clear()
        accelerometer.get_z()
        if upper_th < accelerometer.get_z(): #up
            motion_state = "move_up"
        if lower_th > accelerometer.get_z(): #down
            motion_state = "move_down"
        if motion_state == "move_up" or motion_state == "move_down":
            radio.send("x")
            display.show(Image.HAPPY)
            print("JUMPED")
            motion_state = "not_moving"
    