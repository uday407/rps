import tkinter as tk
from random import choice

# Define game options and messages
options = ["Rock", "Paper", "Scissors"]
WIN_MESSAGE = "You won!"
LOSS_MESSAGE = "You lost!"
TIE_MESSAGE = "It's a tie!"

# Dictionary to map user names to personalized messages
personalized_messages = {
    "Uday": "Hey Uday! Let's play Rock Paper Scissors.",
    "Replace": "Hello Replace! Ready for a game?"
}

# Initialize game statistics
game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

def decide_winner(user_choice):
    # Randomly choose computer's choice
    computer_choice = choice(options)
   
    # Determine game result
    if user_choice == computer_choice:
        result = TIE_MESSAGE
        game_stats["ties"] += 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = WIN_MESSAGE
        game_stats["wins"] += 1
    else:
        result = LOSS_MESSAGE
        game_stats["losses"] += 1
       
    # Return formatted result message
    return f"Computer's choice: {computer_choice}\n{result}"

def play_RPS():
    # Get user's name and choice
    user_name = user_name_var.get()
    user_choice = user_choice_var.get()
   
    # Update personalized message based on user's name
    if user_name in personalized_messages:
        personalized_message.set(personalized_messages[user_name])
    else:
        personalized_message.set(f"Hello {user_name}! Let's play.")
   
    # Determine game outcome and update result message
    result = decide_winner(user_choice)
    result_text.set(result)
   
    # Update game statistics display
    stats_text.set(f"Wins: {game_stats['wins']} | Losses: {game_stats['losses']} | Ties: {game_stats['ties']}")

def reset_game():
    # Reset game statistics
    game_stats["wins"] = 0
    game_stats["losses"] = 0
    game_stats["ties"] = 0
   
    # Clear result and update game statistics display
    result_text.set("")
    stats_text.set("")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Set background color and fonts
background_color = "#e0e0e0"
font_style = ("Helvetica", 14)

# Configure root window
root.configure(bg=background_color, padx=20, pady=20)

# Create GUI elements
tk.Label(root, text="Enter your name:", bg=background_color, font=font_style).pack()
user_name_var = tk.StringVar()
tk.Entry(root, textvariable=user_name_var, font=font_style).pack(pady=10)

tk.Label(root, text="Select your choice:", bg=background_color, font=font_style).pack()

# Create radio buttons for game options
user_choice_var = tk.StringVar()
for option in options:
    tk.Radiobutton(root, text=option, variable=user_choice_var, value=option, bg=background_color, font=font_style).pack(anchor="center")

# Create Play button
play_button = tk.Button(root, text="Play", command=play_RPS, bg="#4CAF50", fg="white", font=font_style, bd=3, relief=tk.RAISED)
play_button.pack(pady=20)

# Result label to display game outcome
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, bg=background_color, font=font_style)
result_label.pack()

# Personalized message label
personalized_message = tk.StringVar()
tk.Label(root, textvariable=personalized_message, bg=background_color, font=font_style).pack(pady=10)

# Game statistics display
stats_text = tk.StringVar()
stats_label = tk.Label(root, textvariable=stats_text, bg=background_color, font=font_style)
stats_label.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game, bg="#f44336", fg="white", font=font_style, bd=3, relief=tk.RAISED)
reset_button.pack(pady=20)

# Run the main event loop
root.mainloop()