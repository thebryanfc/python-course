import random
while True:
    choiches = ["rock", "paper", "scissors"]

    computer = random.choice(choiches)
    player = None

    while player not in choiches:
        player = input("rock, paper, or scissors? :").lower()

    if player == computer:
        print(f"Computer: {computer}")
        print(f"Player : {player}")
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player : {player}")
            print("You lose!")
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player : {player}")
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player : {player}")
            print("You lose!")
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player : {player}")
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player : {player}")
            print("You lose!")
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player : {player}")
            print("You win!")

    play_again = input(f"Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")