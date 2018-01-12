# Import Modules
from microbit import *
import radio
# Set Radio
radio.on()
radio.config(channel = 41)
# Set Variables
prev_time = 0;
time = 0;
# Check Repl
print("FISH")
# Loop Program
while True:
    # Read Gesture
    if accelerometer.was_gesture("shake"):
        # Set Time Between Gestures
        time = running_time() - prev_time
        # Display And Send Time
        print(time)
        radio.send(str(time))
        # Reset Time 
        prev_time = running_time()  
