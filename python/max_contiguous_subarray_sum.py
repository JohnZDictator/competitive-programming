class Solution:
    def maxContiguousSubarraySum(self, nums):
        max_sum_here = nums[0]
        max_sum_so_far = nums[0]
        for i in range(1, len(nums)):
            max_sum_here = max(max_sum_here + nums[i], nums[i])
            max_sum_so_far = max(max_sum_here, max_sum_so_far)

        return max_sum_so_far

if __name__ == '__main__':
    s = Solution()
    print(s.maxContiguousSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))