#!/bin/python

import sys

def getTotalX(a, b):
    count = 0
    check = False
    xList = []
    for i in a:
        for j in a:
            x = i*j
            if x not in xList:
                xList.append(x)
    for x in xList:
        for i in a:
            for j in b:
                if x % i == 0 and j % x == 0:
                    check = True
        if check:
            count += 1
    return count

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total
