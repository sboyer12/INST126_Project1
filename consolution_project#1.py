# consolidation project #1

import os
import random

#this is the start of the function where we see how many players are going
players = input("How many people are playing? \n")
if players == 1:
    single_player = input("What is your name? \n")
elif players == 2:
    player1 = input("What is player ones name? \n")
    player2 = input("What is player twos name? \n")
elif players > 2:
    print("Only two players at most please start over.")

die_sides = (1, 2, 3, 4, 5, 6)
random.choice(die_sides)
