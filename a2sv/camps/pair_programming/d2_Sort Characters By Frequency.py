import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        myHeap = []
        maxFreq = []
        
        for key, value in frequency.items():
            heapq.heappush(myHeap, (-value, key))
        for i in frequency:
            popped = heapq.heappop(myHeap)
            maxFreq.append(popped[1]*(-popped[0]))
        
        return ''.join(maxFreq)
    

#         cccaacca
#         ['c', 'a', 'b']
#         [5, 3, 7]
        
#         s
#         'c', 'a'
#         freq = {'c': 3, 'a': 1}
#         freq = {'c': 5, 'a': 3, 'b': 7}
        
#         {'b': 7, 'c':5, 'a': 3}
        
#         ''.join()
        
#         output = ''
        
#         'b'*7 + 'c'*5, 'a'*3
        
#         cnt_arr = Counter(s)
#         output = []
        
#         freq_ele = {k: v for k, v in sorted(cnt_arr.items(), key=lambda item: item[1], reverse=True)}
    
#         for k in freq_ele:
#             output.append( k * freq_ele[k])
        
#         return ''.join(output)