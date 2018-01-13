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
def left_wheel(speed):
    if speed < 0 :
        left_forward.write_analog(0)
        left_back.write_analog(abs(speed))
    else:
        left_forward.write_analog(abs(speed))
        left_back.write_analog(0)

#controls right wheel, -ve speed is backward
def right_wheel(speed):
    if speed < 0 :
        right_forward.write_analog(0)
        right_back.write_analog(abs(speed))
    else:
        right_forward.write_analog(speed)
        right_back.write_analog(0)

#maps sensor value to output value, where x is sensor value, 
#a->b is the range of sensor values, and c->d is the range of desired output values.
def map_to_range(value):
    initial_min, initial_max, new_min, new_max = 600, 800, 175, 1023
    #correct values outside range
    if value < initial_min:
        value = inital_min
    if value > initial_max:
        value = initial_max
    # Figure out how 'wide' each range is
    initial_span = initial_max - initial_min
    new_span = new_max - new_min

    # Convert the left range into a 0-1 range (float)
    scaled_value = (value - initial_min) / initial_span

    # Convert the 0-1 range into a value in the right range.
    return 1023 - (new_min + (scaled_value * new_span))
    
    
l_previous_speeds = [150]
r_previous_speeds = [150]
l_avg = 0
r_avg = 0
length = 2
while True:
    msg = radio.receive()
   # print(msg)
    if button_b.is_pressed() == 1:
        left_wheel(0)
        right_wheel(0)
        game_start = 0
    if msg:
        if msg == "start":
            game_start = 1
    if game_start ==1:    
        if len(l_previous_speeds) == length:
            l_previous_speeds.pop(0)
        if len(r_previous_speeds) == length:
            r_previous_speeds.pop(0)
        if msg:
            if msg.startswith("r"):
                r_previous_speeds.append(map_to_range(int(msg[1:]))+300)
                display.show(Image.CHESSBOARD)
            elif msg.startswith('l'):
                l_previous_speeds.append(map_to_range(int(msg[1:]))+300)
                display.show(Image.CHESSBOARD)
        else:
            l_previous_speeds.append(l_avg-4)
            r_previous_speeds.append(r_avg-4)
            display.clear()
        l_avg = sum(l_previous_speeds)/len(l_previous_speeds)
        r_avg = sum(r_previous_speeds)/len(r_previous_speeds)
        if l_avg < 0:
            l_avg = 0
        if r_avg < 0:
            r_avg = 0
        left_wheel(l_avg)
        right_wheel(r_avg)
        
        print('speeds:', l_avg, r_avg)
        
        light = left_light.read_analog()
        print(light)
        if  light < 20:
            radio.send('time')
            left_wheel(0)
            right_wheel(0)
            game_start = 0

        
