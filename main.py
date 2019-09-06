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
    print("Informe os movimentos iniciais separados por virgula sentido horário (1-R-1, 1-L-1, 1-U-1, 1-D-1, 1-F-1, 1-B-1), giros duplos (1-R-2, 1-L-2, 1-U-2, 1-D-2, 1-F-2, 1-B-2), duplos sentindo anti-horário (1-R-3, 1-L-3, 1-U-3, 1-D-3, 1-F-3, 1-B-3): ")
    sequence = input()
    if sequence == None or sequence == "":
        cubes[0].scramble(cubes[0].cube, moves)
    else:
        cubes[0].scramble(cubes[0].cube, moves, sequence)

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
