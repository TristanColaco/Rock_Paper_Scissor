
print("Let's play Rock, Paper, Scissor")

test_cases = {
    1: ("rock", "paper"),
    2: ("rock", "scissor"),
    3: ("rock", "rock"),
    4: ("paper", "paper"),
    5: ("paper", "scissor"),
    6: ("paper", "rock"),
    7: ("scissor", "rock"),
    8: ("scissor", "paper"),
    9: ("scissor", "scissor")
}

for key, (player, computer) in test_cases.items():
    print(f"---Test Cases #{key}---")
    print(f" Player chooses: {player} & Computer chooses: {computer}")

    player_choice = player
    computer_choice = computer

    #if player chooses rock
    if player_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        elif computer_choice == "scissor":
            print("You win!")
        else:
            print("Its a tie!")

    #if player chooses paper
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        elif computer_choice == "scissor":
            print("You lose!")
        else:
            print("Its a tie!")

    #if player chooses scissor
    elif player_choice == "scissor":
        if computer_choice == "paper":
            print("You win!")
        elif computer_choice == "rock":
            print("You lose!")
        else:
            print("Its a tie!")

print("Thank you for playing!!!")
