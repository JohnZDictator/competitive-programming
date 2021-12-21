class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        counter = 0
        end_index = len(arr)
        output = []
    
        while len(arr)-counter > 0 and arr != sorted(arr):
            max_element = max(arr[:len(arr)-counter])
            max_element_index = arr.index(max_element)
            # print(max_element, max_element_index)
            
            self.reverseSubArray(arr, max_element_index+1)
            output.append(max_element_index+1)
            self.reverseSubArray(arr, end_index-counter)
            output.append(end_index-counter)
            counter += 1
        
        return output
    
    def reverseSubArray(self, arr, k):
        for i in range(0, k//2):
            arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
        return arr