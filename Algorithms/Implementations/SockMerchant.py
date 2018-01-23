#!/bin/python

import sys

def sockMerchant(n, ar):
    count = 0
    sock_dict = {}
    for i in ar:
        if i in sock_dict:
            sock_dict[i] += 1
        else:
            sock_dict[i] = 1

    for key, value in sock_dict.iteritems():
        count += value/2
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
