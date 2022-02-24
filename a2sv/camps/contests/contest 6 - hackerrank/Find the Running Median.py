#!/bin/python3

import heapq

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    maxHeap = []
    minHeap = []
    median = []
    counter = 0
    while counter < len(a):
        if len(minHeap) < len(maxHeap):
            if -maxHeap[0] > a[counter]:
                maxVal = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, -maxVal)
                heapq.heappush(maxHeap, -a[counter])
            else:
                heapq.heappush(minHeap, a[counter])
        elif len(minHeap) == len(maxHeap):
            if len(minHeap) > 0 and minHeap[0] < a[counter]:
                minVal = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -minVal)
                heapq.heappush(minHeap, a[counter])
            else:
                heapq.heappush(maxHeap, -a[counter])
        else:
            if minHeap[0] < a[counter]:
                maxVal = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -maxVal)
                heapq.heappush(minHeap, a[counter]) 
            else:
                heapq.heappush(maxHeap, -a[counter])
        if len(maxHeap) > len(minHeap):
            median.append(-maxHeap[0])
        elif len(minHeap) > len(maxHeap):
            median.append(minHeap[0])
        else:
            median.append((minHeap[0]+(-maxHeap[0]))/2)
        counter += 1
    return median

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
