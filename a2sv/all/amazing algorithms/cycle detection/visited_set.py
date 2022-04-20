"""
Set Cycle detection
=> This cycle detection uses set data structure.
    => If the node has been visited there indicates there is a cylce there
    => Elif the node will be stored as visited and go to the next node
=> Complexity Analysis:
    => Time complexity: O(n)
    => Space complexity: O(n) - because we store each linked list element on to the set
"""
def cycleDetection(llist):
    visited = set()
    itr = llist.head

    while itr:
        if itr.data in visited:
            return 1
        else:
            visited.add(itr.data)
            itr = itr.next
    return 0