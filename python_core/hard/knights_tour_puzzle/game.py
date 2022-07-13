# IMPORTS #
from copy import deepcopy


# CLASS #
class KnightsTourPuzzle:

    def __init__(self):
        # Get board dimensions
        dimensions = input('Enter your board dimensions: ')
        while not self._valid_dimensions(dimensions):
            print('Invalid dimensions!')
            dimensions = input('Enter your board dimensions: ')
        self.x_dim, self.y_dim = int(dimensions.split()[0]), int(dimensions.split()[1])

        # Create board
        self.cell_size = len(str(self.x_dim * self.y_dim))
        self.board = [['_' * self.cell_size] * self.x_dim for _ in range(self.y_dim)]
        self.border = '-' * (self.x_dim * (self.cell_size + 1) + 3)
        self.next_moves_board = deepcopy(self.board)

        # Get starting position
        start_position = input("Enter the knight's starting position: ")
        while not self._valid_position(start_position):
            print('Invalid position!')
            start_position = input("Enter the knight's starting position: ")
        self.x_pos, self.y_pos = int(start_position.split()[0]) - 1, int(start_position.split()[1]) - 1
        self.board[self.y_pos][self.x_pos] = 'X'.rjust(self.cell_size)

        # Others
        self.visited = {(self.x_pos, self.y_pos)}
        self.next_steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        # For AI
        self.solver_board = deepcopy(self.board)
        self.solver_board[self.y_pos][self.x_pos] = '1'.rjust(self.cell_size)
        self.solver_visited = deepcopy(self.visited)

    @staticmethod
    def _valid_dimensions(dimensions):
        if len(dimensions.split()) != 2:
            return False
        x_dim, y_dim = dimensions.split()
        if not all((x_dim.isnumeric(), y_dim.isnumeric())):
            return False
        if int(x_dim) == 0 or int(y_dim) == 0:
            return False
        return True

    def _valid_position(self, position):
        if len(position.split()) != 2:
            return False
        x_pos, y_pos = position.split()
        if not all((x_pos.isnumeric(), y_pos.isnumeric())):
            return False
        if not ((1 <= int(x_pos) <= self.x_dim) and (1 <= int(y_pos) <= self.y_dim)):
            return False
        return True

    @staticmethod
    def _valid_move(move, next_moves):
        if len(move.split()) != 2:
            return False
        x_move, y_move = move.split()
        if not all((x_move.isnumeric(), y_move.isnumeric())):
            return False
        if (int(x_move) - 1, int(y_move) - 1) not in next_moves:
            return False
        return True

    def _get_next_moves(self, x_pos, y_pos, visited):
        next_positions = []

        for x_step, y_step in self.next_steps:
            next_x_pos, next_y_pos = x_pos + x_step, y_pos + y_step
            if (
                    0 <= next_x_pos <= self.x_dim - 1
                    and 0 <= next_y_pos <= self.y_dim - 1
                    and (next_x_pos, next_y_pos) not in visited
            ):
                next_positions.append((next_x_pos, next_y_pos))

        return next_positions

    def _solver(self, pos, move_num):
        next_moves = self._get_next_moves(*pos, self.solver_visited)
        if not next_moves:
            return

        next_moves_counts = {}
        for next_move in next_moves:
            second_next_moves = self._get_next_moves(*next_move, self.solver_visited)
            next_moves_counts[next_move] = len(second_next_moves)

        next_best_moves = sorted(next_moves_counts, key=lambda move: next_moves_counts[move], reverse=True)
        for next_best_move in next_best_moves:
            next_best_x_pos, next_best_y_pos = next_best_move

            self.solver_board[next_best_y_pos][next_best_x_pos] = move_num + 1
            self.solver_visited.add(next_best_move)

            self._solver(next_best_move, move_num + 1)
            
            if len(self.solver_visited) == self.x_dim * self.y_dim:  # goal state
                return
            else:  # reset board to previous state
                self.solver_board[next_best_y_pos][next_best_x_pos] = '_' * self.cell_size
                self.solver_visited.remove(next_best_move)

    def start(self):
        ans = input('Do you want to try the puzzle? (y/n): ')
        while ans not in ['y', 'n']:
            print('Invalid input!')
            ans = input('Do you want to try the puzzle? (y/n): ')

        self._solver((self.x_pos, self.y_pos), 1)  # AI solves the puzzle

        if len(self.solver_visited) != self.x_dim * self.y_dim:
            print('No solution exists!')
            return

        # AI plays
        if ans == 'n':
            print("\nHere's the solution!")
            self.print_board(self.solver_board)
            return

        # User plays
        while True:
            next_moves = self._get_next_moves(self.x_pos, self.y_pos, self.visited)
            if not next_moves:
                break

            for next_x_move, next_y_move in next_moves:
                second_next_moves = self._get_next_moves(next_x_move, next_y_move, self.visited)
                total_second_next_moves = len(second_next_moves)
                self.next_moves_board[next_y_move][next_x_move] = str(total_second_next_moves).rjust(self.cell_size)
            self.print_board(self.next_moves_board)
            print()

            user_move = input('Enter your next move: ')
            while not self._valid_move(user_move, next_moves):
                print('Invalid move!', end=' ')
                user_move = input('Enter your next move: ')

            self.board[self.y_pos][self.x_pos] = '*'.rjust(self.cell_size)
            self.x_pos, self.y_pos = int(user_move.split()[0]) - 1, int(user_move.split()[1]) - 1
            self.board[self.y_pos][self.x_pos] = 'X'.rjust(self.cell_size)
            self.visited.add((self.x_pos, self.y_pos))

            self.next_moves_board = deepcopy(self.board)

        if len(self.visited) == self.x_dim * self.y_dim:
            print('What a great tour! Congratulations!')
        else:
            print('No more possible moves!')
            print(f'Your knight visited {len(self.visited)} squares!')

    def print_board(self, board):
        print('Here are the possible moves:')
        print(f" {self.border}")
        for row in range(self.y_dim, 0, -1):
            print(f'{row}|', *board[row - 1], '|')
        print(f" {self.border}")
        print('  ', *range(1, self.x_dim + 1), sep=' ' * self.cell_size)


# MAIN #
game = KnightsTourPuzzle()
game.start()
