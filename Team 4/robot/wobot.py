from microbit import *

left_back = pin12
left_forward = pin8
right_back = pin16
right_forward = pin0
left_light = pin1
right_light = pin2
turn_ratio = 6
turn_speed = 1023

def left_wheel(speed):
    if speed < 0 :
        left_forward.write_analog(0)
        left_back.write_analog(abs(speed))
    else:
        left_forward.write_analog(speed)
        left_back.write_analog(0)
    
def right_wheel(speed):
    if speed < 0 :
        right_forward.write_analog(0)
        right_back.write_analog(abs(speed))
    else:
        right_forward.write_analog(speed)
        right_back.write_analog(0)


while True:
    if left_light.read_analog() > 10 and right_light.read_analog() > 10:
        left_wheel(1023)
        right_wheel(1023)
    elif left_light.read_analog() > 10:
        left_wheel(turn_speed)
        right_wheel(turn_speed/turn_ratio)
        turn = "left"
    elif right_light.read_analog() > 10:
        right_wheel(turn_speed)
        left_wheel(turn_speed/turn_ratio)
        turn = "right"