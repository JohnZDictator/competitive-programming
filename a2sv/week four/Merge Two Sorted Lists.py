# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        counter = 0
        first_node = None
        
        while l1 or l2:
            if not l1:
                if counter == 0:
                    return l2
                output.next = l2
                break
            elif not l2:
                if counter == 0:
                    return l1
                output.next = l1
                break
            else:
                if l1.val <= l2.val:
                    if counter == 0:
                        first_node = ListNode(l1.val)
                        output = first_node
                    else:
                        node = ListNode(l1.val)
                        output.next = node
                    l1 = l1.next
                else:
                    if counter == 0:
                        first_node = ListNode(l2.val)
                        output = first_node
                    else:
                        node = ListNode(l2.val)
                        output.next = node
                    l2 = l2.next
            
            if counter != 0:
                output = output.next
            counter += 1
            
        output = first_node
        return output
                
