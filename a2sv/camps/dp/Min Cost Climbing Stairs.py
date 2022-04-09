class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def findMinCost(costs, index):
            if index in memo: 
                return memo[index]
            
            if index == n - 1:
                return costs[index]
            elif index >= n:
                return 0
            
            left = findMinCost(costs, index + 1)
            right = findMinCost(costs, index + 2)
            
            memo[index] = min(left, right) + costs[index] 
            
            return memo[index]
            
        
        return min( findMinCost( cost, 0 ), findMinCost( cost, 1 ) )