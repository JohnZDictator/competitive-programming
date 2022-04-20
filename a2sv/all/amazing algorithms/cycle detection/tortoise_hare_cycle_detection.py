"""
Cycle Detection Algorithm => Tortoise and Hare(rabbit) algorithm
=> This algorithm is used to detect cycles in LinkedList.
    => we have 2 pointers slow and fast pointers
        - if fast pointer is None it is evident that there is no cycle found on the list
            (if there is a cycle None which is end of the linked list is not reachable) 
        - slow pointer will move 1 step at a time.
        - fast pointer will move 2 step at a time.
        - if slow and fast meet(they will meet some place in between the cycle 
            not necessarily at the entry point of the cycle)
    => to find the entry point of the cycle
        - break at node the slow and fast pointer met
        - let the slow pointer start at head of linked list
        - let the fast pointer move 1 step at a time
        - then necessarily the place where they meet will be the entry point of cycle
=> Complexity Analysis
    => Time Complexity = O(n)
    => Space Complexity = O(1)
"""
def cycleDetection(llist):
    slow = llist.head
    fast = llist.head
    met = False
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            met = True
            break
    if not met:
        return None
    else:
        slow = llist.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
    return slow
