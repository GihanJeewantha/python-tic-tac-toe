boardboard = [1,2,3,4,5,6,7,8,9]


player1_symbol =input("Choose Symbol: \"X or O\" ").upper()

while player1_symbol not in ["X", "O"]:
    if player1_symbol == "X":
        player2_symbol = "O"
    else: player2_symbol = "X"


print(player1_symbol)
print(player2_symbol)
