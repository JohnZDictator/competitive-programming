class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = defaultdict(int)
        outdegree = defaultdict(list)
        
        for i in range(n):
            for node in graph[i]:
                indegree[i] += 1
                outdegree[node].append(i)
        
        queue = collections.deque()
        for i in range(n):
            if indegree[i] == 0: 
                queue.append(i)
        
        safe_nodes = []
        while queue:
            curr = queue.popleft()
            safe_nodes.append(curr)
            
            for node in outdegree[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        
        safe_nodes.sort()
        return safe_nodes