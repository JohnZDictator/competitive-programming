import heapq

class Solution:
    def __init__(self):
        self.heaped = []
        self.deleted = {}
    def insert(self, val):
        heapq.heappush(self.heaped, val)
    def remove(self, val):
        self.deleted[val] = 1
    def printMin(self):
        while self.heaped[0] in self.deleted:
            heapq.heappop(self.heaped)
        return self.heaped[0]
    
if __name__ == '__main__':
    q = int(input())
    s= Solution()
    counter = 0
    while counter < q:
        inp = input().split()
        if inp[0] == '1':
            s.insert(int(inp[1]))
        elif inp[0] == '2':
            s.remove(int(inp[1]))
        elif inp[0] == '3':
            print(s.printMin())
        counter += 1
            
        
    
