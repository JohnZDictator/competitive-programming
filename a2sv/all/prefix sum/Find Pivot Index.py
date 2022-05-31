from collections import deque

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left, right = deque([nums[0]]), deque([nums[n]])
        
        count = 1
        while count <= n:
            left.append(left[-1] + nums[count])
            right.appendleft(right[0] + nums[n - count])
            count += 1
        
        for i in range(n+1):
            if left[i] == right[i]:
                return i
        return -1