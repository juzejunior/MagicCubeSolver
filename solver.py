import itertools
import time
from queue import PriorityQueue


def save(algorithm, total_time, nodes, n, sequence, start_time, max_mem, depth):
    dados = {
        'algorithm': algorithm,
        'sequence': sequence,
        'time': total_time,
        'nodes': nodes,
        'memory': max_mem,
        'depth': depth
    }
    file = open(f'results/{start_time}/{n}.txt', 'a')
    file.write(str(dados) + "\n")
    file.close()


class Solver:
    def __init__(self, problem, algorithm='BFS', time_limit=float('inf'), start_time=0):
        self.num_visited = 0
        self.algorithm = algorithm
        self.problem = problem
        self.time_limit = time_limit
        self.start_time = start_time
        self.start = 0
        self.max_mem = -1

    def solve(self):
        result = None
        self.start = time.time()
        print(self.algorithm)
        if self.algorithm == 'BFS':
            result = self.BFS()
        elif self.algorithm == 'A* 0':
            result = self.ASTAR(0)
        end = time.time()
        self.problem.print_sequence(result)
        if result != 'TimeOut':
            print(str(round(end - self.start, 3))+" s")
            save(self.algorithm, end - self.start, self.num_visited, self.problem.n,
                 self.problem.sequence[:-1], self.start_time, self.max_mem, str(self.problem.sequence).count(","))
        return

    def print_nodes(self):
        pass
        #print(f'\rNós visitados: {self.num_visited}', end='')

    def BFS(self):
        queue = ['']
        visited = [str(self.problem.cube)]
        print("a VISITAR:")
        print(visited)
        while queue:
            if (time.time() - self.start) > self.time_limit:
                return 'TimeOut'
            self.print_nodes()
            self.num_visited += 1
            if self.max_mem < len(queue):
                self.max_mem = len(queue)

            path = queue.pop(0)

            for neighbour in self.problem.successors(path):
                new_path = f'{path}{neighbour},'
                solution, cube = self.problem.is_target(new_path)

                if str(cube) not in visited:
                    if solution:
                        return new_path
                    queue.append(new_path)
                    visited.append(str(cube))

    def heuristic1(self):
        total = 0
        for face in ['R', 'L', 'U', 'D', 'F', 'B']:
            for cube in self.problem.cube[face]:
                for c in cube:
                    if c[0] != face:
                        total += 1
        return total

    def ASTAR(self, heuristic):
        queue = PriorityQueue()
        queue.put((0, ''))
        cost_so_far = {'': 0}
        visited = [str(self.problem.cube)]

        while queue:
            if (time.time() - self.start) > self.time_limit:
                return 'TimeOut'
            self.print_nodes()
            self.num_visited += 1
            if self.max_mem < queue.qsize():
                self.max_mem = queue.qsize()

            cost, path = queue.get_nowait()

            for neighbour in self.problem.successors(path):
                new_path = f'{path}{neighbour},'
                new_cost = cost + 1
                solution, cube = self.problem.is_target(new_path)

                if str(cube) not in visited:
                    if solution:
                        return new_path

                    if neighbour not in cost_so_far or new_cost < cost_so_far[new_path]:
                        cost_so_far[new_path] = new_cost
                        priority = new_cost + self.heuristic1()
                        queue.put((priority, new_path))
                        visited.append(str(cube))
