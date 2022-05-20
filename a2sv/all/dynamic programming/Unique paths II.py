class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
            
        def dfs(row, col, memo):
            unique_paths = 0
            if (row, col) in memo:
                return memo[(row, col)]
            if obstacleGrid[row][col] == 1:
                return 0
            elif row == m-1 and col == n-1:
                return 1
            for pos in [(row, col+1), (row+1, col)]:
                if  0 <= pos[0] < m and 0 <= pos[1] < n:
                    memo[(row, col)] += dfs(pos[0], pos[1], memo)
            return memo[(row, col)]
        return dfs(0, 0, defaultdict(int))