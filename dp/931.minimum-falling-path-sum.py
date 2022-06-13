#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    '''changing the matrix in place
    '''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif 1 <= j <= n-2:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
        return min(matrix[-1])
        
# @lc code=end

