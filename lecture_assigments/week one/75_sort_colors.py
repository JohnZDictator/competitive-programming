class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_val = nums[i]
            for j in range(i+1, len(nums)):
                if min_val > nums[j]:
                    min_val, nums[j] = nums[j], min_val
            nums[i] = min_val
        
        