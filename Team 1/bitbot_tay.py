from microbit import*
import radio
radio.on()
radio.config(channel = 51)

lefty_speed = pin0
lefty_dir = pin8
righty_speed = pin1
righty_dir = pin12
turn_sleep = 210

def left():
    lefty_speed.write_digital(1)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(0)
    righty_dir.write_digital(0)
    sleep(turn_sleep)
    
def right():
    lefty_speed.write_digital(1)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(0)
    righty_dir.write_digital(0)
    sleep(turn_sleep)
    
def HECK_STOP():
    righty_speed.write_digital(0)
    righty_dir.write_digital(0)
    lefty_speed.write_digital(0)
    lefty_dir.write_digital(0)
    
def run_motor(left=0, right=0):
    if left < 0 or right < 0 or left >= 1024 or right >= 1024:
        raise Exception()
        
    lefty_speed.write_analog(left)
    lefty_dir.write_digital(0)
    righty_speed.write_analog(right)
    righty_dir.write_digital(0)

#while True:
    #run_motor(left=1023, right=1023)

'''
while True:
    sleep(5000)
    right()
    HECK_STOP()
    break
'''
while True:
    msg = radio.receive()
    if msg == '