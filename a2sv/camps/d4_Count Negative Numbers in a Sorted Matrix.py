'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        for i in range(len(grid)):
            left = 0 
            right = len(grid[i])-1
            best = None
            
            while left <= right:
                mid = left + (right-left)//2
                
                if grid[i][mid] >= 0:
                    left = mid+1
                else:
                    right = mid-1
                    best = mid
            if best != None:
                count += len(grid[i])-best
        return count