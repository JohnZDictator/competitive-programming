import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heaped = []
        
        for i in range(n-1):
            h = heights[i+1] - heights[i]
            if h < 0: 
                continue
            
            heapq.heappush(heaped, h)
            if len(heaped) > ladders:
                min_h = heapq.heappop(heaped)
                bricks -= min_h
            
            if bricks < 0:
                return i        
        
        return n-1

"""
Use the ladder to the largest height difference seen yet whil traversing through arr of heights.
And use the bricks when you run out of ladders and use them for small height difference.
The ideal data structure to keep track of min and max height elements in this case is heap.

#implementation idea
If i use heap i can store larger height differences that can be handled by my ladders.
If i run out of ladders i will pop off small heights and use bricks to handle them.
If i run out of bricks i will return the current furthest building i reached.
If i cross all my building i will return length of my buildings - 1.
"""