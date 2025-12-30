board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()  


# Ask Player 1 to choose X or O
player1_symbol = input('Player 1, choose your symbol (X or O): ').strip().upper()

# Validate symbol choice
while player1_symbol not in ["X", "O"]:
    print("Invalid choice! Please enter only 'X' or 'O'.")
    player1_symbol = input('Player 1, choose your symbol (X or O): ').strip().upper()

# Assign opposite symbol to Player 2
player2_symbol = "O" if player1_symbol == "X" else "X"

print(f"Player 1: {player1_symbol}")
print(f"Player 2: {player2_symbol}")
print("\nGame Start!\n")

display_board()


def check_winner(symbol):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == symbol and board[combo[1]] == symbol and board[combo[2]] == symbol:
            return True
    return False


# Main game loop
current_player_symbol = player1_symbol
current_player_name = "Player 1"

while True:
    # Get valid move
    while True:
        try:
            position = int(input(f"{current_player_name} ({current_player_symbol}), enter position (1-9): "))

            if not 1 <= position <= 9:
                print("Invalid! Choose a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] in ["X", "O"]:
                print("Position already taken! Choose another.")
                continue

            # Place symbol
            board[index] = current_player_symbol
            display_board()
            break

        except ValueError:
            print("Invalid input! Please enter a number.")

    # Check for winner
    if check_winner(current_player_symbol):
        print(f"🎉 Congratulations! {current_player_name} ({current_player_symbol}) wins! 🎉")
        break

    # Check for draw (all spots filled)
    if all(isinstance(cell, str) for cell in board):  # All are X or O (no numbers left)
        print("It's a draw! Well played both!")
        break

    # Switch player
    if current_player_symbol == player1_symbol:
        current_player_symbol = player2_symbol
        current_player_name = "Player 2"
    else:
        current_player_symbol = player1_symbol
        current_player_name = "Player 1"