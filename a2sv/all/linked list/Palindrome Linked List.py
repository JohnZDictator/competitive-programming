# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time complexity - O(n), Space complexity - O(n)
        # node_arr = []
        # while head:
        #     node_arr.append(head.val)
        #     head = head.next
        
        # right = len(node_arr) - 1
        # left = 0
        
        # while left < right:
        #     if node_arr[left] != node_arr[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # Time complexity - O(n), Space complexity - O(1) 
        # By reversing the nodes after the middle node
        # We find the middle using Tortoise-Hare algorithm 
        # 1. when the fast one finishes the list
        # 2. the place where the slow one stops become middle
        # Intuition => Because fast moves twice of the slow
        #           => So when fast finish the slow will be at the middle 
        # and comparing the elements with two pointers
        # 1. from head to middle
        # 2. from middle to end
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
       
        prev_node = None
        curr_node = slow
        next_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        while head and prev_node:
            if head.val != prev_node.val:
                return False
            head = head.next
            prev_node = prev_node.next
        return True