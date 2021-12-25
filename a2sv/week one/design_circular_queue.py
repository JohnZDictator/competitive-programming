class MyCircularDeque:
     
    def __init__(self, k: int):
        self.maxSize = k
        self.deque = []
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque.insert(0, value) 
            print(len(self.deque), self.deque)
            return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque.insert(len(self.deque), value)
            return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque.pop(0)
            return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque.pop(len(self.deque)-1)
            return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[len(self.deque)-1]
    def isFull(self) -> bool:
        if len(self.deque) == self.maxSize:
            return True
        return False
    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        return False
    
#     def __init__(self, k: int):
#         self.front = -1
#         self.rear = -1
#         self.k = k
#         self.deque = [None] * self.k

#     def insertFront(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         elif self.isEmpty():
#             self.front, self.rear = 0, 0
#             self.deque[self.front] = value
#         elif self.front == 0:
#             self.front = self.k-1
#             self.deque[self.front] = value
#         else:
#             self.front -= 1
#             self.deque[self.front]
#         return True
#     def insertLast(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         elif self.isEmpty():
#             self.front, self.rear = 0, 0
#             self.deque[self.rear] = value
#         else:
#             self.rear = (self.rear + 1) % self.k
#             self.deque[self.rear] = value
#         return True
#     def deleteFront(self) -> bool:
#         if self.isEmpty():
#             return False
#         else:
#             self.deque[self.front] = None
#             self.front = (self.front + 1) % self.k
#         return True
#     def deleteLast(self) -> bool:
#         if self.isEmpty():
#             return False
#         else:
#             self.deque[self.rear] = None
#             if self.rear == 0:
#                 self.rear = -1
#             self.rear -= 1
#     def getFront(self) -> int:
#         return self.deque[self.front]

#     def getRear(self) -> int:
#         return self.deque[self.rear]

#     def isEmpty(self) -> bool:
#         if self.front == -1 and self.rear == -1:
#             return True
#         return False
#     def isFull(self) -> bool:
#         if self.front == 0 and self.rear == self.k-1 or self.rear == self.front-1:
#             return True
#         return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()