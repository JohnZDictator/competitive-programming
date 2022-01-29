class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtStart(self, data):
        node = Node(data, self.head)
        self.head = node
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print('Empty Linked List')
            return
        itr = self.head
        llStr = ''
        while itr:
            llStr += str(itr.data) + '-->'
            itr = itr.next
        print(llStr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    ll.insertAtEnd(9)
    ll.insertAtStart(8)
    ll.insertAtEnd(10)
    ll.insertAtStart(7)
    ll.print()
















# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insertAtStart(self, data):
#         node = Node(data, self.head)
#         self.head = node
#     def insertAtEnd(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)

#     def print(self):
#         if self.head is None:
#             print('Empty Linked List...')

#         itr = self.head
#         llStr = ''
#         while itr:
#             llStr += str(itr.data) + '--->'
#             itr = itr.next
#         print(llStr)

# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insertAtEnd(30)
#     ll.insertAtStart(5)
#     ll.insertAtStart(89)
#     ll.insertAtEnd(44)
#     ll.insertAtEnd(6)
#     ll.insertAtStart(21)
#     ll.print()