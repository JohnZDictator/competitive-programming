class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        
        memo = {}
        def dp(idx):
            if idx > n:
                return 0
            if idx == n:
                return nums[idx]
            if idx in memo:
                return memo[idx]
            
            memo[idx] = max(dp(idx+2) + nums[idx], dp(idx+1))
            
            return memo[idx]
        
        return dp(0)