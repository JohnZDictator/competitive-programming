class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.data = data
        self.right = right

def inOrderTraversal(root):
    if root == None:
        return
    
    if root.left != None:
        inOrderTraversal(root.left)
    
    print(root.data)
    if root.right != None:
        inOrderTraversal(root.right)