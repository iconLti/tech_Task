import pygame as pg
from collections import deque
from config import *
from functions import *


def graphical_rep_of_bfs(matrix):
    graph = create_graph(matrix)
    
    pg.init()
    queue = deque([start])
    visited = {start: None}
    cur_node = start

    screen = pg.display.set_mode([cols * TILE, rows * TILE])
    clock = pg.time.Clock()

    while True:
        #  screen fill
        screen.fill(pg.Color('black'))
        #  draw matrix
        for y, row in enumerate(matrix):
            for x, col in enumerate(row):
                if col:
                    pg.draw.rect(screen, pg.Color('darkred'), get_rect(x, y))

        if start in graph:
            #  draw BFS
            found_goal = goal in visited
            if not found_goal:
                for x, y in visited:
                    pg.draw.rect(screen, pg.Color('gainsboro'), get_rect(x, y))
                for x, y in queue:
                    pg.draw.rect(screen, pg.Color('maroon'), get_rect(x, y))

                #  logic
                if queue:
                    cur_node = queue.popleft()
                    if cur_node != goal:
                        next_nodes = graph[cur_node]
                        for next_node in next_nodes:
                            if next_node not in visited:
                                queue.append(next_node)
                                visited[next_node] = cur_node

        #  path
        path_segment = goal
        count = 0
        while path_segment and path_segment in visited:
            pg.draw.rect(screen, pg.Color('lime'), get_rect(*path_segment), TILE, border_radius=TILE // 3)
            path_segment = visited[path_segment]
            count += 1
        pg.draw.rect(screen, pg.Color('dimgray'), get_rect(*start), border_radius=TILE // 3)
        pg.draw.rect(screen, pg.Color('dimgray'), get_rect(*goal), border_radius=TILE // 3)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        pg.display.flip()
        clock.tick(30)