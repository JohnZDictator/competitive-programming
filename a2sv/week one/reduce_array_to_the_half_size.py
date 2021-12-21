class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_frequency = {}
        
        output = 0
        total_frequency = 0
        
        for i in range(len(arr)):
            if str(arr[i]) in arr_frequency:
                arr_frequency[str(arr[i])] += 1
            else:
                arr_frequency[str(arr[i])] = 1
        
        while total_frequency < len(arr)/2:
            max_frequency = max(arr_frequency, key=arr_frequency.get)
            max_value = arr_frequency[max_frequency]
            
            if max_value == 1 and output == 0:
                output = len(arr)//2
                break
            
            arr_frequency.pop(max_frequency)
            
            total_frequency += int(max_value)
            output += 1
        
        return output