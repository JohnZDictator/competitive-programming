"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:

Input: root = [1,2,3]
Output: [1,3]

 

Constraints:

    The number of nodes in the tree will be in the range [0, 104].
    -231 <= Node.val <= 231 - 1


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        
        return self.helper(root, [], 0)
            
    def helper(self, root, output, level):
        if len(output) == level:
            output.append(root.val)
        
        if output[level] < root.val:
            output[level] = root.val
        
        # for child in [root.left, root.right]:
        #     if child:
        #         self.helper(child, output, level+1)
        
        if root.right:
            self.helper(root.right, output, level+1)
        if root.left:
            self.helper(root.left, output, level+1)
            
        return output