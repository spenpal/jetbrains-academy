# IMPORTS #
import warnings
from copy import deepcopy

import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)


# CLASS #
class Tetris:

    def __init__(self, dims=(10, 20)):
        self.width, self.height = dims
        self.area = self.width * self.height
        self.grid = np.array([['-'] * self.width for _ in range(self.height)])
        self.print_grid()

        self.piece = None
        self.position = None
        self.positions = None
        self.starting_positions = {
            'O': np.array([[4, 14, 15, 5]]),
            'I': np.array([[4, 14, 24, 34], [3, 4, 5, 6]]),
            'S': np.array([[5, 4, 14, 13], [4, 14, 15, 25]]),
            'Z': np.array([[4, 5, 15, 16], [5, 15, 14, 24]]),
            'L': np.array([[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]),
            'J': np.array([[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]),
            'T': np.array([[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]])
        }
        self.rotation_num = 0
        self.static = True

    def _get_indices(self, grid_num):
        return divmod(grid_num, self.width)

    def _fall(self):
        self.positions += self.width

    def _add_grid_position(self):
        for grid_num in self.position:
            row, col = self._get_indices(grid_num)
            self.grid[row][col] = '0'

    def _remove_grid_position(self):
        for grid_num in self.position:
            row, col = self._get_indices(grid_num)
            self.grid[row][col] = '-'

    def _move(self, action):
        if action == 'rotate':
            num_of_rotations = len(self.positions)
            self.rotation_num = (self.rotation_num + 1) % num_of_rotations
        elif action == 'left':
            if not abs(self._get_indices(self.position)[0] - self._get_indices(self.position - 1)[0]).any():
                self.positions -= 1
        elif action == 'right':
            if not abs(self._get_indices(self.position)[0] - self._get_indices(self.position + 1)[0]).any():
                self.positions += 1

    def _break(self):
        while np.all(self.grid[-1] == '0'):
            self.grid = np.delete(self.grid, -1, axis=0)
            self.grid = np.insert(self.grid, 0, np.array(['-'] * self.width), axis=0)
            if not self.static:
                self._fall()

    def _check_static(self):
        return ((self.area - self.width < self.position) & (self.position < self.area)).any() \
               or any(self.grid[self._get_indices(grid_num)] == '0' for grid_num in (self.position + self.width))

    def _end_condition(self):
        return any(np.all(col == '0') for col in self.grid.T)

    def start(self):
        while (action := input()) != 'exit':

            if self._end_condition():
                self.print_grid()
                print('\nGame Over!')
                return

            if action == 'piece' and self.static:
                self.piece = input()
                self.positions = deepcopy(self.starting_positions[self.piece])
                self.position = self.positions[0]
                self.rotation_num = 0
                self._add_grid_position()
                self.static = False
            elif action == 'break':
                self._break()
            elif not self.static:
                self._remove_grid_position()

                self._move(action)
                self._fall()
                self.position = self.positions[self.rotation_num]

                self.static = self._check_static()
                self._add_grid_position()

            self.print_grid()

    def print_grid(self):
        for row in self.grid:
            print(*row)
        print()


# MAIN #
dims = tuple(map(int, input().split()))

game = Tetris(dims)
game.start()
