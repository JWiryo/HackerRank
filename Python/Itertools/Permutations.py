from __future__ import print_function
from itertools import permutations

Input = raw_input().split()

S = str(Input[0])
k = int(Input[1])

for words in list(permutations(S,k)):
    print(''.join(words))