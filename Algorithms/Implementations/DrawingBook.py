#!/bin/python

import sys
import math

def solve(n, p):
    fromStart = math.ceil(abs(p-1)/2.0)
    fromEnd = math.floor(abs(n-p)/2.0)
    if p == n-1 and n % 2 == 0 and n != 2:
        return 1
    elif fromStart < fromEnd:
        return int(fromStart)
    else:
        return int(fromEnd)

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
