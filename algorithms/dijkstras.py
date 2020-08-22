# dijkstras.py
import pygame
from queue import PriorityQueue


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    previous = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(previous, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                previous[neighbour] = current
                g_score[neighbour] = temp_g_score
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((g_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False


def reconstruct_path(previous, current, draw):
    while current in previous:
        current = previous[current]
        current.make_path()
        draw()
