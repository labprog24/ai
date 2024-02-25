import numpy as np
import random
from time import sleep

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

def check_win(board, player):

    return (np.any(np.all(board == player, axis=0)) 
            or np.any(np.all(board == player, axis=1)) 
            or np.all(np.diag(board) == player) 
            or np.all(np.diag(np.fliplr(board)) == player)) 

def evaluate(board):
    for player in [1, 2]:
        if check_win(board, player):
            return player
    if np.all(board != 0):
        return -1
    return 0

def play_game():
    board = create_board()
    print(board)
    sleep(1)
    winner = 0
    counter = 1

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"board after {counter} move")
            print(board)
            sleep(1)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

print("Winner is:", play_game())
