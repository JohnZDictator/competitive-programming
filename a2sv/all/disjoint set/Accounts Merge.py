class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        parent = [-1 for x in range(n)]
        rank = [0 for x in range(n)]

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            
            if parent_y == parent_x:
                return
            elif rank[parent_x] < rank[parent_y]:
                parent[parent_x] = parent_y
                rank[parent_y] += 1
            elif rank[parent_y] < rank[parent_x]:
                parent[parent_y] = parent_x
                rank[parent_x] += 1
            elif rank[parent_y] == rank[parent_x]:
                parent[parent_y] = parent_x
                rank[parent_x] += 1
            
        email_arr = []
        for i in range(n):
            m = len(accounts[i])
            email_set = set()
            for j in range(1, m):
                email_set.add(accounts[i][j])
            email_arr.append(email_set)
        
        
        for idx in range(n):
            account_name = accounts[idx][0]
            for i in range(n):
                if idx != i and account_name == accounts[i][0]:
                    m = len(accounts[idx])
                    for c in range(1, m):
                        if accounts[idx][c] in email_arr[i]:
                            union(idx, i)
        
        for i in range(n):
            parent_i = find(i)
            if parent_i != -1:
                for email_i in email_arr[i]:
                    if email_i not in email_arr[parent_i]:
                        email_arr[parent_i].add(email_i)
        
        
        union_email = []
        for i in range(n):
            if parent[i] == -1:
                parent_arr = []
                parent_arr.append(accounts[i][0])
                
                for email in email_arr[i]:
                    parent_arr.append(email)
                parent_arr[1:] = sorted(parent_arr[1:])
                union_email.append(parent_arr)
        
        return union_email