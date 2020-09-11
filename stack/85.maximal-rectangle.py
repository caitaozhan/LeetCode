#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

from typing import List

# @lc code=start
class Solution:
    '''using the idea of collapse, time is O(n^2 * m), time beat 9%, n is the # of rows, m is the # of columns
    '''
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row  = len(matrix)
        if row == 0:
            return 0

        maxx = 0
        for i in range(row):
            for j in range(i, row):
                if j == i:
                    collapsed = matrix[i]
                else:
                    collapsed = self.collapse(collapsed, matrix[j])
                width = self.largest_continuous_one(collapsed)
                area = width*(j-i+1)
                # print(i, j, collapsed, area)
                maxx = max(maxx, area)
        return maxx

    def collapse(self, row1, row2):
        collapsed = []
        for a, b in zip(row1, row2):
            if a == '1' and b == '1':
                collapsed.append('1')
            else:
                collapsed.append('0')
        return collapsed

    def largest_continuous_one(self, row):
        maxx = 0
        cur = 0
        for e in row:
            if e == '1':
                cur += 1
                maxx = max(maxx, cur)
            else:
                cur = 0
        return maxx

# @lc code=end

