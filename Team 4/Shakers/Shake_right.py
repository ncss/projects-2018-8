# Import Modules
from microbit import *
import radio
# Set Radio
radio.on()
radio.config(channel = 41)
# Set Variables
prev_time = 0;
time = 0;
# Loop Program
while True:
    display.show("R")
    # Read Gesture
    if accelerometer.was_gesture("shake"):
        # Set Time Between Gestures
        time = running_time() - prev_time
        # Display And Send Time
        print(time)
        radio.send('r' + str(time))
        display.show(Image.HAPPY)
        sleep(100)
        # Reset Time  
        prev_time = running_time()  
        display.clear()

