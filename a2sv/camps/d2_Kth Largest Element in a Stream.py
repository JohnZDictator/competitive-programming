import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heaped = []
        self.counter = 0
        
    def add(self, val: int) -> int:
        self.nums.append(val)
        while self.counter < len(self.nums):
            if len(self.heaped) < self.k:
                heapq.heappush(self.heaped, self.nums[self.counter])
            else:
                if self.nums[self.counter] > self.heaped[0]:
                    heapq.heappush(self.heaped, self.nums[self.counter])
                    heapq.heappop(self.heaped)
            self.counter += 1
        return self.heaped[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)