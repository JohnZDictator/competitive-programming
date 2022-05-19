class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        def dp(m, n, memo):
            if (m, n) in memo:
                return memo[(m, n)]
            
            if m >= len(grid) and  n >= len(grid[0]):
                return 0
            
            if m >= len(grid) - 1 and n < len(grid[0]):
                memo[(m, n)] = dp(m + 1, n + 1, memo) + grid[len(grid) - 1][n]
                return memo[(m, n)]
            elif n >= len(grid[0]) - 1 and m < len(grid):
                memo[(m, n)] = dp(m + 1, n + 1, memo) + grid[m][len(grid[0]) - 1]
                return memo[(m, n)]
            
            memo[(m, n)] = min(dp(m + 1, n, memo), dp(m, n + 1, memo)) + grid[m][n]
            return memo[(m, n)]
        
        return dp(0, 0, {})