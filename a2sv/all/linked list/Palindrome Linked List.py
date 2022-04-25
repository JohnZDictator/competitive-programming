# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time complexity - O(n), Space complexity - O(n)
        node_arr = []
        while head:
            node_arr.append(head.val)
            head = head.next
        
        right = len(node_arr) - 1
        left = 0
        
        while left < right:
            if node_arr[left] != node_arr[right]:
                return False
            left += 1
            right -= 1
        return True