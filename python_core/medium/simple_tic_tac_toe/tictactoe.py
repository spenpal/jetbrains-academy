# IMPORTS #
import itertools


# CLASS #
class TicTacToe():
    
    def __init__(self, board_str='_' * 9):
        self.board = self.convert_to_board(board_str)
    
    def convert_to_board(self, board_str):
        return [list(board_str[i:i+3]) for i in range(0, len(board_str), 3)]
    
    def get_board_str(self):
        return ''.join(itertools.chain(*self.board))
           
    def win_diagonal(self, mark):
        return any([
            all(self.board[i][i] == mark for i in range(len(self.board))), # left diagonal
            all(self.board[len(self.board)-1-i][i] == mark for i in range(len(self.board))) # right diagonal
        ])
        
    def win_column(self, mark):
        board_t = list(map(list, zip(*self.board))) # tranpose the board
        return any(all(box == mark for box in row) for row in board_t)
        
    def win_row(self, mark):
        return any(all(box == mark for box in row) for row in self.board)
        
    def check_win(self, mark):
        return self.win_row(mark) or self.win_column(mark) or self.win_diagonal(mark)

    # def impossible(self):
    #     return (self.check_win(self.board, 'X') and self.check_win(self.board, 'O')) or abs(self.board_str.count('X') - self.board_str.count('O')) >= 2
        
    # def get_state(self):
    #     if self.impossible(): return 'Impossible'
    #     elif self.check_win('X'): return 'X wins'
    #     elif self.check_win('O'): return 'O wins'
    #     elif '_' in self.board_str: return 'Game not finished'
    #     return 'Draw'
    
    def winner(self):
        if self.check_win('X'):
            print('X wins')
            return True
        elif self.check_win('O'): 
            print('O wins')
            return True
        elif '_' not in self.get_board_str():
            print('Draw')
            return True
        
        return False
    
    def error_check(self, move):
        row_coord, col_coord = move.split()
        if not (row_coord.isnumeric() and col_coord.isnumeric()):
            print('You should enter numbers!')
            return True
        elif not (1 <= int(row_coord) <= 3 and 1 <= int(col_coord) <= 3):
            print('Coordinates should be from 1 to 3!')
            return True
        elif self.board[int(row_coord)-1][int(col_coord)-1] != '_':
            print('This cell is occupied! Choose another one!')
            return True
            
        return False
    
    def print_board(self):
        print('---------')
        for row in self.board:
            line = ' '.join(row)
            print(f'| {line} |')
        print('---------')
           
    def start(self):
        mark = 'X'
        self.print_board()
        
        while not self.winner():
            while self.error_check(move := input()): continue
            
            row, col = (int(coord) - 1 for coord in move.split())
            self.board[row][col] = mark
            
            mark = 'O' if mark == 'X' else 'X'
            self.print_board()


# MAIN #
game = TicTacToe()
game.start()