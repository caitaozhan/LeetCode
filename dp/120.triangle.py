#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (43.47%)
# Likes:    1923
# Dislikes: 230
# Total Accepted:    243.7K
# Total Submissions: 559K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#

from typing import List

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        dp1, dp2 = [0]*n, [0]*n
        for i in range(0, n):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    dp2[j] = dp1[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp2[j] = dp1[j-1] + triangle[i][j]
                else:
                    dp2[j] = min(dp1[j-1], dp1[j]) + triangle[i][j]
            dp1, dp2 = dp2, dp1
        return min(dp1)


class Solution:
    '''6/12/2022 redo, space O(n^2) version
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = []
        for i in range(row):
            dp.append([0] * (i + 1))
        dp[0][0] = triangle[0][0]
        for i in range(1, row):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif i == j:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[row-1])


class Solution:
    '''6/12/2022 redo, flipping the triangle (thinking out of the box)
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]
        new_dp = [0] * n
        for i in reversed(range(n-1)):  # row: n-2, n-3, ..., 0
            for j in range(i+1):
                new_dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
            dp, new_dp = new_dp, dp
        return dp[0]

# @lc code=end

