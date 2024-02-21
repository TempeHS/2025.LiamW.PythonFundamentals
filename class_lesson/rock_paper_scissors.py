def main():
    player_choice = input("Rock, Paper or Scissor: ")
    player_choice = player_choice.lower()
    computer_choice = generate_random()
    match player_choice:
        case "rock":
            match computer_choice:
                case "rock":
                    print("Tie")
                case "paper":
                    print("Lose")
                case "scissor":
                    print("Win!")
        case "paper":
            match computer_choice:
                case "rock":
                    print("Win!")
                case "paper":
                    print("Tie")
                case "scissor":
                    print("Lose")
        case "scissor":
            match computer_choice:
                case "rock":
                    print("Lose")
                case "paper":
                    print("Win!")
                case "scissor":
                    print("Tie")
        case _:


def generate_random():
    return()


main()