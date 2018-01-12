from microbit import *
import radio
# MASTER
GAME_CHANNEL = 49
INCORRECT_PENALTY = 5000    # The amount of points (in ms) subtracted due to a wrong answer.
POINTS = 50000     # The amount of points (in ms) the player begins with.
radio.on()
radio.config(channel = GAME_CHANNEL)
answer = None
decrease_points = False
while True:
    # Initialises timer & sets correct answer.
    if button_a.was_pressed():
        answer = "true"
        start_time = running_time()
        decrease_points = True
    if button_b.was_pressed():
        answer = "false"
        start_time = running_time()
        decrease_points = True
    # Checks for incoming answer, checks if answer is correct, subtracts points based on time elapsed and INCORRECT_PENALTY.
    incoming = radio.receive()
    if incoming:
        if incoming == answer:
            radio.send(answer)
            decrease_points = False
        if incoming != answer:
            POINTS -= INCORRECT_PENALTY
            radio.send(answer)
            decrease_points = False
    if decrease_points:
        end_time = running_time()
        elapsed_time = end_time - start_time
        start_time = end_time
        POINTS -= elapsed_time
        print(POINTS)