import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    return (board[0][0] == board[1][1] == board[2][2] == player) or \
           (board[0][2] == board[1][1] == board[2][0] == player)

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def ai_move(board):
    # Try to win
    for (i, j) in get_empty_positions(board):
        board[i][j] = 'O'
        if check_winner(board, 'O'):
            return
        board[i][j] = ' '

    # Try to block X
    for (i, j) in get_empty_positions(board):
        board[i][j] = 'X'
        if check_winner(board, 'X'):
            board[i][j] = 'O'
            return
        board[i][j] = ' '

    # Take center if available
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return

    # Take any corner or side
    move = random.choice(get_empty_positions(board))
    board[move[0]][move[1]] = 'O'

def play_game():
    board = [[' ']*3 for _ in range(3)]
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)

    for _ in range(9):
        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        break
                    else:
                        print("Cell already taken!")
                else:
                    print("Row and column must be between 0 and 2.")
            except:
                print("Invalid input. Try again.")

        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            return

        if not get_empty_positions(board):
            break

        print("AI is making a move...")
        ai_move(board)
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            return

        if not get_empty_positions(board):
            break

    print("It's a draw!")

# Run the game
play_game()
