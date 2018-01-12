# README!
# change the payload variable to change the text it 
# transmits when the A button is pressed

from microbit import *
import radio

payload = '>'

radio.on()
radio.config(channel=51)
while True:
    if button_a.was_pressed():
        radio.send(payload)
        display.show(Image.PACMAN)
        sleep(1000)
        display.clear()
    display.show(payload)