# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        even_count = 0
        if root == None:
            return even_count
        if root.val % 2 == 0:
            for cur in [root.right, root.left]:
                if cur and cur.left:
                    even_count += cur.left.val
                if cur and cur.right:
                    even_count += cur.right.val
        
        even_count += self.sumEvenGrandparent(root.left)
        even_count += self.sumEvenGrandparent(root.right)
        return even_count