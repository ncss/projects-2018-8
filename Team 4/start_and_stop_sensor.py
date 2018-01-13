from microbit import *
import radio

radio.on()
radio.config(channel=41)

left_back = pin8
left_forward = pin12
right_back = pin0
right_forward = pin16
left_light = pin1
right_light = pin2
sense_num = 0

while True:
    
    sensor = left_sense.read_analog()
    if sensor < 20:
        sense_num += 1
    
        if sense_num == 1:
            radio.send("start")
            sleep(2000)
            
        if sense_num == 2:
            radio.send("end")
            sleep(1000)
            left_forward.write_analog(0)
            right_forward.write_analog(0)
    else:
        left_forward.write_analog(300)
        right_forward.write_analog(300)