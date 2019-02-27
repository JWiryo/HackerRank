#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
def maxRegion(grid):
    def dfs(grid, i, j):
        positions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        n = len(grid)
        m = len(grid[0])

        grid[i][j] = 0
        counter = 1

        for p in positions:
            if i + p[0] in range(n) and j + p[1] in range(m):
                if grid[i + p[0]][j + p[1]] == 1:
                    counter += dfs(grid, i + p[0], j + p[1])
        return counter

    n = len(grid)
    m = len(grid[0])
    maxSize = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                maxSize = max(maxSize, dfs(grid, i, j))

    return maxSize


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
