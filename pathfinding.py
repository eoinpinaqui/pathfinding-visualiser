# pathfinding.py
import pygame
from constants import WIDTH, TOTAL_ROWS, WHITE
import grid
from algorithms import astar, dijkstras, dfs

# Setup
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualiser")


# Methods
def draw(win, node_grid, total_rows, width):
    win.fill(WHITE)
    for row in node_grid:
        for node in row:
            node.draw(win)
    grid.draw_grid(win, total_rows, width)
    pygame.display.update()


def get_clicked_pos(mouse_pos, total_rows, width):
    node_width = width // total_rows
    i, j = mouse_pos
    row = i // node_width
    col = j // node_width
    return row, col


def main(win, width):
    total_rows = TOTAL_ROWS
    node_grid = grid.make_grid(total_rows, width)
    start = None
    end = None
    running = True
    started = False
    clear = False

    while running:
        draw(win, node_grid, total_rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, total_rows, WIDTH)
                node = node_grid[row][col]
                if clear:
                    clear = False
                    grid.clear_grid_keep_barriers(node_grid)
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                if clear:
                    clear = False
                    grid.clear_grid_keep_barriers(node_grid)
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, total_rows, WIDTH)
                node = node_grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if clear:
                    clear = False
                    grid.clear_grid_keep_barriers(node_grid)
                if not started:
                    for row in node_grid:
                        for node in row:
                            node.update_neighbours(node_grid)
                    if event.key == pygame.K_SPACE:
                        start = None
                        end = None
                        grid.clear_grid(node_grid)
                    if event.key == pygame.K_1:
                        astar.algorithm(lambda: draw(win, node_grid, total_rows, width), node_grid, start, end)
                        started = False
                        clear = True
                    if event.key == pygame.K_2:
                        dijkstras.algorithm(lambda: draw(win, node_grid, total_rows, width), node_grid, start, end)
                        started = False
                        clear = True
                    if event.key == pygame.K_3:
                        dfs.algorithm(lambda: draw(win, node_grid, total_rows, width), node_grid, start, end)
                        started = False
                        clear = True

    pygame.quit()


main(window, WIDTH)