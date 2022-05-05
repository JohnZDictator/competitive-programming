class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        visited = set()
        total_area = 0
        def dfs(i, j):
            total_area = 0
            for x, y in [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1 and (x, y) not in visited:
                    visited.add((x, y))
                    total_area += 1 + dfs(x, y)
            return total_area
            
        
        max_area = 0
        for i in range(n):  
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))
                    
        return max_area