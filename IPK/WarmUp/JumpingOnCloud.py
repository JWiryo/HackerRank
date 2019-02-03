
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    noOfJump = 0
    counter = 0

    while counter < len(c) - 2:
        print(counter)
        if c[counter + 2] != 1:
            counter += 2
            noOfJump += 1
        else:
            counter += 1
            noOfJump += 1
    if counter < len(c) - 1:
        counter += 1
        noOfJump += 1;

    return noOfJump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
