print("Let's play Rock, Paper, Scissor")

game = 1
while game == 1:
    player_choice = str.lower(input("Please enter your choice --> "))
    computer_choice = "paper"

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

    game = int(input("Do you want to continue? Press 1 or else 0 to end --> "))

print("Thank you for playing!!!")