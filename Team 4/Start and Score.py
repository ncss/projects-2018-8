from microbit import *
import radio

radio.on()
radio.config(channel = 41)

start_time = 0
finish_time = 0
score = 0
prev_time = 0
race_going = 0
while True:
    if button_a.is_pressed() == 1:
        print("Pressed")
        start_time = running_time()
        race_going = 1
        
    if msg:
        if radio.recive == "TIME" and race_going == 1
            finish_time = running_time()
            score = finish_time - start_time
            print(score)
