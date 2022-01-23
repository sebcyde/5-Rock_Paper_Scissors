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
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)


    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("Computer chose scissors, you win!")
        
    
    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("Computer chose rock, you win!")
        
        
    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("Computer chose paper, you win!")
        

    elif user_input == computer_pick:
        print("It's a tie! Try again")

    else:
        computer_wins += 1
        print("You Lose")

print("Your score is", user_wins, "wins and", computer_wins, "losses.")
print("Goodbye!")
