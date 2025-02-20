from collections import deque
from config import *

def get_rect(x, y):
    """
    Get coordinates for tile in matrix;
    each tile is 1 in the main matrix;;
    """
    return x * TILE, y * TILE, TILE - 2, TILE - 2

def get_next_nodes(x, y, matrix):
    """
    Check the possibility of passage
    """
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not matrix[y][x] else False
    ways = ([-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1])
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def create_graph(matrix):
    """
    create a dict of adjacency lists
    """
    graph = {}
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if not col:  #  col == 0, we can get through this tile
                graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y, matrix)
                
    return graph

def bfs(start, goal, graph):
    """
    Breadth First Search (BFS)
    """
    queue = deque([start])
    visited = {start: None}
    
    while queue: 
        cur_node = queue.popleft()  
        if cur_node == goal:
            break        
        next_nodes = graph[cur_node]       
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    
    return visited

def find_shortest_path(matrix):
    """
    main task;
    Finding the shortest path from the start (0,0) to the goal (n-1, n-1)
    """
    graph = create_graph(matrix)
    #  restore path
    if start in graph:
        visited = bfs(start, goal, graph)
        count_tiles = 1

        cur_node = goal

        if goal in visited:
            while cur_node != start:
                cur_node = visited[cur_node]
                count_tiles += 1
            return count_tiles
        else:
            return -1
    else:
        return -1