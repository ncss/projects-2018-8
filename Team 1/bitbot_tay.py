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

for i in range(12):
    pixels[i] = (0,0,0)
pixels.show()

def left():
    lefty_speed.write_analog(0)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(1023)
    righty_dir.write_digital(0)
    sleep(turn_sleep)
    HECK_STOP()
    
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
    lefty_speed.write_analog(current_speed)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(current_speed+7)
    righty_dir.write_digital(0)

def backwards():
    lefty_speed.write_analog(200)
    lefty_dir.write_digital(1)
    righty_speed.write_analog(200)
    righty_dir.write_digital(1)
    sleep(turn_sleep)
    HECK_STOP()
    
    
    
def get_color():
    # returns (0,0,0)
    return [random.randrange(10) for i in range(3)]
    
colors = [get_color() for i in range(12)]

def rainbow():
    return
    for i, color in enumerate(colors):
        pixels[i] = tuple(color)
    pixels.show()
   
    colors.append(colors.pop(0))
    
    
    
before = 0
change_light_time = 300


current_round_time = 0

rainbow()
stop = True
while True:
    now = running_time()
    if before+change_light_time < now:
        rainbow()
        before = running_time()
    
    left_line = pin11.read_digital()
    right_line = pin5.read_digital()
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
        if not left_line or not right_line:
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
    
    
    
    