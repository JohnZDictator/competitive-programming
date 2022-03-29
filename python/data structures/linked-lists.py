class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, val):
        node = Node(val, self.head)
        self.head = node
    def insertAtEnd(self, val):
        itr = self.head
        while itr.next:
            itr = itr.next
        
        node = Node(val, None)
        itr.next = node
    
    def insertAtIndex(self, val, index):
        itr = self.head
        if index == 0:
            node = Node(val, self.head)
            self.head = node
            return 

        for i in range(index-1):
            if itr:
                itr = itr.next
            else:
                raise Exception("Index Out of Range")
        
        node = Node(val, itr.next)
        itr.next = node

    def printOut(self):
        itr = self.head
        sstr = ''
        while itr:
            sstr += str(itr.val) + '-->'
            itr = itr.next
        print(sstr)


if __name__ == '__main__':
    s = SinglyLinkedList()
    s.printOut()
    s.insertAtStart(4)
    s.insertAtEnd(5)
    s.insertAtStart(3)
    s.printOut()
    s.insertAtIndex(10, 0)
    s.insertAtIndex(1,1)
    s.insertAtEnd(100)
    s.insertAtStart(0)
    s.printOut()