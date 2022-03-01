import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        counter = 1
        heaped = []
        ugly = -1
        
        while counter <= n:
            if len(heaped) == 0:
                heapq.heappush(heaped, counter)
            ugly = heapq.heappop(heaped)
            if not ugly * 2 in heaped:
                heapq.heappush(heaped, ugly*2)
            if not ugly * 3 in heaped:
                heapq.heappush(heaped, ugly*3)
            if not ugly * 5 in heaped:
                heapq.heappush(heaped, ugly*5)
            counter += 1
        return ugly