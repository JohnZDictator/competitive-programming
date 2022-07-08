class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # steps: 
            # 1. sort the array
            # 2. compare each adjacent elements of the array
            # 3. if any of two adjacent elements is found to be equal then return True
            # 4. if none found in the array then return False
        # Time Complexity - O(nlog(n))
        # Space Complexity - O(1)
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                return True
        return False