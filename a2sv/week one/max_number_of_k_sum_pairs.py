class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums)-1
        num_operations = 0
        nums.sort()
        while start < end:
            if nums[start] + nums[end] == k:
                num_operations += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1
        return num_operations
                
                