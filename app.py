# create a game of rock, paper, scissors using Python and help from Github Copilot

import random

# 1. get the user's choice
user_choice = input("Do you want to play rock, paper, scissors? (y/n) ")
# if choice is invalid, keep asking until valid input is given
while user_choice not in ["y", "n"]:
    user_choice = input("Invalid input. Please choose y or n: ")
# initialize score for computer and user
computer_score = 0
user_score = 0
while user_choice == "y":
    user_choice = input("Choose rock, paper, or scissors: ")
    # transform user input into lowercase
    user_choice = user_choice.lower()
    # if input is invalid, keep asking until valid input is given
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid input. Please choose rock, paper, or scissors: ")
        user_choice = user_choice.lower()
# 2. get the computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print("The computer chose", computer_choice)
    # 3. compare the two choices and decide who wins
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
            user_score += 1
        else:
            print("The computer wins!")
            computer_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
            user_score += 1
        else:
            print("The computer wins!")
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
            user_score += 1
        else:
            print("The computer wins!")
            computer_score += 1
    # 5. ask the user if they want to play again
    user_choice = input("Do you want to play again? (y/n) ")
    # if choice is invalid, keep asking until valid input is given
    while user_choice not in ["y", "n"]:
        user_choice = input("Invalid input. Please choose y or n: ")
    # if user choice is no, print the final score
    if user_choice == "n":
        print("-------------------------")
        print("Final score: ")
        print("Computer:", computer_score)
        print("User:", user_score)
        # print who won the game
        if computer_score > user_score:
            print("The computer won the game!")
        elif computer_score < user_score:
            print("You won the game!")
        else:
            print("It's a tie!")
        print("-------------------------")
        break
