class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        right = 1
        output = 0
        while right < len(nums):
            if nums[right] <= nums[right-1]:
                output += nums[right-1] - nums[right] + 1
                nums[right] += nums[right-1] - nums[right] + 1
            if nums[right] > nums[right-1]:
                right += 1
        return output