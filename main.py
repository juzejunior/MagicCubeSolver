import os

from cube import Cube
from solver import Solver
from pprint import pprint
import time

if __name__ == '__main__':
    n = [2, 2]  # 2 - 5
    d = [3, 3]  # 1 - 5
    time_out = 300
    start_time = "2"
    dirName = f'results/{start_time}'
    cubes = []

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    cubes = []
    for i in range(d[0], d[1] + 1):
        for j in range(n[0], n[1] + 1):
            cube = Cube(j, i)
            cubes.append(cube)
    print("ESTADO META: ")
    print(cubes[0].print_cube())
    moves = 2
    cubes[0].scramble(cubes[0].cube, moves)
    print("Depois de Misturar: ")
    print(cubes[0].print_cube())
    cubes[0].start = cubes[0].cube

    cubes[0].print_sequence()
    print("Informe qual algoritmo deseja utilizar (1 - bfs, 2 - A*): ")
    algorithm = int(input())
    if algorithm == 1:
        Solver(cubes[0], 'BFS', time_out, start_time).solve()
    elif algorithm == 2:
        Solver(cubes[0], 'A* 0', time_out, start_time).solve()

    print("Resolvido: ")
    print(cubes[0].print_cube())
