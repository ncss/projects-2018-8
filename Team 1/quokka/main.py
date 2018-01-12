# README!
# scrolls stuff on the microbit when recieved on channel 51
from quokka import *
neopixels.all(0,0,0)
neopixels.show()

radio.config(channel=51)
queue = []
clear_time = 0
def queue_text(char):
	queue.append(char)
	
while True:
    msg = radio.receive()
    now = running_time()
    if clear_time < now:
        display.fill(0)
        display.show()
    '''
    if msg:
        display.text(msg, 0,0, 1)
        display.show()
        sleep(1000)
    '''
    if buttons.a.was_pressed():
        radio.send("G")
        display.text("GO", 0, 0, 1)
        display.show()
        print("GOHI!!")
        sleep(1000)
	
	# button b is hooked up to D for some reason
    if buttons.d.was_pressed():
        radio.send("S")
        display.text("STOP", 0, 0, 1)
        display.show()
        print("HI!")
        sleep(1000)
    
		
		
        
    