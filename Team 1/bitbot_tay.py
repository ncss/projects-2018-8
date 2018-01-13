from microbit import*
import radio
radio.on()
radio.config(channel = 51, address=0x77696c6c)
start_speed = 300    

lefty_speed = pin0
lefty_dir = pin8
righty_speed = pin1
righty_dir = pin12
turn_sleep = 400
current_speed = start_speed
speed_change = 100


def left():
    lefty_speed.write_analog(0)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(1023)
    righty_dir.write_digital(0)
    sleep(turn_sleep)
    run_motor()
    
def right():
    lefty_speed.write_analog(1023)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(0)
    righty_dir.write_digital(0)
    sleep(turn_sleep+40)
    run_motor()
    
def HECK_STOP():
    righty_speed.write_analog(0)
    righty_dir.write_digital(0)
    lefty_speed.write_analog(0)
    lefty_dir.write_digital(0)
    
def forward():
    righty_speed.write_analog(current_speed)
    righty_dir.write_digital(0)
    lefty_speed.write_analog(current_speed+7)
    lefty_dir.write_digital(0)
    
    
def run_motor(left=0, right=0):
    if left < 0 or right < 0 or left >= 1024 or right >= 1024:
        raise Exception()
        
    lefty_speed.write_analog(left)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(right)
    righty_dir.write_digital(0)

stop = True
while True:
    msg = radio.receive()
    if msg == 'G':
        forward()
        stop = False
        current_speed = start_speed
            
    if msg == 'S':
        HECK_STOP()
        stop = True
        current_speed = start_speed
            
    if stop:
        # the robit is in stop mode
        display.show(Image.SAD)
        
    else:
    
        display.show(Image.HAPPY)
        
        if msg == '<':
            left()
            forward()
            print('L')
        if msg == '>':
            right()
            forward()
            print('R')
        if msg == '-':
            current_speed = max(current_speed - speed_change, 0)
            forward()
        if msg == '+':
            current_speed = min(current_speed + speed_change, 1023)
        forward()
    
    
    
    
    