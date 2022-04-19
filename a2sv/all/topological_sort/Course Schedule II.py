class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        indegree = defaultdict(int)
        outdegree =defaultdict(list)
        
        for i in range(n):
            indegree[prerequisites[i][0]] += 1
            outdegree[prerequisites[i][1]].append(prerequisites[i][0])
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0: queue.append(i)
        
        course_order = []
        while queue:
            curr = queue.popleft()
            course_order.append(curr)
            for course in outdegree[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        if len(course_order) != numCourses:
            return []
        return course_order