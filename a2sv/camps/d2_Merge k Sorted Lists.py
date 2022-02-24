# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heaped = []
        ans = None
        
        for i in lists:
            while i:
                heapq.heappush(heaped, i.val)
                i = i.next
        
        if len(heaped) == 0: 
            return None
        
        start = ListNode(heapq.heappop(heaped))
        ans = start
        
        while len(heaped) > 0:
            node = ListNode(heapq.heappop(heaped))
            ans.next = node
            ans = ans.next
        
        ans = start
        return ans