class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l, r = 0, 0
        res, total = 0, 0
        
        while r < len(nums):
            total += nums[r]
            
            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
        
#         nums.sort()
#         end = len(nums)-1
#         prev_end = len(nums)-2
        
#         frequent_counter = 1
#         k_needed = 0 
#         output = 0
        
#         while end > 1 and end > output:
#             k_needed += nums[end] - nums[prev_end]
            
#             while k_needed <= k and prev_end > -1:
#                 prev_end -= 1
#                 frequent_counter += 1
#                 k_needed += nums[end] - nums[prev_end]
            
#             output = max(frequent_counter, output)
            
#             frequent_counter = 1
#             k_needed = 0
#             end -= 1
#             prev_end = end - 1
#         return output