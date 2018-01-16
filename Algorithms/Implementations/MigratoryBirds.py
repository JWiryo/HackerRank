#!/bin/python

import sys
import operator

def migratoryBirds(n, ar):
    birdDict = {}
    for bird in ar:
        if bird not in birdDict:
            birdDict[bird] = 1
        else:
            birdDict[bird] = birdDict[bird] + 1
    return max(birdDict.iteritems(), key=operator.itemgetter(1))[0]



n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
