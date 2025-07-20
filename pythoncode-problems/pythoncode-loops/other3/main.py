import random

# Game loop starts here
while True:
    print('''
    Choose any one from below:
    ** rock  * paper * scissors **
    --- Press 'Q' to quit ---
    ''')

    # Computer randomly chooses one of the options
    computer = random.choice(['rock', 'paper', 'scissors'])

    # User input, with 'Q' as a quit option
    user = input("Enter your choice (rock, paper, scissors or 'Q' to quit): ").lower()

    if user == 'q':  # Check if the user wants to quit
        print("Thanks for playing!")
        break  # Exit the game loop

    # Validate the user input
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, please choose rock, paper, or scissors.")
        continue  # Restart the loop if input is invalid

    print(f"Your choice: {user}")
    print(f"Computer's choice: {computer}")

    # Determine the result
    if computer == user:
        print("It's a tie!")

    else:
        if (computer == 'rock' and user == 'scissors') or \
           (computer == 'scissors' and user == 'paper') or \
           (computer == 'paper' and user == 'rock'):
            print("You lost!")
        else:
            print("You won!")

