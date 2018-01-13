from microbit import *
import radio
radio.on()
radio.config(channel = 41)
    
while True:
    if button_a.was_pressed():
        radio.send('on/off')
    msg = radio.receive()
    high = 1500
    low = 500
    threshold = (high - low)/5
    if msg:
        msg = int(msg)
        if msg<low:
            msg = low
        if msg>high:
            msg = high
        msg -= low
        msg = high - msg
        print(msg)
        for i in range(msg/threshold):
            print('i:',i)
            for j in range(5):
                print('j',j)
                display.set_pixel(4-i,4-j,9)
        display.clear()
    