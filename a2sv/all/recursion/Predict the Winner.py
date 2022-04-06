class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def maxPL1S(l, r, t):
            if l == r:
                if t == 0:
                    return nums[l]
                elif t == 1:
                    return 0
            
            if t == 0:
                return max(nums[l] + maxPL1S(l+1, r, 1-t), nums[r] + maxPL1S(l, r-1, 1-t))
            elif t == 1:
                return min(maxPL1S(l+1, r, 1-t), maxPL1S(l , r-1, 1-t))
        
        pl1s = maxPL1S(0, n-1, 0)
        total = sum(nums)
        pl2s = total - pl1s
        
        if pl1s >= pl2s:
            return True
        else:
            return False