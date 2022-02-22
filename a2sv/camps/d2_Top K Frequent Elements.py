import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        output = []
        for key, value in frequency.items():
            heapq.heappush(output, (value, key))
            if  len(output) > k:
                heapq.heappop(output)
        ans = [output[i][1] for i in range(len(output))]
        return ans