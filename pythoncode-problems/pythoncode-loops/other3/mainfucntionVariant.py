import random

def display_menu():
    """Displays the menu to the user."""
    print('''
    Choose any one from below:
    ** rock  * paper * scissors **
    --- Press 'Q' to quit ---
    ''')

def get_computer_choice():
    """Returns a random choice for the computer (rock, paper, or scissors)."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Prompts the user to enter their choice and validates it."""
    user_choice = input("Enter your choice (rock, paper, scissors or 'Q' to quit): ").lower()
    return user_choice

def determine_winner(user, computer):
    """Determines and prints the winner based on user and computer choices."""
    if computer == user:
        print("It's a tie!")
    elif (computer == 'rock' and user == 'scissors') or \
         (computer == 'scissors' and user == 'paper') or \
         (computer == 'paper' and user == 'rock'):
        print("You lost!")
    else:
        print("You won!")

def play_game():
    """Runs the game loop until the user decides to quit."""
    while True:
        display_menu()
        computer_choice = get_computer_choice()  # Get computer's random choice
        user_choice = get_user_choice()  # Get user's input
        
        # Check if the user wants to quit
        if user_choice == 'q':
            print("Thanks for playing!")
            break
        
        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue  # Restart the loop for a valid choice

        # Print choices
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine and print the result
        determine_winner(user_choice, computer_choice)

# Start the game
play_game()


