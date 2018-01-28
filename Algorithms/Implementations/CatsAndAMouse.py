#!/bin/python

import sys

def catAndMouse(x, y, z):
    resultList = []
    if abs(x-z) < abs(y-z):
        resultList.append("Cat A")
    elif abs(y-z) < abs(x-z):
        resultList.append("Cat B")
    else:
        resultList.append("Mouse C")
    return resultList

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print " ".join(map(str, result))



