# README!
# scrolls stuff on the microbit when recieved on channel 51
'''
from quokka import *
neopixels.all(0,0,0)
neopixels.show()
'''
from microbit import *
import radio


radio.on()
radio.config(channel=51,address=0x77696c6c)

	
while True:
    msg = radio.receive()
    display.show("@")
   
   
    if button_a.was_pressed():
        radio.send("G")
        display.scroll("GO", wait=False)
        print("GOHI!!")
        sleep(1000)
	
	# button b is hooked up to D for some reason
    if button_b.was_pressed():
        radio.send("S")
        display.scroll("STOP", wait=False)
        print("HI!")
        sleep(1000)
    
		
		
        
    