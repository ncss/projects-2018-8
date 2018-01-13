from microbit import*
import radio
from neopixel import NeoPixel
import random

radio.on()
radio.config(channel = 51, address=0x77696c6c)

start_speed = 200    

lefty_speed = pin0
lefty_dir = pin8
righty_speed = pin1
righty_dir = pin12
turn_sleep = 400
current_speed = start_speed
speed_change = 100
pixels = NeoPixel(pin13, 12)

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
    HECK_STOP()
    
def HECK_STOP():
    lefty_speed.write_analog(0)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(0)
    righty_dir.write_digital(0)
    
    
def forward():
    run_motor_forward(left=current_speed+7,right=current_speed)

def backwards():
    run_motor_back(left=200,right=200)
    sleep(turn_sleep)
    HECK_STOP()
    
    
def run_motor_forward(left=0, right=0):
    if left < 0 or right < 0 or left >= 1024 or right >= 1024:
        raise Exception()
        
    lefty_speed.write_analog(left)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(right)
    righty_dir.write_digital(0)

def run_motor_back(left=0, right=0):
    if left < 0 or right < 0 or left >= 1024 or right >= 1024:
        raise Exception()
        
    lefty_speed.write_analog(left)
    lefty_dir.write_digital(1)
    righty_speed.write_analog(right)
    righty_dir.write_digital(1)
    
def get_color():
    # returns (0,0,0)
    return [random.randrange(80) for i in range(3)]
    
colors = [get_color() for i in range(12)]

def rainbow():
    for i, color in enumerate(colors):
        pixels[i] = tuple(color)
    pixels.show()
    colors.pop(0)
    colors.append(get_color())
    
    
    
before = 0
change_light_time = 300

rainbow()
stop = True
while True:
    now = running_time()
    if before+change_light_time < now:
        rainbow()
        before = running_time()
    
    left = pin11.read_digital()
    right = pin5.read_digital()
    msg = radio.receive()
    if msg:
        print('Receive message:', msg)
    
    
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
        
        if not left or not right:
            print("Entered!")
            display.show(Image.SWORD)
            backwards()
            forward()
            continue
        
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
    
    
    
    