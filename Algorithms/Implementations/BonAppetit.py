#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    bActual = sum(ar) - ar[k]
    if bActual/2 == b:
        return 'Bon Appetit'
    else:
        return str(abs(bActual/2 - b))



n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
