# node.py
import pygame
from constants import WHITE, BLACK, GRAY, RED, YELLOW, BLUE, GREEN, PURPLE, ORANGE, TURQUOISE


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED

    def make_closed(self):
        self.colour = RED

    def is_open(self):
        return self.colour == GREEN

    def make_open(self):
        self.colour = GREEN

    def is_barrier(self):
        return self.colour == BLACK

    def make_barrier(self):
        self.colour = BLACK

    def is_start(self):
        return self.colour == ORANGE

    def make_start(self):
        self.colour = ORANGE

    def is_end(self):
        return self.colour == TURQUOISE

    def make_end(self):
        self.colour = TURQUOISE

    def is_path(self):
        return self.colour == PURPLE

    def make_path(self):
        self.colour = PURPLE

    def reset(self):
        self.colour = WHITE

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbours.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbours.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
