#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()

    minNumInArr = min(arr)
    arr.remove(minNumInArr)
    minDiff = abs(arr[1] - minNumInArr)

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < minDiff:
            minDiff = arr[i] - arr[i - 1]
    return minDiff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
