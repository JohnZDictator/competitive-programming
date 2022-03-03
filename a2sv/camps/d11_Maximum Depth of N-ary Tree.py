"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
        
#         stack = [ root ]
        
#         while stack:
#             current = stack.pop()
#             print(current.val)    
#             for child in current.children:
#                 stack.append(child)
      
class Solution:
    def __init__(self):
        self.counter = 1
        self.maxDepthCounter = -1
    
    def dfsTraversal(self, root):
        if not root:
            self.maxDepthCounter = 0
            return 
        
        for node in root.children:
            self.counter += 1
            self.maxDepth(node)
            self.counter -= 1
        self.maxDepthCounter = max(self.maxDepthCounter, self.counter)
        
    
    def maxDepth(self, root: 'Node') -> int:
        self.dfsTraversal(root)
        
        return self.maxDepthCounter