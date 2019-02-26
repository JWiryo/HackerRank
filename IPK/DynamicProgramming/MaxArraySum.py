#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    memo = {}
    memo[0] = arr[0]
    memo[1] = max(arr[0], arr[1])

    for i in range(2,len(arr)):
        memo[i] = max(arr[i], memo.get(i-1), memo[i-2]+arr[i])
    return memo.get(len(arr)-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
