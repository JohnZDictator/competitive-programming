class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        rel = defaultdict(list)
        dependency_count = defaultdict(int)
        print(len(dependency_count))
        for course in prerequisites:
            rel[course[1]].append(course[0])
            dependency_count[course[0]] += 1
            
        
        stack = []
        for i in range(numCourses):
            if dependency_count[i] == 0:
                stack.append(i)
                dependency_count.pop(i)
                
        while stack:
            course_taken = stack.pop()
            for c in rel[course_taken]:
                dependency_count[c] -= 1
                if dependency_count[c] == 0:
                    stack.append(c)
                    dependency_count.pop(c)
                    
        if len(dependency_count) == 0:
            return True
        return False