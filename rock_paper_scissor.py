#Rock-paper-scissor game:The Rock-Paper-Scissors game is a simple Python project that mimics the classic hand game played between two participants. 
# In the Python version, the user plays against the computer, which randomly selects a choice.
#The game logic determines the winner based on these rules:
#                 Rock beats Scissors
#                 Scissors beats Paper
#                 Paper beats Rock
#The result is displayed (Win, Lose, or Draw).

import random
options=["rock","paper","scissors"]

while True:
    player=None
    computer=random.choice(options)
    
    while player not in options:
        player=input("Enter your choice(rock,paper,scissor): ")
    print(f"player:{player}")
    print(f"computer:{computer}")      
    if player==computer:
            print("Its a tie!")
    elif player=="rock" and computer=="scissors":
            print("You win!")
    elif player=="paper" and computer=="rock":
            print("You win!")
    elif player=="scissors" and computer=="paper":
            print("You win!")
    else:
            print("You lose!")
    if not input("Do you want to play again? (y/n):").lower()=="y":
            break

print("Thanks for playing!")
    

    

