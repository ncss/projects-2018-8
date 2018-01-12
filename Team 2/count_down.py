from microbit import *
import radio
import random
radio.on()
radio.config(channel=43)

activity = ['jump', 'duck', 'left', 'right']

wait = 2000
level = 1
lives = 3
curr_round = 1

while lives > 0:
    count_down = 0
    if level > 5:
        count_down += random.int(
    else:
        count_down += random.randint(4,6)-level
    
    for i in range(count_down, 0, -1):
        print(i)
        sleep(999)
    
    to_do = random.choice(activity[:level])
    print(to_do)

    for i in range(wait):
        action = radio.receive()
        '''if action != to_do:
            lives -= 1'''
            
    if curr_round == 5:
        print('new level')
        level += 1
        curr_round = 0
    else:
        curr_round += 1
        
print('you lose')