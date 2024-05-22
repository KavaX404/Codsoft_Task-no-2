import numpy as np
import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to check if the game is over
def game_over(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to evaluate the board for the AI player
def evaluate(board):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    else:
        return 0

# Minimax function with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth-1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth-1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = minimax(board, 5, False, alpha, beta)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are playing against the AI. Enter your moves in the format 'row col'.")
    print_board(board)

    while not game_over(board):
        # Player's move
        player_move = input("Enter your move (row col): ").split()
        row, col = map(int, player_move)
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)

        if game_over(board):
            break

        # AI's move
        print("AI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'
        print("AI's move: ", ai_move)
        print_board(board)

    if check_winner(board, 'X'):
        print("Congratulations! You win!")
    elif check_winner(board, 'O'):
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw!")

# Start the game
play_game()
