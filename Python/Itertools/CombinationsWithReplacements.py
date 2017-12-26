from __future__ import print_function
from itertools import combinations_with_replacement

Input = raw_input().split()

S = str(Input[0])
k = int(Input[1])

[print(''.join(words)) for words in list(combinations_with_replacement(sorted(S), k))]
