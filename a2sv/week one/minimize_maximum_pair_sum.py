class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        start,end = 1,len(nums)-2
        nums.sort()
        
        min_val = nums[0] + nums[-1]
        
        while start < end:
            min_val = max(min_val, nums[start]+nums[end])
            start += 1
            end -= 1
           
        return min_val
        