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

game_start = 0
light = 0

rightStop = 0
leftStop = 0

def left_wheel(speed):
    left_forward.write_analog(abs(speed))
    left_back.write_analog(0)

#controls right wheel, -ve speed is backward
#-1023 to 1023
def right_wheel(speed):
    right_forward.write_analog(abs(speed))
    right_back.write_analog(0)
    
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
        if msg:
            print(msg)
            if msg.startswith("r"):
                rightStop = running_time() + 500
            elif msg.startswith('l'):
                leftStop = running_time() + 500
                
        if rightStop >= running_time():
            right_wheel(1023)
        else:
            right_wheel(0)
            
        if leftStop >= running_time():
            left_wheel(1023)
        else:
            left_wheel(0)
        light = left_light.read_analog()
        
        if  light < 20:
            radio.send('time')
            left_wheel(0)
            right_wheel(0)
            game_start = 0