class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        self.upheap(arr, n, i)
        self.downheap(arr, n, i)
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n-1, -1, -1):
            self.heapify(arr, n, i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.remove(arr, n)
        arr.reverse()
    def remove(self, arr, n):
        self.buildHeap(arr, n)
        arr[0], arr[n-1] = arr[n-1], arr[0]
        if n > 0:
            self.remove(arr, n-1)
    def upheap(self, arr, n, i):
        parent = self.getParent(i)
        if i > 0 and arr[parent] > arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
            self.upheap(arr, n , i)
    def downheap(self, arr, n, i):
        leftChild = self.leftChild(i)
        rightChild = self.rightChild(i)
        minIndex = leftChild
        if minIndex < n and rightChild < n and arr[rightChild] < arr[leftChild]:
            minIndex = rightChild
        if minIndex < n and arr[minIndex] < arr[i]:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
            i = minIndex
            self.downheap(arr, n, i)
        
    def getMin(self, arr):
        return arr[0]
    
    def getParent(self, i):
        return (i-1)//2
    
    def leftChild(self, i):
        return 2*i+1
    
    def rightChild(self, i):
        return 2*i+2

if __name__ == '__main__':
    s = Solution()
    # print(s.buildHeap([4,1,3,9,7], 5))
    for i in range(10):
        print(i)
        print(s.downheap([10, 9,8,7,6,5,4,3,2,1], 10, i))