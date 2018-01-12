# Things to add:
# what happens when POINTS <= 0 (remember the less than because you are potentially subtracting more than 1 each tick)

from microbit import *
import radio
# MASTER
GAME_CHANNEL = 49
INCORRECT_PENALTY = 5000    # The amount of points (in ms) subtracted due to a wrong answer.
POINTS = 50000     # The amount of points (in ms) the player begins with.
radio.on()
radio.config(channel = GAME_CHANNEL)
question_asked = False
while True:
    # Initialises timer & sets correct answer.
    if button_a.was_pressed():
        answer = "true"
        start_time = running_time()
        question_asked = True
    if button_b.was_pressed():
        answer = "false"
        start_time = running_time()
        question_asked = True
    # Checks for incoming answer, checks if answer is correct, subtracts points based on time elapsed and INCORRECT_PENALTY.
    print(question_asked, POINTS)
    if question_asked:
        incoming = radio.receive()
        if incoming and incoming.startswith("tf:"):
            if incoming != "tf:" + answer:
                POINTS -= INCORRECT_PENALTY
            question_asked = False
            radio.send("tf:" + answer)
        if question_asked:
            end_time = running_time()
            elapsed_time = end_time - start_time
            start_time = end_time
            POINTS -= elapsed_time