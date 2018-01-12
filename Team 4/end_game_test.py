from microbit import *
import radio

radio.on()
radio.config(channel = 41)

left_sense = pin1
right_sense = pin2

while True:
    sensor = left_sense.read_analog()
    if sensor < 20:
       radio.send("time")
