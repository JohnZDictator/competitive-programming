# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.moves = 0
    
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.postOrder(root)
        
        return self.moves
        
        
    
    def postOrder(self, node):
        if not node: return (0, 0)

        left = self.postOrder(node.left)
        right = self.postOrder(node.right)
        
        self.moves += abs(left[1] - left[0]) + abs(right[1] - right[0])

        return ( left[0] + right[0] + 1, left[1] + right[1] + node.val )

      
    #def countEmpty(self, root):
#         if root.right and not root.left:
#             if root.val == 0:
#                 return 1 + self.countEmpty(root.right)
            
#             return self.countEmpty(root.right)
        
#         elif root.left and not root.right:
#             if root.val == 0:
#                 return 1 + self.countEmpty(root.left) 
            
#             return self.countEmpty(root.left)
        
#         else:
#             if root.val == 0 and root.right == None and root.left == None:
#                 return 1
            
#             elif root.right == None and root.left == None:
#                 return 0
            
#             if root.val == 0:
#                 return 1 + self.countEmpty(root.right) + self.countEmpty(root.left)
            
             
#             return self.countEmpty(root.right) + self.countEmpty(root.left)
    
    
#     def countEmpty(self, root, count):
#         if root.right and not root.left:
#             if root.val == 0:
#                 count += 1
#             return count + self.countEmpty(root.right, count)
        
#         elif root.left and not root.right:
#             if root.val == 0:
#                 count += 1
#             return count + self.countEmpty(root.left, count)
        
#         else:
#             if root.val == 0 and root.right == None and root.left == None:
#                 return 1
#             elif root.right == None and root.left == None:
#                 return 0
            
#             if root.val == 0:
#                 count += 1
            
             
#             return count + self.countEmpty(root.right, count) + self.countEmpty(root.left, count)
        