#!/bin/python

import sys

n = int(raw_input().strip())
a = []

primarySum = 0;
secondarySum = 0;

for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)
    primarySum += a[a_i][a_i];
    secondarySum += a[a_i][n-1-a_i];

print abs(primarySum - secondarySum);