import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heaped = []
        ans = None
        counter = 0
        
        for num in nums:
            heapq.heappush(heaped, -num)
        
        while counter < k:
            ans = heapq.heappop(heaped)
            counter += 1
        return -ans