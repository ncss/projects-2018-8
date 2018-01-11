from microbit import *

prevTime = 0;
time = 0;
print("FISH")
while True:
  if accelerometer.was_gesture("shake"):
    time = running_time() - prevTime
    print(time)
    prevTime = running_time()  

