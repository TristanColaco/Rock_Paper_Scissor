choice = ["rock", "paper", "scissor"]

test = {
    1: ("rock", "rock"),
    2: ("rock", "scissor"),
    3: ("rock", "rock"),
    4: ("paper", "paper"),
    5: ("paper", "scissor"),
    6: ("paper", "rock"),
    7: ("scissor", "rock"),
    8: ("scissor", "paper"),
    9: ("scissor", "scissor")
}

for key, (player, computer) in test.items():
    print(f"---Test Case #{key}--")
    print(f"Player chose: {player} & Computer chose: {computer}")

    player_choice = player
    computer_choice = computer

    player_index = choice.index(player_choice)
    computer_index = choice.index(computer_choice)

    if player_index == computer_index:
        print("Its a tie!!!")
    elif (player_index + 1) % 3 == computer_index:
        print("Computer Wins!!!")
    else:
        print("Player Wins!!!")