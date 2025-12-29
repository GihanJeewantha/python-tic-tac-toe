board = [1,2,3,4,5,6,7,8,9]

def display_board():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])


# Ask Player 1 to choose X or O
player1_symbol = input('choose your symbol (X or O): ').strip().upper()

# Keep asking enter a valid choice
while player1_symbol not in ["X", "O"]:
    print("Invalid choice! Please enter only 'X' or 'O'.")
    player1_symbol = input('choose your symbol (X or O): ').strip().upper()

# assign the opposite symbol to Player 2
if player1_symbol == "X":
    player2_symbol = "O"
else:
    player2_symbol = "X"


print(f"Player 1: {player1_symbol}")
print(f"Player 2: {player2_symbol}")

display_board()