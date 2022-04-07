class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = None
        node = None
        for i in range(1, n + 1):
            if not head:
                head = Node(i)
                node = head
            else:
                head.next = Node(i)
                head = head.next
        head.next = node 
        
        head = node
        t = k
        while n > 1:
            if k == 1 or (k == n + 2 and k != t):
                k = n + 1
            
            count = 2
            while count < k:
                head = head.next
                count += 1
             
            head.next = head.next.next
            head = head.next
            
            n -= 1
                
        return head.val