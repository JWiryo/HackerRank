#!/bin/python

import sys

def countingValleys(n, s):
    curLevel = 0
    valleyCount = 0
    for step in list(s):
        if step == 'U':
            curLevel += 1
        else:
            curLevel -= 1
        if curLevel == 0 and step == 'U':
            valleyCount += 1
    return valleyCount

if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    result = countingValleys(n, s)
    print result
