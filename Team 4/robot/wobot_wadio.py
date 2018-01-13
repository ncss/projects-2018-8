from microbit import *
import radio

radio.on()
radio.config(channel=41)
left_back = pin12
left_forward = pin8
right_back = pin16
right_forward = pin0
left_light = pin1
right_light = pin2

#controls left wheel, -ve speed is backward
def left_wheel(speed):
    if speed < 0 :
        left_forward.write_analog(0)
        left_back.write_analog(abs(speed))
    else:
        left_forward.write_analog(speed)
        left_back.write_analog(0)

#controls right wheel, -ve speed is backward
def right_wheel(speed):
    if speed < 0 :
        right_forward.write_analog(0)
        right_back.write_analog(abs(speed))
    else:
        right_forward.write_analog(speed)
        right_back.write_analog(0)

#follows line. Increased turn ratio results in tighter turning. 
#turn speed must be a value between 0 -> 1023.
#time must be in milliseconds
def follow_line(turn_ratio, turn_speed):
    total_time = 0
    while True:
        if left_light.read_analog() > 10 and right_light.read_analog() > 10:
            left_wheel(turn_speed)
            right_wheel(turn_speed)
        elif left_light.read_analog() > 10:
            left_wheel(turn_speed)
            right_wheel(turn_speed/turn_ratio)
        elif right_light.read_analog() > 10:
            right_wheel(turn_speed)
            left_wheel(turn_speed/turn_ratio)
#maps sensor value to output value, where x is sensor value, 
#a->b is the range of sensor values, and c->d is the range of desired output values.
def map_to_range(x):
    a = 600
    b = 2000
    c = 170
    d = 1023
    if x < a:
        x = a
    elif x > b:
        x = b
    return 1023 - ((x-a)/(b-a)*(d-c)+c)
previous_speeds = [150]
avg = 0
length = 2
while True:
    msg = radio.receive()
    if len(previous_speeds) == length:
        previous_speeds.pop(0)
    if msg:
        previous_speeds.append(map_to_range(int(msg))+300)
        display.show(Image.CHESSBOARD)
    else:
        previous_speeds.append(avg-4)
        display.clear()
    avg = sum(previous_speeds)/len(previous_speeds)
    if avg < 0:
        avg = 0
    left_wheel(avg)
    right_wheel(avg)
    if left_light.read_analog() < 20 and right_light.read_analog() < 20:
        radio.send('time')
        left_wheel(0)
        right_wheel(0)
    
