class Solution:
    def largestNumber(self, nums: List[int]) -> str:        
        start, end = 0, len(nums)-1
        
        if max(nums) == 0:
            return '0'
        
        while start < len(nums)-1:
            max1 = str(nums[start]) + str(nums[end])
            max2 = str(nums[end]) + str(nums[start])
            
            if start == end:
                start += 1
                end = len(nums)-1
            elif int(max1) >= int(max2):
                end -= 1
            elif int(max2) > int(max1):
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
        
        return ''.join(str(x) for x in nums)
                
        
    