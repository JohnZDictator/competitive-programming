'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
        
        
    def binarySearch(self, nums, target, goLeft):
        left = 0
        right = len(nums)-1
        best = -1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                if goLeft:
                    right = mid-1
                    best = mid
                else:
                    left= mid+1
                    best = mid
        return best
                
                
            
            
            
        