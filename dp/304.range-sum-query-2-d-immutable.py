#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:
    ''' using a dp array with one extra element will make the code cleaner.
    '''
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0 for _ in range(n)] for _ in range(m)]
        self.prefix[0][0] = matrix[0][0]
        for i in range(1, m):
            self.prefix[i][0] = self.prefix[i-1][0] + matrix[i][0]
        for j in range(1, n):
            self.prefix[0][j] = self.prefix[0][j-1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                self.prefix[i][j] = self.prefix[i][j-1] + self.prefix[i-1][j] - self.prefix[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 >=1 and col1 >=1:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1-1][col1-1]
        if row1 == 0 and col1 >=1:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        if col1 == 0 and row1 >=1:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        if col1 == 0 and row1 == 0:
            return self.prefix[row2][col2] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

