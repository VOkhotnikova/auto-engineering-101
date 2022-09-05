""" If the user gets to 20 before 5 rolls, end the game - they won!
    if they are greater than or less than 20 spaces - they lose!
    Remember there are only 20 spaces on the board so a message like
    'You advanced to space 22' is a bug!

    example:
    Roll 1: you rolled a 3. You are now on space 3 and have 17 more to go
    Roll 2: you rolled a 3. You are now on space 6 and have 14 more to go
    Roll 3: you rolled a 3. You are now on space 9 and have 11 more to go
    Roll 4: you rolled a 5. You are now on space 14 and have 6 more to go
    Roll 5: you rolled a 6. You are now on space 20. Congrats, you win!
"""

import random


# roll the dice for a user (a randomly generated number between 1 and 6)
def dice():
    return random.randint(1, 6)


# # advance the user that many spaces on the game board
# def moving(steps, position=0):
#     position += steps
#     return position


# after each roll tell the user which space they are on and how many spaces they need to go to win
def message(j, steps, position):
    if position == 20:
        return f'Roll {j}: you rolled a {steps}. You are now on space {position}. Congrats, you win!'
    elif position < 20 and j < 5:
        return f'Roll {j}: you rolled a {steps}. You are now on space {position} and have {20 - position} more to go'
    elif position < 20 and j == 5:
        return f'Roll {j}: you rolled a {steps}. You are now on space {position}. You lose with {20 - position} to go'
    else:
        return f'Roll {j}: you rolled a {steps}. You lose and out of field'


# repeat this 4 additional times for 5 rolls in total
if __name__ == '__main__':
    pos = 0
    for i in range(1, 6):
        step = dice()
        pos += step
        print(message(i, step, pos))
        # input()
