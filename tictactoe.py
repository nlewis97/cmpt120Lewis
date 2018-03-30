# CMPT 120 Intro to Programming
# Lab #7 – Tic Tac Toe Game
# Author: Nicholas Lewis
# Created: 2018-03-29
def tictactoe():
    board = [None] + list(range(1, 10))
    win = [(1, 2, 3),(4, 5, 6),(7, 8, 9),(1, 4, 7),(2, 5, 8),(3, 6, 9),(1, 5, 9),(3, 5, 7),]

    def drawboard():
        print(board[1], board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print()

    def markboard():
        while True:
            try:
                a = int(input())
                if a in board:
                    return a
                else:
                    print("Sorry this is an invalid move. Try again")
            except ValueError:
               print("Sorry this is an invalid move. Try again")

    def gameover():
        for a, b, c in win:
            if board[a] == board[b] == board[c]:
                print("Player {0} wins!".format(board[a]))
                return True
        if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
            print("The game ends in a tie")
            return True

    for player in 'XO' * 9:
        drawboard()
        if gameover():
            break
        print("Player {0} pick your move".format(player))
        board[markboard()] = player
        print()

while True:
    tictactoe()
    if input("Do you want to play again? (y/n)") != "y":
        break
