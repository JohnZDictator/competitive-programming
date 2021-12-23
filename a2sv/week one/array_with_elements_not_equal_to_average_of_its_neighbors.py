class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        start, end = 0, len(nums)-1
        output = []
        
        while len(output) != len(nums):
            output.append(nums[start])
            start += 1

            if start <= end:
                output.append(nums[end])
                end -= 1
                
        return output