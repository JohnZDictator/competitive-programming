class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        output = []
        
        count = Counter(changed)
        
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                output.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                output.append(num)
        
        if len(output) != len(changed)//2:
            return []
        
        return output 