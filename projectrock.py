import tkinter as tk
import random

# Function to determine the winner and update the label
def determine_winner(player_choice):
    global player_score, computer_score
    
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        player_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_score()

# Function to update the score display
def update_score():
    score_label.config(text=f"Player Score: {player_score}  Computer Score: {computer_score}")

# Function to reset the game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    update_score()
    result_label.config(text="")

# Initialize scores
player_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons with text labels
rock_button = tk.Button(root, text="Rock", width=20, command=lambda: determine_winner('Rock'))
paper_button = tk.Button(root, text="Paper", width=20, command=lambda: determine_winner('Paper'))
scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: determine_winner('Scissors'))
reset_button = tk.Button(root, text="Reset Game", width=20, command=reset_game)

# Arrange buttons in a grid
rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)
reset_button.grid(row=1, column=0, columnspan=3, pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=('Helvetica', 16))
result_label.grid(row=2, column=0, columnspan=3, pady=20)

# Label to display the score
score_label = tk.Label(root, text=f"Player Score: {player_score}  Computer Score: {computer_score}", font=('Helvetica', 14))
score_label.grid(row=3, column=0, columnspan=3)

# Run the application
root.mainloop()