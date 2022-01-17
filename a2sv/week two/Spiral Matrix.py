class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = 1
        column = 1
        output = []
        row_min, row_max = 0, len(matrix)-1
        col_min, col_max = 0, len(matrix[0])-1
        
        while True:
            output, row_min = self.toRight(matrix, output, row_min, row_max, col_min, col_max)
            output, col_max = self.toBottom(matrix, output, col_max, col_min, row_min, row_max)
            output, row_max = self.toLeft(matrix, output, row_max, row_min, col_min, col_max)
            output, col_min = self.toTop(matrix, output, col_min, col_max, row_min, row_max)
            if col_min > col_max or row_min > row_max:
                break
        return output
    
    def check(self, m_min, m_max):
        if m_min > m_max:
            return False
        return True
    def toRight(self, matrix, output, curr_row, row_max, col_min, col_max):
        while col_min <= col_max and self.check(curr_row, row_max):
            output.append(matrix[curr_row][col_min])
            col_min += 1
        return output, curr_row+1
    
    def toBottom(self, matrix, output, curr_col, col_min, row_min, row_max):
        while row_min <= row_max and self.check(col_min, curr_col):
            output.append(matrix[row_min][curr_col])
            row_min += 1
        return output, curr_col-1
    def toLeft(self, matrix, output, curr_row, row_min, col_min, col_max):
        while col_min <= col_max and self.check(row_min, curr_row):
            output.append(matrix[curr_row][col_max])
            col_max -= 1
        return output, curr_row-1
    def toTop(self, matrix, output, curr_col, col_max, row_min, row_max):
        while row_min <= row_max and self.check(curr_col, col_max):
            output.append(matrix[row_max][curr_col])
            row_max -= 1
        return output, curr_col+1
        
        