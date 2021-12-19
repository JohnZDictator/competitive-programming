#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    curr_height_level = 0
    prev_height_level = 0
    valley_count = 0
    for i in range(steps):
        prev_height_level = curr_height_level
        if path[i] == 'D':
            curr_height_level -= 1
        elif path[i] == 'U':
            curr_height_level += 1
        if prev_height_level == 0 and curr_height_level < 0:
            valley_count += 1
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
