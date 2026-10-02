class NumMatrix:

    _matrix: List[List[int]] 

    def __init__(self, matrix: List[List[int]]):
            self._matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Use nested for loop
        sum = 0
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                sum += self._matrix[r][c]
        
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)