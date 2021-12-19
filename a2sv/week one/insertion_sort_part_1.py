#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    temp = arr[n-1]
    for i in reversed(range(n)):
        if i == 0:
            arr[i] = temp
            print(*arr)
            return
        elif temp < arr[i-1]:
            arr[i] = arr[i-1]
        elif temp > arr[i-1]:
            arr[i] = temp
            print(*arr)
            return 
        # printing a space separated list items
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
