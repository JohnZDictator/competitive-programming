class Graph:
    def __init__(self, graph):
        self.graph = graph
    
    def depthFirst(self, source):
        stack = [ source ]
        
        while len(stack) > 0:
            current = stack.pop()
            print(current)

            for node in self.graph[current]:
                stack.append(node)
    
    def depthFirstRecursion(self, source):
        print(source)

        for node in self.graph[source]:
            self.depthFirstRecursion(node)
    
    def breadthFirst(self, source):
        queue = [ source ]

        while len(queue) > 0:
            current = queue.pop(0)
            print(current)

            for node in self.graph[current]:
                queue.append(node)


if __name__ == '__main__':
    adjacencyList = {
        'a': ['b','c'], 
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    
    graph = Graph(adjacencyList)
    # graph.depthFirst(graph, 'a')
    # graph.breadthFirst(graph, 'a')

    graph.depthFirstRecursion('a')