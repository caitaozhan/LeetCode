#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (32.81%)
# Likes:    2590
# Dislikes: 65
# Total Accepted:    211.7K
# Total Submissions: 642.8K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    '''Use an increasing monotone stack
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n <= 0:
            return 0
        heights.append(0)
        stack = []
        maxx  = 0
        for i in range(n+1):
            while stack and heights[i] <  heights[stack[-1]]:
                right = stack[-1]
                while stack and heights[i] <  heights[stack[-1]]:
                    height_index  = stack.pop()
                    height = heights[height_index]
                    if stack:
                        left = stack[-1]
                    else:
                        left = -1
                    width  = right - left
                    area = height*width
                    maxx = max(maxx, area)
            stack.append(i)
        return maxx
        
        
# @lc code=end

