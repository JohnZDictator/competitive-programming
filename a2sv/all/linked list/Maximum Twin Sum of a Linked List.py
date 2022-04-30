# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        next_ = None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        itr = head
        max_twin_sum = -float('inf')
        while prev:
            max_twin_sum = max(max_twin_sum, itr.val + prev.val)
            itr = itr.next
            prev = prev.next
        
        return max_twin_sum