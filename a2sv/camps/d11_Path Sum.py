# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.isTargetSum = False
        self.nodeSum = 0
        
    def dfsTraversal(self, root, targetSum):
        if not root:
            pass
        else:
            self.nodeSum += root.val
            self.dfsTraversal(root.left, targetSum)
            self.dfsTraversal(root.right, targetSum)
            
            if not root.right and not root.left:
                print(self.nodeSum, root.val)
                if self.nodeSum == targetSum:
                    self.isTargetSum = True
            self.nodeSum -= root.val
            
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.dfsTraversal(root, targetSum)
        
        return self.isTargetSum