class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(row, col, memo):
            if (row, col) in memo:
                return memo[(row, col)]
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            elif row == m-1 and col == n-1:
                return 1
            
            for pos in [(row, col+1), (row+1, col)]:
                memo[(row, col)] += dfs(pos[0], pos[1], memo)
            return memo[(row, col)]
        return dfs(0, 0, defaultdict(int))