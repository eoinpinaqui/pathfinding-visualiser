# grid.py
import pygame
from constants import GRAY
from node import Node


def make_grid(total_rows, width):
    grid = []
    node_width = width // total_rows
    for i in range(total_rows):
        grid.append([])
        for j in range(total_rows):
            node = Node(i, j, node_width, total_rows)
            grid[i].append(node)
    return grid


def draw_grid(window, total_rows, width):
    node_width = width // total_rows
    for i in range(total_rows):
        pygame.draw.line(window, GRAY, (0, i * node_width), (width, i * node_width))
        pygame.draw.line(window, GRAY, (i * node_width, 0), (i * node_width, width))


def clear_grid(grid):
    for row in grid:
        for node in row:
            node.reset()


def clear_grid_keep_barriers(grid):
    for row in grid:
        for node in row:
            if node.is_end() or node.is_start() or node.is_barrier():
                continue
            else:
                node.reset()
