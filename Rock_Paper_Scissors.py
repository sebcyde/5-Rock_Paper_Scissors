import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # Rock:0 , Paper:1 , Scissors:2

    if user_input == options[0] and random_number == options[2]:
        print("Computer chose scissors, you win!")
    
    elif user_input == options[1] and random_number == options[0]:
        print("Computer chose rock, you win!")
        
    elif user_input == options[2] and random_number == options[1]:
        print("Computer chose paper, you win!")



print("Goodbye!")
