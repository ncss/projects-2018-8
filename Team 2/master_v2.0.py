from microbit import *
import radio
import random
import music

#radio configurations
radio.on()
radio.config(channel = 43)
start_signal = '1'   
end_signal = '0'

#game constants
GAME_STATE = False
place_holder = Image("99999:99999:99999:99999:99999")
action_list = ['JUMP', 'DUCK']
action_images = {'JUMP': Image.ARROW_N, 'DUCK': Image.ARROW_S}
count_time = 5
wait_time = 2000 
sleep_time = 1000

#game stats
lives = 3
level = 1
score = 0

def start_sequence ():
    for i in range(3):
        display.show(place_holder, wait=True)
        sleep(1000)
        display.clear()
        sleep(200)

def reset_game ():
    start_sequence()
    display.show('START', wait=True, loop=False, clear=True)
    sleep(1000)

while True:
    if button_a.was_pressed():
        lives = 3
        level = 1
        score = 0
        reset_game()   
        GAME_STATE = True
        
    while lives > 0 and GAME_STATE == True:
        for i in range(count_time):
            display.show(str(count_time - i))
            sleep(1000)
            display.clear()
        
        radio.send(start_signal)
        start_time = running_time()
        action_complete = False
        action_to_do = random.choice(action_list)
        display.show(action_images[action_to_do], wait=False)
        while running_time() - start_time < wait_time:
            action_made = radio.receive()
            if action_made == action_to_do or button_b.was_pressed():
                action_complete = True
                
        radio.send(end_signal)
        
        if action_complete == True:
            score += 1
            music.play(music.BA_DING)
        else:
            #music.play(['G1:2','C'])
            lives -= 1
            
        if lives == 0:
            GAME_STATE = False
            #music.play(music.WAWAWAWAA)
            display.show(str(score))
        '''else:
            start_time = running_time()
            display.show(place_holder, wait=False)
            i = 0
            while running_time - start_time < sleep_time:
                if (running_time - start_time) % (sleep_time / 5) == 0:
                    i += 1
                    display.clear()
                    display.show(place_holder.shift_left(i), wait=False)'''