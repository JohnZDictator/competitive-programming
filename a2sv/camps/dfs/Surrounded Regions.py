class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(x, y):
            visited.add((x, y))
            if board[x][y] == 'O':
                for pos in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 > pos[0] or pos[0] >= m or 0 > pos[1] or pos[1] >= n:
                        continue
                    elif board[pos[0]][pos[1]] == 'O' and pos not in visited:
                        dfs(pos[0], pos[1])
                        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
