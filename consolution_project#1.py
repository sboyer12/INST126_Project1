# consolidation project #1


"""
“Tuple Out” Dice Game

For this project, you will implement a simulation of a simple dice game with the following rules:
• This game may have one or more players.
• The object of the game is to score the most points, or to be the first to reach a certain score.
• Players take turns rolling dice to score points, as described below.
• Each turn, the active player rolls three dice:
– If all three dice are rolled with the same number, the player has “tupled out”, and ends their
turn with zero points. (For example, rolling three “4”s at the same time.)
– If two dice have the same value, they are “fixed”, and they cannot be re-rolled.
– The player can re-roll any dice that are not “fixed”, as often as they would like, until they
decide to stop, or until they “tuple out” (get three of the same number).
• When a player decides to stop, they score points equal to the total of the three dice, and then
their turn ends.
• If a player “tuples out”, their turn ends and they score 0 points for that turn.
 """


# importing the different packages that I will need to utilize for this game.
import os
import random

# this is how we view our dice
die1_sides = (1, 2, 3, 4, 5, 6)

die2_sides = (1, 2, 3, 4, 5, 6)

die3_sides = (1, 2, 3, 4, 5, 6)

# these are the functions for how we roll the dice
def roll1dice():
    return random.choice(die1_sides) + random.choice(die2_sides) + random.choice(die3_sides)
    
#def roll2dice():
    
#def roll3dice():
    

#this is the start of the function where we see how many players are going. I didn't like this one so I am not using it.
'''
players = input("How many people are playing? \n")
if players == 1:
    single_player = input("What is your name? \n")
elif players == 2:
    player1 = input("What is player ones name? \n")
    player2 = input("What is player twos name? \n")
elif players > 2:
    print("Only two players at most please start over.")
'''
# I am going to create a list of the players that want to play instead of using an if statement. This will make it more compact
players = []

print("Hello World! \n")   # this satisfies one of the points
print("welcome to the Tuple Out Dice Game!! \n") # intro to the game\

# this while statement allows me to take all players and put their names into the list
while True:
    name = input("Enter player names! Type 'done' to start the game: \n")

    if name.lower() == 'done':
        break

    players.append(name)

print(f"\n Number of players: {len(players)} \n") # len shows the length of the function. So it reads how many playesr are in our player list

input("Press Enter to Start the game.")

for name in players:
    print(f"\n{name} its your move!")
    points = 0
    while True:
        print("Press enter to continue\n")
        dice = roll1dice
        print(f"\n You rolled a {roll1dice}!")

        if points == [3, 6, 9, 12, 15, 18]:
            break
        else:
            points += sum(dice)
            print(f"\n you have {points} many points")



