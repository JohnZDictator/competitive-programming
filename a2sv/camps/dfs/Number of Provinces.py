class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        connection = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    connection[i].append(j)
        
        visited = set()
        def dfs(city):
            visited.add(city)
            for c in connection[city]:
                if c not in visited:
                    dfs(c)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
                
        return count