from __future__ import print_function
from itertools import groupby

S = str(raw_input())

[print((len(list(g)), int(k)), end=' ') for k, g in groupby(S)]
