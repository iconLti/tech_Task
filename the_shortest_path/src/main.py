from config import *
from random import random
from functions import find_shortest_path
from colorful_bfs import graphical_rep_of_bfs

matrix = [[1 if random() < 0.2 else 0 for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    
    print(f"main matrix:\n{'-' * 12}")
    for row in matrix:
        print(*row)

    shortest_path = find_shortest_path(matrix)
    print(f"{'-' * 18}\nshortest_path:", shortest_path)
    
    graphical_rep_of_bfs(matrix)