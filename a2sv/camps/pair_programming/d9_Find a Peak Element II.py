class Solution:
    def findLocalPeak(self, i, j, mat):
        left_nbr = mat[i-1][j] if i-1 >= 0 else -1
        right_nbr = mat[i+1][j] if i+1 < len(mat) else -1
        top_nbr = mat[i][j-1] if j-1 >= 0 else -1
        bottom_nbr = mat[i][j+1] if j+1 < len(mat[0]) else -1
        
        if mat[i][j] < left_nbr:
            return self.findLocalPeak(i-1, j, mat)
        
        if mat[i][j] < right_nbr:
            return self.findLocalPeak(i+1, j, mat)
        
        if mat[i][j] < top_nbr: 
            return self.findLocalPeak(i, j-1, mat)
        
        if mat[i][j] < bottom_nbr:
            return self.findLocalPeak(i, j+1, mat)
        
        return [i, j]
        
        
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        return self.findLocalPeak(0, 0, mat)