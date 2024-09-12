import random

# List of possible moves
moves = ['rock','paper','scissors']

# Function to dertermine the winner
def determine_winner(player_move,computer_move):
    if player_move==computer_move:
        return "It's a tie!"
    elif(player_move=='rock' and computer_move=="scissors") or\
    (player_move=="scissors" and computer_move=="paper") or\
    (player_move=='paper' and computer_move=='rock'):
        return "Youu win!"
    else:
        return "Compputer win!"
    
# Main game loop
while True:
    # Get the player's move
    player_move = input("Enter your move (rock, paper, scissors) or 'quit' to exit: ").lower()
    
    # Check if the player wants to quit
    if player_move == 'quit':
        print("Thanks for playing!")
        break
    
    # Check if the move is valid
    if player_move not in moves:
        print("Invalid move, please try again.")
        continue
    
    # Get the computer's move
    computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")
    
    # Determine the winner
    result = determine_winner(player_move, computer_move)
    print(result)
