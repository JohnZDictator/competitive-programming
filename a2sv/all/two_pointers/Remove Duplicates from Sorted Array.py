class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, 1
        curr_min = nums[0]
        counter = 1
        
        while right < n:
            if curr_min < nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    curr_min = nums[left]
                    left += 1
                    counter += 1
            elif nums[right] > curr_min:
                curr_min = nums[right]
                counter += 1
            right += 1
        return counter