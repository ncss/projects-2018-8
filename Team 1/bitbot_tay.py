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
    
    
   
   
    
before = 0
change_light_time = 300




current_before_time = 0

ROUND_TIME = 60

current_round_time = ROUND_TIME * 1000

def convert_milli_to_display(millis):
    secs = millis // 1000
    mins = secs // 60
    secs %= 60
    return "{:02}{:02}".format(mins,secs)

for i in range(12):
    pixels[i] = (random.randrange(10),random.randrange(10),random.randrange(10))
pixels.show()

stop = True
while True:
    now = running_time()
    
    
    left_line = pin11.read_digital()
    right_line = pin5.read_digital()
    msg = radio.receive()
    
    
    if msg:
        print('Receive message:', msg)
    
    if msg == 'G':
        forward()
        stop = False
        current_speed = start_speed 
        
    if msg == 'E':
        print("reseting!")
        current_speed = start_speed 
        stop = True
        current_round_time = ROUND_TIME * 1000
        HECK_STOP()
        
            
    if msg == 'S':
        HECK_STOP()
        stop = True
        current_speed = start_speed
            
    if stop:
        # the robit is in stop mode
        display.show(Image.SAD)
        
    else: 
        if before+change_light_time < now:
            # current round time is round time in milliseconds
            current_round_time -= change_light_time
            print("Time=", current_round_time)
            msg2 = "B" + convert_milli_to_display(current_round_time)
            radio.send(msg2)
            print(msg2)
            
            
            before = running_time()
            
        
        
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
            current_speed = min(current_speed + speed_change, 1015)
            forward()
    
    
    
    