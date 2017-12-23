from __future__ import print_function
from itertools import product

A = [int(a) for a in raw_input().split()]
B = [int(b) for b in raw_input().split()]

print(*list(product(A, B)), sep=' ')
