from microbit import *
import radio

radio.on()
radio.config(channel = 41)

start_time = 0
finish_time = 0
score = 0
pressed = 0
prev_time = 0
race_going = 0
while True:
    if button_a.is_pressed() == 1 and pressed == 0:
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(1000)
        display.show("1")
        sleep(1000)
        radio.send("start")
        start_time = running_time()
        display.scroll("GO!", wait = False, loop = False)
        pressed = 1
        race_going = 1

    msg = radio.receive()
    if msg:
        if msg == "time" and race_going == 1:
            finish_time = running_time()
            score = finish_time - start_time
            print(score)
            score = score//100
            score = score/10
            display.scroll("time = " + str(score) + " s", wait = True)
            race_going = 0
            pressed = 0
