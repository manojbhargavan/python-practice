import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.gol_list = np.zeros((x_dim, y_dim)).astype(int)

    def get_grid(self):
        # Implement a getter method for your grid.
        return self.gol_list

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        for i in range(0, self.x_dim):
            for j in range(0, self.y_dim):
                print(self.gol_list[i][j], end=' | ')
            print('')
            print(''.join(['- ' for i in range(0, self.x_dim * 2)]))

    def populate_grid(self, coord: (int, int)):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        x, y = coord
        x -= 1
        y -= 1
        if x < 0 or x > self.x_dim - 1 or y < 0 or y > self.y_dim:
            raise ValueError
        self.gol_list[x][y] = 1

    def get_adjacent(self, x, y):
        result = []
        adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in adjacent:
            x_adjacent, y_adjacent = i
            x_adjacent += x
            y_adjacent += y
            if 0 <= x_adjacent < self.x_dim and 0 <= y_adjacent < self.y_dim:
                result.append((x_adjacent, y_adjacent))
        return result

    def get_value(self, x, y):
        result = []
        adjacent = self.get_adjacent(x, y)
        for coord in adjacent:
            x_cur, y_cur = coord
            result.append(self.gol_list[x_cur][y_cur])

        return result

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        for i in range(0, self.x_dim):
            for j in range(0, self.y_dim):
                adjacent_values = self.get_value(i, j)
                # Any live cell with two or three live neighbors survives. Otherwise, a cell dies due to loneliness
                # (with no or only one neighbor) or overpopulation (with four or more neighbors).
                live_adjacent_list = [x for x in adjacent_values if x == 1]
                live_adjacent = len(live_adjacent_list)
                if self.gol_list[i][j] == 1:
                    if 2 <= live_adjacent <= 3:
                        self.gol_list[i][j] = 1
                    elif live_adjacent < 2:
                        self.gol_list[i][j] = 0
                    elif live_adjacent >= 4:
                        self.gol_list[i][j] = 0

                # Any dead cell with (exactly) three live neighbors becomes a live cell.
                # A dead cell with any other number of neighbors remains dead.
                if self.gol_list[i][j] == 0:
                    if live_adjacent == 3:
                        self.gol_list[i][j] = 1
                    else:
                        self.gol_list[i][j] = 0

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        for step in range(0, n):
            self.make_step()

    def draw_grid(self):
        # Draw the current state of the grid.
        dead_cells_x = []
        dead_cells_y = []
        live_cells_x = []
        live_cells_y = []
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.gol_list[i][j] == 0:
                    dead_cells_x.append(i + 1)
                    dead_cells_y.append(j + 1)
                else:
                    live_cells_x.append(i + 1)
                    live_cells_y.append(j + 1)

        plt.scatter(dead_cells_x, dead_cells_y, color='purple')
        plt.scatter(live_cells_x, live_cells_y, color='yellow')
        plt.show()

x = 30
y = 30
gol = GameOfLife(x, y)
# init_list = [(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)]
# for coord in init_list:
#     gol.populate_grid(coord)
#
# not_steady_state = True
# while not_steady_state:
#     current_grid = gol.get_grid()[:]
#     gol.make_n_steps(14)
#     for i in range(x):
#         if list(current_grid[i]) == list(gol.get_grid()[i]):
#             not_steady_state = True
#         else:
#             not_steady_state = False
#             print(list(current_grid[i]), list(gol.get_grid()[i]))
#             break
#     gol.draw_grid()
init_list = [(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)]
for coord in init_list:
    gol.populate_grid(coord)
gol.draw_grid()
gol.make_n_steps(12)
gol.draw_grid()