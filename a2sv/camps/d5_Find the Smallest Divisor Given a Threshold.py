class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        minVal = 1
        maxVal = max(nums)
        best = 0
        div = 0
        
        while minVal <= maxVal:
            total = 0
            div = (minVal+maxVal)//2
            for i in range(len(nums)):
                if nums[i]%div == 0:
                    total += nums[i]/div
                else:
                    total += (nums[i]//div)+1
            if total > threshold:
                minVal = div+1
            else:
                maxVal = div-1
                best = div
        return best