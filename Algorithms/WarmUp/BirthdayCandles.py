#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    count = 0

    tallestCandle = max(ar);
    for i in ar:
        if i == tallestCandle:
            count += 1;

    return count;


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
