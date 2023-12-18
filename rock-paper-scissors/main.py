import random

game_list = ["Rock", "Paper", "Scissors"] 

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
random_number = random.randint(0, 2)

if player_input == 0:
    if random_number == 0:
        print("You played: Rock! - Enemy played: Rock!")
        print("It's a Draw!")
    elif random_number == 1:
        print("You played: Rock! - Enemy played: Paper!")
        print("You Lose!")
    elif random_number == 2:
        print("You played: Rock! - Enemy played: Scissors!")
        print("You Win!")
elif player_input == 1:
    if random_number == 0:
        print("You played: Paper! - Enemy played: Rock!")
        print("You Win!")
    elif random_number == 1:
        print("You played: Paper! - Enemy played: Paper!")
        print("It's a Draw!")
    elif random_number == 2:
        print("You played: Paper! - Enemy played: Scissors!")
        print("You Lose!")
elif player_input == 2:
    if random_number == 0:
        print("You played: Scissors! - Enemy played: Rock!")
        print("You Lose!")
    elif random_number == 1:
        print("You played: Scissors! - Enemy played: Paper!")
        print("You Win!")
    elif random_number == 2:
        print("You played: Scissors! - Enemy played: Scissors!")
        print("It's a Draw!")
else:
    print("Invalid input!")