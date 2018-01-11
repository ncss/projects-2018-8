from microbit import *
import radio
radio.on()
radio.config(channel = 41)
prev_time = 0;
time = 0;
print("FISH")
while True:
  if accelerometer.was_gesture("shake"):
    time = running_time() - prevTime
    radio.send(str(time))
    print(time)
    prevTime = running_time()  

