# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.leftSum = 0
        self.rightSum = 0
        self.startNode = None
        self.counter = 0
        self.rootNodes = []
        
    def travRight(self, root):
        if root:
            self.rightSum += root.val
            self.travRight(root.right)
            self.travRight(root.left)
        
    def travLeft(self, root):
        if root:
            self.leftSum += root.val
            self.travLeft(root.right)
            self.travLeft(root.left)
        
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        
        if self.counter == 0:
            self.startNode = root
            if root == None:
                return 0
        
        self.counter += 1
        if root:
            self.rightSum, self.leftSum = 0, 0
            self.travRight(root.right)
            self.travLeft(root.left)
            root.val = abs(self.leftSum-self.rightSum)
            self.rootNodes.append(root.val)
            self.findTilt(root.right)
            self.findTilt(root.left)
        
        # root = self.startNode
        # if root:
        #     self.leftSum, self.rightSum = 0, 0
        #     self.travRight(root.right)
        #     self.travLeft(root.left)
        
        return sum(self.rootNodes)