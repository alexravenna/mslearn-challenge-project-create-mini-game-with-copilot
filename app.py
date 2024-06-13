import random

play_again = "yes"
user_score = 0
nr_rounds = 0

while play_again == "yes":
    user_input = ""
    
    # accept user input that can be one of the following: Rock, paper, scissors
    while user_input not in ["rock", "paper", "scissors"]:
        user_input = input("Enter your choice (rock, paper, scissors): ")

        # # check if the user input is one of the following: Rock, paper, scissors
        if user_input in ["rock", "paper", "scissors"]:
            # continue with the game logic
            pass
        else:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

    nr_rounds += 1

    # generate a random choice from the computer that can be one of the following: rock, paper, scissors
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    # compare the user input to the computer input
    # if the user input is the same as the computer input, it's a tie
    if user_input == computer_choice:
        print("It's a tie!")

    # if the user input is rock and the computer input is scissors, the user wins and the user score is incremented by 1
    elif user_input == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
        user_score += 1
    # if the user input is paper and the computer input is rock, the user wins
    elif user_input == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
        user_score += 1
    # if the user input is scissors and the computer input is paper, the user wins
    elif user_input == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")
        user_score += 1
    # if the computer input is scissors and the user input is paper, the computer wins
    elif computer_choice == "scissors" and user_input == "paper":
        print("You lose! Scissors beats paper.")
    # if the computer input is paper and the user input is rock, the computer wins
    elif computer_choice == "paper" and user_input == "rock":
        print("You lose! Paper beats rock.")
    # if the computer input is rock and the user input is scissors, the computer wins
    elif computer_choice == "rock" and user_input == "scissors":
        print("You lose! Rock beats scissors.")

    # print the computer choice
    print(f"Computer choice: {computer_choice}")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    if play_again != "yes":
        print(f"Your score after {nr_rounds}: {user_score}\n")
        print("Thanks for playing!")