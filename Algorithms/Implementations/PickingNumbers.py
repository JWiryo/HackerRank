#!/bin/python

import sys

def pickingNumbers(a):
    max_num = 0
    for i in a:
        j = a.count(i)
        k = a.count(i-1)
        j = j + k
        if max_num < j:
            max_num = j
    return max_num

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = pickingNumbers(a)
    print result
