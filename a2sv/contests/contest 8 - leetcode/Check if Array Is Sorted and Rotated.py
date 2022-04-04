class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        min_element = float('inf')
        rotated = False
        
        for index in range(n-1):
            
            if not rotated and nums[index] > nums[index+1]:
                rotated = True
                min_element = nums[0]
            
            elif rotated and nums[index] > min_element:
                return False
        
            elif rotated and nums[index] > nums[index+1]:
                return False
        
        if rotated and nums[-1] > min_element:
            return False
        
        return True