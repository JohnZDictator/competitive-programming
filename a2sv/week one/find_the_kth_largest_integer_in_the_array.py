class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_int = []
        
        for i in range(len(nums)):
            nums_int.append(int(nums[i]))
        
        for j in range(1, k+1):
            max_index = nums_int.index(max(nums_int))
            if j == k:
                return str(nums_int[max_index])
            nums_int.pop(max_index)