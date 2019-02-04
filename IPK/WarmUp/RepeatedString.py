#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    noOfA = 0
    noOfAInShortString = s.count('a')

    floorResult = n // len(s)
    noOfA = noOfAInShortString * floorResult

    remainderString = n - len(s) * floorResult
    if remainderString == len(s):
        noOfA += noOfAInShortString
    elif remainderString == 0:
        return noOfA
    else:
        noOfA = noOfA + s[0:remainderString].count('a')
    return noOfA

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

# This cannot handle very large number
# def repeatedString(s, n):
#     noOfA = 0
#     s = s * n
#
#     for i in range(n):
#         if s[i] == "a":
#             noOfA += 1
#
#     return noOfA

# Brute Force Method
# def repeatedString(s, n):
#     noOfA = 0
#     noOfAInShortString = 0
#     remainderACount = 0
#
#     for char in s:
#         if char == 'a':
#             noOfA += 1
#             noOfAInShortString += 1
#
#     floorResult = n // len(s)
#     noOfA = noOfA * floorResult
#
#     remainderString = n - len(s) * floorResult
#     print(remainderString)
#     if remainderString == len(s):
#         noOfA += noOfAInShortString
#     elif remainderString == 0:
#         return noOfA
#     else:
#         for finalChar in s[0:remainderString]:
#             if finalChar == 'a':
#                 remainderACount += 1
#     return noOfA + remainderACount