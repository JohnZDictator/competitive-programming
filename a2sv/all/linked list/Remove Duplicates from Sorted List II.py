# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicates = set()
        
        itr = head
        while itr and itr.next:
            if itr.val == itr.next.val:
                if itr.val not in duplicates:
                    duplicates.add(itr.val)
            itr = itr.next
        
        while head and head.val in duplicates:
            head = head.next
        
        itr = head
        while itr and itr.next:
            if itr.next.val in duplicates:
                jump = itr.next
                while jump and jump.val in duplicates:
                    jump = jump.next
                itr.next = jump
            itr = itr.next
        
        return head