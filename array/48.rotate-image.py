#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

from typing import List

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def next_pixel(i: int, j: int, n: int):
            return j, n - 1 - i
        
        n = len(matrix)
        for row in range((n+1) // 2):
            square_length = n - 2*row
            for col in range(row, row + (square_length - 1)):
                i1, j1 = row, col
                i2, j2 = next_pixel(i1, j1, n)
                i3, j3 = next_pixel(i2, j2, n)
                i4, j4 = next_pixel(i3, j3, n)
                matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s = Solution()
s.rotate(matrix)
print(matrix)
        
# @lc code=end

