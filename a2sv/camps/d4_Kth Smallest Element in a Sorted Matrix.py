import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        counter = 0
        heaped = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(heaped, matrix[i][j])
        
        while counter < k:
            ans = heapq.heappop(heaped)
            counter += 1
        return ans