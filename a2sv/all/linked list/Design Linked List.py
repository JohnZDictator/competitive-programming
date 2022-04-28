class Node:
    def __init__(self, val, lnext=None):
        self.val = val
        self.next = lnext
        
class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def printOut(self):
        itr = self.head
        while itr:
            print(itr.val)
            itr = itr.next
    
        
    def get(self, index: int) -> int:
        
        # print('get:>>>')
        # self.printOut()
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index:
                return itr.val
            itr = itr.next
            counter += 1
        return -1
        
        
    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        # print('addAtHead:>>>')
        # self.printOut()
        
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        itr = self.head
        if self.head == None:
            self.head = newNode
        else:
            while itr.next:
                itr = itr.next
            itr.next = newNode
        # print('addAtTail:>>>')
        # self.printOut()

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        
        newNode = Node(val)
        counter = 1
        itr = self.head
        while itr:
            if index == counter:
                newNode.next = itr.next
                itr.next = newNode
                break
            counter += 1
            itr = itr.next
        
        # print('addAtIndex:>>>')
        # self.printOut()
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next            
        else:
            counter = 1
            itr = self.head
            while itr:
                if index == counter:
                    if itr.next:
                        itr.next = itr.next.next
                    else:
                        itr.next = None
                itr = itr.next
                counter += 1
        
        # print('delete:>>>')
        # self.printOut()
        
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)