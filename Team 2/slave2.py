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
        if not (motion_state != "move_down" or motion_state != "move_up"):
            accelerometer.get_z()
            if upper_th < accelerometer.get_z(): #up
                motion_state = "move_up"
            if lower_th > accelerometer.get_z(): #down
                motion_state = "move_down"
            if motion_state == "move_up":
                radio.send("move_up")
                display.show(Image.ARROW_N)
                print("move_up")
                motion_state = "not_moving"
            if motion_state == "move_down":
                radio.send("move_down")
                display.show(Image.ARROW_S)
                print("move_down")
                
    