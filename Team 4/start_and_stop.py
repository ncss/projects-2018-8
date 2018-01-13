from microbit import *
import radio

radio.on()
radio.config(channel = 41)

start_time = 0
finish_time = 0
score = 0

while True:
    if radio.receive() == "start":
        print("start")
        start_time = running_time()
        
    if radio.receive() == "end":
        finish_time = running_time()
        score = finish_time - start_time
        score = score//100
        score = score/10
        print(score)
