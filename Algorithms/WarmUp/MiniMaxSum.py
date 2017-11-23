#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))

Total = sum(arr);
minSum = Total - max(arr);
maxSum = Total - min(arr);

print str(minSum) + ' ' + str(maxSum);