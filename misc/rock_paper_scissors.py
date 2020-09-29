
# https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
from random import randint

# Create a list of play options
opt = ["Rock", "Paper", "Scissors", "Spock"]

# Assign a random play to the computer
computer = opt[randint(0,3)]

# Set player to False
player = False

while player == False:
    # Set player to True
    player = input(f"Rock, Paper, Scissors, Spock?")
    if player == computer:
        print("Tie!")
    elif player == "Spock":
        print(f"You win! {player} is more logical than {computer}.")
    elif computer == "Spock":
        print(f"You lose...{computer} is more logical than {player}.")
    else:
        print(f"Working on that, {player} and {computer}.")
    player = False
    computer = opt[randint(0,2)]
