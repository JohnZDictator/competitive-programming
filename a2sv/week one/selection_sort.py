class Solution: 
    def select(self, arr, i):
        # code here
        for n in range(i, len(arr) - 1):
            min_element = arr[n]
            for m in range(i+1, len(arr)):
                if min_element > arr[j]:
                    min_element = arr[j]
        return min_element
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr) - 1):
            min_element = arr[i]
            temp = 0
            for j in range(i+1, len(arr)):
                if min_element > arr[j]:
                    temp = min_element
                    min_element = arr[j]
                    arr[j] = temp
            arr[i] = min_element
