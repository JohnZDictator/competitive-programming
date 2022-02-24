#!/bin/python3

import heapq

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

def minimumAverage(customers):
    n = len(customers)
    waiting_time = 0
    currentTime = 0
    currentTime = 0
    heaped = []
    counter = 0
    popper = 0
    
    customers.sort()
    
    while popper < len(customers):
        if counter < len(customers) and len(heaped) == 0 and currentTime < customers[counter][0]:
            currentTime = customers[counter][0]
        if counter < len(customers)and customers[counter][0] <= currentTime:
            heapq.heappush(heaped, (customers[counter][1], customers[counter][0]))
            counter += 1
        else:
            popped = heapq.heappop(heaped)
            currentTime += popped[0]
            waiting_time += currentTime - popped[1]
            popper += 1
            
    return waiting_time//n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
 