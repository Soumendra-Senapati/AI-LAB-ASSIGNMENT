def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
            
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
        
    return False

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    for turn in range(9):
        print("\nCurrent Board:")
        print_board(board)
        print(f"Player {player}'s turn")
        
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the col (0-2): "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue
            
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Out of bounds! Enter row and col between 0 and 2.")
            continue
            
        if board[row][col] == " ":
            board[row][col] = player
            
            # Check if the current player won
            if check_winner(board):
                print("\nFinal Board:")
                print_board(board)
                print(f"Player {player} wins!")
                return
                
            # Switch player turn
            player = "O" if player == "X" else "X"
        else:
            print("Cell already occupied! Try again.")
            
    # If 9 turns complete without a winner
    print("\nFinal Board:")
    print_board(board)
    print("Game Draw!")

if _name_ == "_main_":
    play_tic_tac_toe()
