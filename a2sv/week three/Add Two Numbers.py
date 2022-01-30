# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        itrl1 = l1
        itrl2 = l2
        
        node = ListNode()
        itr = node
        while itrl1 or itrl2:
            # checking if the linked lists are None or not
            # getting their values if they are not None
            # if None setting their values to zero
            op1 , op2, rem = 0, 0, 0
            if itrl1:
                op1 = itrl1.val
            if itrl2: 
                op2 = itrl2.val
            
            # Sum part
            if op1 + op2 + itr.val > 9:
                itr.val += op1 + op2 - 10
                rem = 1
            else:
                itr.val += op1 + op2 
            
            # iterating through input linked lists
            if itrl1:
                itrl1 = itrl1.next
            if itrl2:
                itrl2 = itrl2.next
            
            # creating new node to store the sum as long as node is diff from none
            if itrl1 or itrl2:
                newNode = ListNode()
                if op1 + op2 + rem > 9:
                    newNode.val = 1
                    rem = 0
                itr.next = newNode
            elif rem == 1:
                newNode = ListNode()
                newNode.val = 1
                itr.next = newNode
            itr = itr.next
        itr = node
        return itr