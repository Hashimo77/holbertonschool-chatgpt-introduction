#!/usr/bin/python3
"""
Simple Tic-Tac-Toe game for two players (X and O).

Players alternate turns to place their marks on a 3x3 grid.
The first player to get three marks in a row (horizontally, vertically, or diagonally) wins.
If the board fills up with no winner, the game ends in a draw.
"""

def print_board(board):
    """Displays the current game board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    """Checks if any player has won."""
    # check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Checks if the board is completely filled."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid input
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Check input range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("⚠️ Invalid position! Choose 0, 1, or 2.")
                continue
        except ValueError:
            print("⚠️ Invalid input! Please enter numbers only.")
            continue

        # Check if cell is available
        if board[row][col] != " ":
            print("⚠️ That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        # Check for draw
        if is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
