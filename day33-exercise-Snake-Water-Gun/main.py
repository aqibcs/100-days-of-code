import random


def get_computer_choice():
    """Randomly selects between 'snake', 'water', and 'gun' for the computer."""
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)


def get_user_choice():
    """Prompts the user to enter their choice."""
    while True:
        user_choice = input("Enter your choice (snake/water/gun): ").lower().strip()
        if user_choice in ['snake', 'water', 'gun']:
            return user_choice
        else:
            print("Invalid choice. Please choose either 'snake', 'water', or 'gun'.")


def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
            (user_choice == 'water' and computer_choice == 'gun') or \
            (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """Plays one round of Snake Water Gun game."""
    print("Welcome to the Snake Water Gun game!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    play_game()
