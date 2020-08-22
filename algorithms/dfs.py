# dfs.py
import pygame


def algorithm(draw, grid, start, end):
    stack = []
    stack.append(start)
    discovered = []
    previous = {}
    while len(stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw()
        current = stack.pop()
        if current in discovered:
            continue
        if current == end:
            end.make_end()
            reconstruct_path(previous, end, draw)
            start.make_start()
            return True
        discovered.append(current)
        for neighbour in current.neighbours:
            if neighbour not in discovered:
                stack.append(neighbour)
                previous[neighbour] = current
                neighbour.make_open()

        current.make_closed()
        start.make_start()
    return False



def reconstruct_path(previous, current, draw):
    while current in previous:
        current = previous[current]
        current.make_path()
        draw()
