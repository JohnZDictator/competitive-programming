class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def dp(idx, row, memo):
            if (row, idx) in memo:
                return memo[(row, idx)]
            if row >= len(triangle):
                return 0
            if idx >= len(triangle[row]):
                return 0
            memo[(row, idx)] = min(dp(idx, row + 1, memo), dp(idx + 1, row + 1, memo)) + triangle[row][idx]
            return memo[(row, idx)]
        
        return dp(0, 0, {})