import queue
from collections import defaultdict


class Graph:

    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        q = queue.Queue()
        distancesList = []
        unvisited = set()

        for i in range(n):
            distancesList.append(-1)
            unvisited.add(i)

        distancesList[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distancesList[node]

            for child in children:
                if child in unvisited:
                    distancesList[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distancesList.pop(root)
        print(" ".join(map(str, distancesList)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)

