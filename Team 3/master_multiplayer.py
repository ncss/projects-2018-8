from microbit import *
import radio

# Button and timer variables
DBLCLICK_TIME = 50
dblclick_timer = 0
a_pressed = False
b_pressed = False
ab_pressed = False
a_was_pressed = False
b_was_pressed = False

# Master variables
question_asked = False


class Player:
    START_POINTS = 30000 # The number of points (in ms) the player begins with
    INCORRECT_PENALTY = 5000 # The amount of points (in ms) subtracted due to a wrong answer

    def __init__(self):
        self.points = Player.START_POINTS
        self.questions_correct = 0


# Define a function that gets the wrong answer
def not_answer(answer):
    if answer == "true":
        return "false"
    return "true"


# Multiplayer variables
MIN_PLAYERS = 1
MAX_PLAYERS = 5
getting_players = True
num_players = 1
current_player = 0

# Setup the radio
GAME_CHANNEL = 49
radio.config(channel = GAME_CHANNEL, power = 7)
radio.on()

# Scroll a message only once
display.scroll("Number of players:", wait=False)

previous_time = running_time()
while True:
    # Get time since the start of the last tick
    current_time = running_time()
    time_elapsed = current_time - previous_time
    previous_time = current_time
    
    # Ensure that all presses only register for one tick
    if a_pressed:
        a_pressed = False
    if b_pressed:
        b_pressed = False
    if ab_pressed:
        ab_pressed = False
    # Get button states
    if button_a.was_pressed(): # set a timer when a or b is pressed; if the other is pressed in that time, set ab_pressed = True (register this as a double press)
        a_was_pressed = True
        dblclick_timer = DBLCLICK_TIME
    if button_b.was_pressed():
        b_was_pressed = True
        dblclick_timer = DBLCLICK_TIME
    if a_was_pressed or b_was_pressed: # tick down the timer if a or b was pressed
        dblclick_timer -= time_elapsed
        if a_was_pressed and b_was_pressed:
            ab_pressed = True
            a_was_pressed = False
            b_was_pressed = False
        elif dblclick_timer <= 0:
            a_pressed = a_was_pressed
            b_pressed = b_was_pressed
            a_was_pressed = False
            b_was_pressed = False
        display.clear()

    # This is the actual code (do not change anything above this while merging)
    if getting_players:
        if a_pressed:
            num_players -= 1
            if num_players < MIN_PLAYERS:
                num_players = MIN_PLAYERS
        if b_pressed:
            num_players += 1
            if num_players > MAX_PLAYERS:
                num_players = MAX_PLAYERS
        if ab_pressed:
            players = [Player() for _ in range(num_players)]
            display.scroll("Player 0 turn")
            getting_players = False
        else:
            display.show(str(num_players))
    else:
        # Sets correct answer based on button pressed
        if a_pressed:
            answer = "true"
            question_asked = True
        if b_pressed:
            answer = "false"
            question_asked = True
        # Checks for incoming answer
        incoming = radio.receive()
        print(incoming)
        if question_asked:
            if incoming == "tof:" + answer or incoming == "tof:" + not_answer(answer):
                if incoming == "tof:" + answer:
                    players[current_player].questions_correct += 1
                else:
                    players[current_player].points -= INCORRECT_PENALTY
                question_asked = False
                display.scroll("Player {} Score: {}".format(current_player, players[current_player].points))
                radio.send("tof:" + answer + "-answer")
                current_player = (current_player + 1) % len(players)
                display.scroll("Player {} turn".format(current_player))
            else:
                players[current_player].points -= time_elapsed
        
        if players[current_player].points <= 0:
            display.scroll("Player {} Game over! {} questions answered correctly!".format(current_player, questions_answered))
            question_asked = False