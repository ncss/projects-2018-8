from microbit import *
import radio

radio.on()
radio.config(channel = 41)

left_sense = pin1
right_sense = pin2
sense_num = 0

while True:
    sensor = left_sense.read_analog()
    if sensor < 20:
        sense_num += 1
        if sense_num == 1:
            radio.send("start")
        if sense_num == 2:
            radio.send("end")