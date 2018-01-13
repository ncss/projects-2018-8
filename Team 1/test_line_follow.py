from microbit import *
import radio
radio.on()
radio.config(channel=47)

while True:
    pin16.write_digital(0)
    left = pin11.read_digital()
    right = pin5.read_digital()
    print('left', left, 'right', right)
    x = "sensor1=" + str(pin2.read_analog())
    radio.send(x)
    print(x)
    pin16.write_digital(1)
    x = "sensor2=" + str(pin2.read_analog())
    radio.send(x)
    print(x)
    sleep(1000)