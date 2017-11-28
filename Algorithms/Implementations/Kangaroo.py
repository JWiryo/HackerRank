#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if (x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2):
        return 'NO';
    else:
        if(abs(x2 - x1) % abs(v2 - v1) == 0):
            return 'YES';
        else:
            return 'NO';

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
