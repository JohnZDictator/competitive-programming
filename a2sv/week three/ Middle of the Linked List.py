# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        itr = head
        while itr:
            count += 1
            itr = itr.next
            
        counter = 0
        while head:
            if counter == count // 2:
                return head
            head = head.next
            counter += 1
            