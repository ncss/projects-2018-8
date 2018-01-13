from microbit import *
import radio

radio.on()
radio.config(channel=41)

left_back = pin16
left_forward = pin0
right_back = pin12
right_forward = pin8
left_light = pin1
right_light = pin2
sense_num = 0
game_start = 0
light = 0

#controls left wheel, -ve speed is backward
#-1023 to 1023
def left_wheel(speed):
    if speed < 0 :
        left_forward.write_analog(0)
        left_back.write_analog(abs(speed))
    else:
        left_forward.write_analog(abs(speed))
        left_back.write_analog(0)

#controls right wheel, -ve speed is backward
#-1023 to 1023
def right_wheel(speed):
    if speed < 0 :
        right_forward.write_analog(0)
        right_back.write_analog(abs(speed))
    else:
        right_forward.write_analog(abs(speed))
        right_back.write_analog(0)

#maps sensor value to output value, where x is sensor value, 
#a->b is the range of sensor values, and c->d is the range of desired output values.
def map_to_range(value):
    initial_min, initial_max, new_min, new_max = 600, 800, 175, 1023
    #correct values outside range
    if value < initial_min:
        value = initial_min
    if value > initial_max:
        value = initial_max
    # Figure out how 'wide' each range is
    initial_span = initial_max - initial_min
    new_span = new_max - new_min

    # Convert the left range into a 0-1 range (float)
    scaled_value = (value - initial_min) / initial_span

    # Convert the 0-1 range into a value in the right range.
    return 1023 - (new_min + (scaled_value * new_span))
    
l_previous_speeds = [0]
r_previous_speeds = [0]
l_avg = 0
r_avg = 0
length = 2
while True:
    msg = radio.receive()
    if button_b.is_pressed() == 1:
        left_wheel(0)
        right_wheel(0)
        game_start = 0
    if msg:
        if msg == "start":
            game_start = 1
    if game_start == 1:
        if len(l_previous_speeds) == length:
            l_previous_speeds.pop(0)
        if len(r_previous_speeds) == length:
            r_previous_speeds.pop(0)
        if msg:
            print("message", msg)
            if msg.startswith("r"):
                r_previous_speeds.append(map_to_range(int(msg[1:])))
            elif msg.startswith('l'):
                l_previous_speeds.append(map_to_range(int(msg[1:])))
        else:
            l_previous_speeds.append(max(0, max(l_previous_speeds)-1))
            r_previous_speeds.append(max(0, max(r_previous_speeds)-1))
        l_avg = sum(l_previous_speeds)/len(l_previous_speeds)
        r_avg = sum(r_previous_speeds)/len(r_previous_speeds)
        left_wheel(l_avg + 100)
        right_wheel(r_avg + 100)

        light = left_light.read_analog()
        if  light < 20:
            radio.send('time')
            left_wheel(0)
            right_wheel(0)
            game_start = 0
