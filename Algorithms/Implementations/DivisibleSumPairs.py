#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in xrange(len(ar)):
        for j in xrange(i, n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
