from __future__ import print_function
from itertools import combinations

Input = raw_input().split()

S = str(Input[0])
k = int(Input[1])

[print(''.join(words)) for i in xrange(1, k + 1) for words in list(combinations(sorted(S), i))]
