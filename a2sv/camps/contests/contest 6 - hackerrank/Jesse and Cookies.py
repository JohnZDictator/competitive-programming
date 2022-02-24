#!/bin/python3

import heapq

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    n = len(A)
    heapq.heapify(A)
    counter = 0
    while True:
        if len(A) == 1:
            if A[0] >= k:
                return counter
            else:
                return -1
        elif A[0] >= k:
            return counter        
        mixedSweet = heapq.heappop(A)
        heapq.heapreplace(A, mixedSweet + 2*A[0])
        counter += 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
