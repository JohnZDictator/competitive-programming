class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [-1 for idx in range(n)]
        rank = [0 for idx in range(n)]
        
        def find(a):
            if parent[a] == -1:
                return a
            return find(parent[a])
        
        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)
            
            if parent_a == parent_b:
                return
            elif rank[parent_a] < rank[parent_b]:
                parent[parent_a] = parent_b
                rank[parent_b] += 1
            elif rank[parent_b] < rank[parent_a]:
                parent[parent_b] = parent_a
                rank[parent_a] += 1
            elif rank[parent_a] == rank[parent_b]:
                parent[parent_a] = parent_b
                rank[parent_b] += 1
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    union(i, j)
        
        numProvinces = 0
        for idx in range(n):
            if parent[idx] == -1:
                numProvinces += 1
        
        return numProvinces