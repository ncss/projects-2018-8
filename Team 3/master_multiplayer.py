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
UPDATE_SCORE_RATE = 500
update_score_timer = UPDATE_SCORE_RATE
question_asked = False


class Player:
    START_POINTS = 10000 # The number of points (in ms) the player begins with
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
            display.scroll("1")
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
        if question_asked:
            if incoming == "tof:" + answer or incoming == "tof:" + not_answer(answer):
                if incoming == "tof:" + answer:
                    players[current_player].questions_correct += 1
                else:
                    players[current_player].points -= Player.INCORRECT_PENALTY
                question_asked = False
                radio.send("tof:" + answer + "-answer")
                display.scroll(": {}".format(players[current_player].points))
                if players[current_player].points <= 0:
                    players[current_player].points = 0
                    display.scroll("{} Game over! {} questions!".format(current_player, players[current_player].questions_correct))
                    question_asked = False
                    if num_players <= 2:
                        getting_players = True
                        current_player = 0
                        if num_players == 2:
                            display.scroll("{} wins!".format(2 - current_player)) # this just happens to display the right thing (0 -> player 2 wins, 1 -> player 1 wins)
                    else:
                        alive_player = -1
                        # loop through the players
                        for player_index in range(num_players):
                            if players[player_index].points > 0:
                                if alive_player == -1: # we have found an alive player
                                    alive_player = player_index
                                else: # we already have an alive player, so we have concluded that at least two players are still alive
                                    break
                        else: # putting 'else' at the end of a 'for loop' means the following indented code will run if the for loop finished naturally (i.e. was not 'break'd out of)
                            # If this code runs, there is one player still alive
                            display.scroll("{} wins!".format(alive_player + 1))
                            getting_players = True
                            current_player = 0
                if not getting_players:
                    current_player = (current_player + 1) % len(players)
            else:
                players[current_player].points -= time_elapsed

        display.show(str(current_player + 1))
        update_score_timer -= time_elapsed
        if update_score_timer <= 0:
            update_score_timer = UPDATE_SCORE_RATE
            radio.send("score:{}".format(players[current_player]))