#!/bin/python

import sys

def hurdleRace(k, height):
    return max(max(height)-k,0)

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = map(int, raw_input().strip().split(' '))
    result = hurdleRace(k, height)
    print result
