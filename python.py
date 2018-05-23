from __future__ import print_function
import random
import os
import sys
#clear output 

head = """
 _____   _   _____       _____   _____    ______       _____    _____    ____
/__ __\ / \ /   __\     /__ __\ /  _  \  /    __\     /__ __\  /  _  \  /  __/ 
  / \   | | |  /   ____   / \  |  / \  | |   /   ____   / \   |  / \  | |  |
  | |   | | |  \__ \___\  | |  |  |_|  | |   \__ \___\  | |   |  \ /  | |  /_ 
  \_/   \_/  \____/       \_/  \_/   \_/ \______/       \_/    \_____/  \____/

                           ------------
                           | 1 | 2 | 3 |
                           | 4 | 5 | 6 | 
                           | 7 | 8 | 9 |
                           ------------ 
"""
                        

class Game(object):
    def my_board(self,board):
        print(head)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
    def player_input(self):
        marker = ' '
        while not (marker == 'X' or marker == 'O'):
            marker = input('Choose O or X to play!').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
    def place_marker(self,board,marker,postion):
        board[position] = marker

    def win_check (self,board,mark):
        return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or 
        (board[4] == mark and board[5] == mark and board[6] == mark) or 
        (board[1] == mark and board[2] == mark and board[3] == mark) or 
        (board[7] == mark and board[4] == mark and board[1] == mark) or 
        (board[8] == mark and board[5] == mark and board[2] == mark) or 
        (board[9] == mark and board[6] == mark and board[3] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) or 
        (board[9] == mark and board[5] == mark and board[1] == mark)
        ) 
     
    def choose_first(self):
        if random.randint(0,1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

 
    def check_space(self,board,position):
        return board[position] == ' '
 
    def full_board_check (self,board):
        for i in range (1,10):
            if self.check_space(board,i):
                return False
        return True

 
    def player_choice(self,board):
        player = self.choose_first()
 
        position = ' '
        while position not in '1 2 3 4 5 6 7 8 9'.split() or not self.check_space(board, int(position)):            
            position = input(player  +'Choose number input ')
        return int(position)


    def replay(self):
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    print('Welcome to Tic Tac Toe Game!')
 
if __name__ == "__main__":
    game = Game()

    while True:
        theBoard = [' '] * 10
        player1_marker, player2_marker = game.player_input()
        turn = game.choose_first()
        print(turn + ' will go first.')
        game_on = True

        while game_on:
            if turn == 'Player 1':
                game.my_board(theBoard)
                position = game.player_choice(theBoard)
                game.place_marker(theBoard, player1_marker, position)

                if game.win_check(theBoard, player1_marker):
                    game.my_board(theBoard)
                    print('Playe 1 has won!')
                    game_on = False
                else:
                    if game.full_board_check(theBoard):
                        my_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
        

                game.my_board(theBoard)
                position = game.player_choice(theBoard)
                game.place_marker(theBoard, player2_marker, position)

                if game.win_check(theBoard, player2_marker):
                    game.my_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if game.full_board_check(theBoard):
                        my_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'

        if not game.replay():
            break   