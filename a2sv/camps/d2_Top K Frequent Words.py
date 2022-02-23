import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heaped = []
        ans = []
        
        for key, value in frequency.items():
            heapq.heappush(heaped, (-value, key))
        while len(ans) < k:
            ans.append(heapq.heappop(heaped)[1])
        return ans