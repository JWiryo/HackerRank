#!/bin/python

import sys


n = int(raw_input().strip())

for i in xrange(n):
    stair = ""
    stair += " "*(n-1-i);
    stair += "#"*(i+1);
    print stair;
