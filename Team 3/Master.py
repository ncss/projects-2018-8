from microbit import *
import radio
# MASTER
GAME_CHANNEL = 49
INCORRECT_PENALTY = 5000    # The amount of points (in ms) subtracted due to a wrong answer.
START_POINTS = 60000 # The amount of points (in ms) the player begins with.
points = START_POINTS
radio.on()
radio.config(channel = GAME_CHANNEL, power = 7)
question_asked = False
questions_answered = 0

display.scroll("start", wait=False)

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
    incoming = radio.receive()
    if question_asked:
        if incoming and incoming.startswith("tof:"):
            if incoming == "tof:" + answer:
                questions_answered += 1
            else:
                points -= INCORRECT_PENALTY
            question_asked = False
            display.scroll("Score: {}".format(points), wait=False)
            radio.send("tof:" + answer + "-answer")
        else:
            end_time = running_time()
            elapsed_time = end_time - start_time
            start_time = end_time
            points -= elapsed_time
    
    if points <= 0:
        display.scroll("Game over! {} questions answered correctly!".format(questions_answered))
        questions_answered = 0
        points = START_POINTS
        question_asked = False