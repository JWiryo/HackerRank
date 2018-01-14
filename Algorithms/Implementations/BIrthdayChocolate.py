#!/bin/python

import sys

def solve(n, s, d, m):
    totalCount = 0
    for i in xrange(len(s)):
        currentSum = 0
        mLength = 0
        index = i
        while mLength < m and index < len(s):
            currentSum += s[index]
            index += 1
            mLength += 1
        if currentSum == d:
            totalCount += 1
    return totalCount

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
