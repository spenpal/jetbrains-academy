import random
import itertools
from collections import Counter

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
    
class DominoesGame:
    domino_set = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]
    
    def __init__(self):
        self.stock_pieces = []
        self.computer_pieces = []
        self.player_pieces = []
        self.domino_snake = []
        self.status = ''
        self.winner = ''
        self.moves = []
    
    def reset(self):
        self.stock_pieces = []
        self.computer_pieces = []
        self.player_pieces = []
        self.domino_snake = []
        self.status = ''
        
    def double_domino(self, domino):
        return domino[0] == domino[1]
        
    def assign_pieces(self):
        copy_set = self.domino_set[:]
        random.shuffle(copy_set)
        
        for _ in range(7):
            computer_piece, player_piece = random.sample(copy_set, k=2)
            
            self.computer_pieces.append(computer_piece)
            self.player_pieces.append(player_piece)
            
            copy_set.remove(computer_piece)
            copy_set.remove(player_piece)
            
        self.stock_pieces = copy_set
    
    def setup(self):
        while not self.status:
            self.reset()
            self.assign_pieces()
            
            self.player_pieces.sort(reverse=True)
            self.computer_pieces.sort(reverse=True)
        
            for player_piece, computer_piece in zip(self.player_pieces, self.computer_pieces):
                highest_domino = max(player_piece, computer_piece)
                
                if self.double_domino(highest_domino):
                    self.domino_snake.append(highest_domino)
                    
                    if highest_domino == player_piece:
                        self.player_pieces.remove(highest_domino)
                        self.status = 'computer'
                    else:
                        self.computer_pieces.remove(highest_domino)
                        self.status = 'player'
                        
                    break
    
    def end_condition(self):
        if not (len(self.computer_pieces) and len(self.player_pieces)): 
            return True
        
        if self.domino_snake[0][0] == self.domino_snake[-1][1]:
            num = self.domino_snake[0][0]
            count = sum(num1 == num + num2 == num for num1, num2 in self.domino_snake)
            if count >= 8:
                return True
        
        if not len(self.stock_pieces) and self.moves[-4:] == [0, 0, 0, 0]:
            return True
        
        return False
    
    def print_game_state(self):
        state = []
        state.append('=' * 70)
        state.append(f'Stock size: {len(self.stock_pieces)}')
        state.append(f'Computer pieces: {len(self.computer_pieces)}\n')
        
        snake = ''
        if len(self.domino_snake) > 6:
            first_three = ''.join([str(d) for d in self.domino_snake[:3]])
            last_three = ''.join([str(d) for d in self.domino_snake[-3:]])
            snake = '...'.join([first_three, last_three])
        else:
            snake = ''.join([str(d) for d in self.domino_snake])
        state.append(snake + '\n')
        
        state.append(f'Your pieces:')
        pieces = [f'{i+1}:{piece}' for i, piece in enumerate(self.player_pieces)]
        pieces = '\n'.join(pieces) + ('\n' * (len(pieces) > 0))
        state.append(pieces)
        
        if self.winner:
            if self.winner == 'player': state.append('Status: The game is over. You won!')
            elif self.winner == 'computer': state.append('Status: The game is over. The computer won!')
            elif self.winner == 'draw': state.append("Status: The game is over. It's a draw!")
        else:
            if self.status == 'player': 
                state.append("Status: It's your turn to make a move. Enter your command.")
            else: 
                state.append("Status: Computer is about to make a move. Press Enter to continue...")
        
        state = '\n'.join(state)
        print(state)
    
    def illegal_move(self, number, piece):
        d_num = self.domino_snake[0][0] if number < 0 else self.domino_snake[-1][1]
        return d_num not in piece
            
    def verify_move(self, choice):
        while True:
            if not (is_integer(choice) and -len(self.player_pieces) <= int(choice) <= len(self.player_pieces)):
                print('Invalid input. Please try again.')
            elif int(choice) != 0 and self.illegal_move(int(choice), self.player_pieces[abs(int(choice)) - 1]):
                print('Illegal move. Please try again.')
            else:
                return choice
                
            choice = input()
                
    def update_domino_snake(self, number, piece):
        if number < 0:
            piece = piece[::-1] if self.domino_snake[0][0] == piece[0] else piece
            self.domino_snake.insert(0, piece)
        elif number > 0:
            piece = piece[::-1] if self.domino_snake[-1][1] == piece[1] else piece
            self.domino_snake.append(piece)
            
    def get_winner(self):
        if not len(self.computer_pieces): self.winner = 'computer'
        elif not len(self.player_pieces): self.winner = 'player'
        else: self.winner = 'draw'
          
    def start(self):
        self.setup()
        
        while not self.end_condition():
            self.print_game_state()
            choice = input()
            
            if self.status == 'player':
                choice = self.verify_move(choice)
                    
                number = int(choice)
                self.moves.append(number)
                
                if number == 0:
                    if len(self.stock_pieces): 
                        piece = random.choice(self.stock_pieces)
                        self.stock_pieces.remove(piece)
                        self.player_pieces.append(piece)
                else:
                    piece = self.player_pieces.pop(abs(number) - 1)
                    self.update_domino_snake(number, piece)
            else:
                lst = self.computer_pieces + self.domino_snake
                lst = list(itertools.chain(*lst)) # flatten nested lists
                counts = Counter(lst)
                scores = Counter({(num1, num2): counts[num1] + counts[num2] for num1, num2 in self.computer_pieces}).most_common()
                
                number = 0
                for piece, _ in scores:
                    piece = list(piece)
                    if not self.illegal_move(-number, piece):
                        number = -(self.computer_pieces.index(piece) + 1)
                        break
                    elif not self.illegal_move(number, piece):
                        number = self.computer_pieces.index(piece) + 1
                        break
                
                self.moves.append(number)
                
                if number == 0:
                    if len(self.stock_pieces): 
                        piece = random.choice(self.stock_pieces)
                        self.stock_pieces.remove(piece)
                        self.computer_pieces.append(piece)
                else:
                    self.computer_pieces.remove(piece)
                    self.update_domino_snake(number, piece)
            
            self.status = 'player' if self.status == 'computer' else 'computer'
        
        self.get_winner()
        self.print_game_state()
            
    def __str__(self):
        return (
            f'Stock pieces: {self.stock_pieces}\n'
            f'Computer pieces: {self.computer_pieces}\n'
            f'Player pieces: {self.player_pieces}\n'
            f'Domino snake: {self.domino_snake}\n'
            f'Status: {self.status}'
        )

# MAIN #
game = DominoesGame()
game.start()