import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heaped = []
        
        if len(stones) == 1:
            return stones[0]
        
        for i in range(len(stones)):
            heapq.heappush(heaped, -stones[i])
        
        while len(heaped) > 1:
            popped = heapq.heappop(heaped)
            if popped != heaped[0]:
                heapq.heapreplace(heaped, -heaped[0]+popped)
            else:
                heapq.heappop(heaped)
        
        if len(heaped) == 0:
            return 0
        
        return -heaped[0]