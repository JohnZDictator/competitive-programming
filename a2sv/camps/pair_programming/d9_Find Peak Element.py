class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # goto mid 
        # check left 
        # check right
        # if greater than both return mid
        # else go to greater
        # if both are greater go to right
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            left_nbr = nums[mid-1] if mid-1 >= 0 else -1*sys.maxsize
            
            right_nbr = nums[mid+1] if mid+1 < len(nums) else -1*sys.maxsize
            
            if nums[mid] > left_nbr and nums[mid] > right_nbr:
                return mid
            
            if right_nbr > nums[mid]:
                left = mid+1
                
            else:
                right = mid-1
    
        return -1