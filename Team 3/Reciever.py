from microbit import *
import radio
radio.on()
GAME_CHANNEL = 49
radio.config(channel = GAME_CHANNEL)
image_time = 0
while True:
    incoming_string = radio.receive()
    if incoming_string:
        if incoming_string == "f":
            last_location = incoming_string
            image_time = 200
        if incoming_string == "t":
            last_location = incoming_string
            image_time = 200

    if image_time > 0:
        display.show(Image.HAPPY)
        image_time -= 1
    if image_time == 0:
        display.clear()