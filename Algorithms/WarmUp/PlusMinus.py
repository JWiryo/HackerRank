#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

positiveCount = 0;
negativeCount = 0;
zeroCount = 0;

for i in arr:
    if i > 0:
        positiveCount += 1;
    if i < 0:
        negativeCount += 1;
    if i == 0:
        zeroCount += 1;

print str(float(positiveCount)/n)
print str(float(negativeCount)/n)
print str(float(zeroCount)/n);