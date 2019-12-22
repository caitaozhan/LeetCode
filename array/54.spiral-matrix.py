#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (32.08%)
# Likes:    1574
# Dislikes: 473
# Total Accepted:    294K
# Total Submissions: 913.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#

from typing import List

# @lc code=start
class Solution:
    ''' All we need to do is to find the patterns.
    '''
    def __init__(self):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)         # rows
        try:
            n = len(matrix[0])  # columns
        except:
            return []
        cur_loc = [0, -1]
        total_loc = m*n
        counter = 0
        direct  = 0
        spiral  = []
        stop = False
        while stop is False:
            steps = [n, m-1, n-1, m-2]   # steps for right, down, left, up
            for direct, step in zip(self.directions, steps):
                for _ in range(step):
                    cur_loc = [cur_loc[0] + direct[0], cur_loc[1] + direct[1]]
                    counter += 1
                    spiral.append(matrix[cur_loc[0]][cur_loc[1]])
                if counter == total_loc:
                    stop = True
                    break
            n -= 2
            m -= 2
        return spiral
            

# @lc code=end

