#!/bin/python

import sys


def getTotalX(a, b):
    count = 0

    for x in xrange(max(a), min(b) + 1):
        if all(x % i == 0 for i in a) and all(j % x == 0 for j in b):
            count += 1
    return count


if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total
